  # Добавленное.
python    
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
        
    def initialize(self):
    logging.info('Bot initializing...')
    self.bot_start_time = time.time()
    self.df = pd.DataFrame(columns=['timestamp', 'symbol', 'open', 'high', 'low', 'close', 'volume', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    self.interval = config.INTERVAL
    self.period = config.PERIOD
    self.exchange = Exchange(config.API_KEY, config.API_SECRET)
    self.indicators = Indicators()
    self.wallet = self.get_wallet()
    self.google_sheets = GoogleSheetsAPI(config.GOOGLE_SHEETS_CREDS_FILE, config.SPREADSHEET_NAME)
    self.get_google_sheets_data()
    self.check_balance()
    self.backtest = config.BACKTEST
    
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
            self.get_balances()
            if self.backtest:
            backtest_res = self.backtest()
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
            
    def place_order(self, symbol, order_type, price):
    if order_type == 'BUY':
        available_amount = self.get_balances() / price
        self.exchange.place_order(symbol, 'BUY', available_amount, price)
        self.log_trade(symbol, 'BUY', price, available_amount)
    elif order_type == 'SELL':
        available_amount = self.get_balances(symbol)
        self.exchange.place_order(symbol, 'SELL', available_amount, price)
        self.log_trade(symbol, 'SELL', price, available_amount)
   
    def fetch_ohlcv(self, symbol, interval, limit):
        candles = self.exchange.fetch_ohlcv(symbol, interval=interval, limit=limit)
        df = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('date', inplace=True)
        df = df[['open', 'high', 'low', 'close', 'volume']]
        df = df.astype(float)
        return df
      
     def fetch_tickers(self):
        tickers = self.exchange.fetch_tickers()
        result = {}
        for pair in tickers:
            result[pair] = {
                'bid': tickers[pair]['bid'],
                'ask': tickers[pair]['ask']
            }
        return result
            
            def backtest(self, df):
        for i in range(self.df.shape[0] - 1):
            symbol_df = self.df.iloc[i:i+self.period]
             rsi_value = self.indicators.rsi(symbol_df['close'].values, self.period)
            macd_value, macd_signal = self.indicators.macd(symbol_df['close'].values, self.period)
            bb_bands = self.indicators.bollinger_bands(symbol_df['close'].values, self.period)
            bb_upper, bb_middle, bb_lower = bb_bands[0][-1], bb_bands[1][-1], bb_bands[2][-1]
            if rsi_value >= config.RSI_OVERBOUGHT and macd_value < macd_signal and latest_price <= bb_lower and self.balance > 0:
                self.balance = self.place_order(symbol, 'BUY', latest_price, self.balance)
            elif rsi_value <= config.RSI_OVERSOLD and macd_value > macd_signal and latest_price >= bb_upper:
                self.balance = self.place_order(symbol, 'SELL', latest_price, self.balance)

    def get_balances(self):
    balances = self.exchange.get_balances()
    self.balance = float(balances['BTC']['free'])
    print("Your current balance is: ", self.balance)

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

   
