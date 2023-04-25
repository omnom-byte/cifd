  # Добавленное.
    
import time
from datetime import datetime, timedelta
import pytz
import talib
import numpy as np
import pandas as pd
from exchange import ExchangeAPI
import config
from indicators import Indicators
import api
import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Bot:
    def __init__(self):
        self.exchange = ExchangeAPI()
        self.indicators = Indicators()
        self.wallet = {'USD': 0, 'BTC': 0, 'ETH': 0, 'XRP': 0}
        self.interval = config.INTERVAL
        self.period = config.PERIOD
        self.backtest = config.BACKTEST_MODE
        if self.backtest:
            self.df = pd.read_csv('historical_data.csv', index_col=0)
            self.df.index = pd.to_datetime(self.df.index)
            self.df = self.df.iloc[::-1]
        else:
            self.df = pd.DataFrame()
        self.bot_start_time = time.time()

    def run(self):
        logging.info('Bot started at {}'.format(datetime.now(pytz.timezone(config.TIMEZONE)).strftime('%Y-%m-%d %H:%M:%S')))
        while True:
            current_time = time.time()
            elapsed_time = current_time - self.bot_start_time
            if elapsed_time > config.LOG_INTERVAL * 3600:
                self.bot_start_time = current_time
                logging.info('Bot is still running at {}'.format(datetime.now(pytz.timezone(config.TIMEZONE)).strftime('%Y-%m-%d %H:%M:%S')))
            try:
                candles = self.exchange.get_candles()
            except Exception as e:
                logging.error(str(e))
                time.sleep(30)
                continue
            self.df = pd.concat([self.df, pd.DataFrame(candles)])
            self.df = self.df.drop_duplicates(subset=['timestamp'], keep='first')
            self.df = self.df.sort_values(by='timestamp')
            for symbol in config.PAIRS:
                try:
                    symbol_df = self.df[self.df['symbol'] == symbol]
                    if self.backtest:
                        latest_price = symbol_df.iloc[-1]['close']
                    else:
                        latest_price = self.exchange.get_latest_price(symbol)
                except Exception as e:
                    logging.error('Error with symbol {}: '.format(symbol) + str(e))
                    continue
                if len(symbol_df) > self.period:
                    rsi_value = self.indicators.rsi(symbol_df['close'].values, self.period)
                    macd_value, macd_signal = self.indicators.macd(symbol_df['close'].values, self.period)
                    bb_bands = self.indicators.bollinger_bands(symbol_df['close'].values, self.period)
                    bb_upper, bb_middle, bb_lower = bb_bands[0][-1], bb_bands[1][-1], bb_bands[2][-1]
                    if rsi_value >= config.RSI_OVERBOUGHT and macd_value < macd_signal and latest_price <= bb_lower:
                        self.place_order(symbol, 'BUY', latest_price)
                    elif rsi_value <= config.RSI_OVERSOLD and macd_value > macd_signal and latest_price >= bb_upper:
                        self.place_order(symbol, 'SELL', latest_price)
            time.sleep(self.interval)

    def get_wallet(self):
        wallet = self.exchange.get_wallet()
        self.wallet = wallet
        return wallet

    def place_order(self, symbol, order_type, price):
        if order_type == 'BUY':
            if self.wallet['USD'] > 0:
                amount_to_buy = self.wallet['USD'] / price
                self.exchange.place_order(symbol, 'BUY', amount_to_buy, price)
                self.get_wallet()
                self.log_trade(symbol, 'BUY', price, amount_to_buy)
        elif order_type == 'SELL':
            if self.wallet[symbol] > 0:
                self.exchange.place_order(symbol, 'SELL', self.wallet[symbol], price)
                self.get_wallet()
                self.log_trade(symbol, 'SELL', price, self.wallet[symbol])

    def log_trade(self, symbol, order_type, price, amount):
        api.log_trade(symbol, order_type, price, amount)
        self.log_balance()

    def log_balance(self):
        api.log_balance(self.wallet)

    def backtest_results(self):
        for symbol in config.PAIRS:
            symbol_df = self.df[self.df['symbol'] == symbol]
            if len(symbol_df) > self.period:
                rsi_values = self.indicators.rsi(symbol_df['close'].values, self.period)
                macd_values, macd_signals = self.indicators.macd(symbol_df['close'].values, self.period)
                bb_bands = self.indicators.bollinger_bands(symbol_df['close'].values, self.period)
                bb_upper, bb_middle, bb_lower = bb_bands[0][-1], bb_bands[1][-1], bb_bands[2][-1]

                signals = pd.DataFrame({
                    'rsi': rsi_values,
                    'macd': macd_values,
                    'macd_signal': macd_signals,
                    'bb_upper': bb_upper,
                    'bb_middle': bb_middle,
                    'bb_lower': bb_lower
                })

                signals['price'] = symbol_df['close'].values
                signals['return'] = np.log(signals['price'].shift(-1) / signals['price'])
                signals['signal'] = np.nan
                signals.loc[(signals['rsi'] >= config.RSI_OVERBOUGHT) & (signals['macd'] < signals['macd_signal']) & (signals['price'] <= signals['bb_lower']), 'signal'] = 1
                signals.loc[(signals['rsi'] <= config.RSI_OVERSOLD) & (signals['macd'] > signals['macd_signal']) & (signals['price'] >= signals['bb_upper']), 'signal'] = -1
                signals = signals.dropna()

                signals['strategy_return'] = signals['signal'] * signals['return']

                signals['cumulative_strategy_return'] = signals['strategy_return'].cumsum().apply(np.exp)

                final_return = signals['cumulative_strategy_return'].iloc[-1]

                api.log_backtest_results(symbol, final_return)

                self.plot_chart(signals, symbol)

    def plot_chart(self, signals, symbol):
        scope = ['https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(config.GOOGLE_SHEETS_CREDS_FILE, scope)
        client = gspread.authorize(creds)

        sheet_name = '{}_{}'.format(symbol, datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        sheet = client.create(sheet_name)
        worksheet = sheet.get_worksheet(0)

        # Writing data to worksheet.
        worksheet.update([signals.columns.values.tolist()] + signals.reset_index().values.tolist())

        # Adding chart.
        chart = worksheet.new_chart('LINE')
        chart.range('A1:G{}'.format(len(signals) + 1)))
        chart.axis('bottom', title='Date')
        chart.axis('left', title='Cumulative Strategy Return')
        chart.title('Cumulative Strategy Return for {}'.format(symbol))
        chart.line('cumulative_strategy_return', 'Cumulative Strategy Return')
        chart.execute()

        logging.info('Chart added to Google Sheets: {}'.format(sheet_name))
