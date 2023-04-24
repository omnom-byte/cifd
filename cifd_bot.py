python
import requests
import time
import config
import logging
import indicators
from datetime import datetime
from typing import List
from backtest import Backtest
from exchange import Exchange

logging.basicConfig(
    filename=config.log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class Bot:
    def __init__(self):
        self.base_url = config.BASE_URL
        self.api_key = config.API_KEY
        self.secret_key = config.SECRET_KEY
        self.interval = config.interval
        self.backtesting = config.backtesting
        self.row_num = 2
        self.exchange = Exchange(self.base_url, self.api_key, self.secret_key)
        if self.backtesting:
            self.backtest = Backtest()

    def get_balance(self):
        """
        Метод получения баланса аккаунта на бирже
        """
        try:
            params = {'api_key': self.api_key}
            headers = {'Sign': self._sign(params)}
            response = requests.get(f'{self.base_url}/balance', headers=headers, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                return 'Ошибка получения баланса'
        except Exception as ex:
            return str(ex)

    def _sign(self, params):
        """
        Метод создания подписи запроса к API биржи
        """
        # реализация подписи запроса
        pass

    def get_dataframe(self):
        data = self.exchange.get_data(self.currency_pair, self.interval)
        return(data)

    def analyze_dataframe(self, df):
        self.RSI = indicators.rsi(df)
        self.MACD = indicators.macd(df)
        self.BollingerBands = indicators.bands(df)

    def generate_signals(self):
        long_signal = False
        short_signal = False
        if self.RSI <= 30 and self.MACD > 0:
            long_signal = True
        elif self.RSI >= 70 and self.MACD < 0:
            short_signal = True
        return(long_signal, short_signal)

    def execute_trade(self, long_signal, short_signal):
        if long_signal:
            order_response = self.exchange.create_order(self.currency_pair, 'buy')
        elif short_signal:
            order_response = self.exchange.create_order(self.currency_pair, 'sell')
        else:
            return
        return(order_response)

    def run(self, currency_pair):
        self.currency_pair = currency_pair
        while True:
            try:
                df = self.get_dataframe()
                self.analyze_dataframe(df)
                long_signal, short_signal = self.generate_signals()
                order_response = self.execute_trade(long_signal, short_signal)
                if self.backtesting:
                    self.backtest.log_row(
                        [datetime.now().strftime("%m/%d/%Y %H:%M:%S"), 
                        currency_pair, 
                        long_signal, 
                        short_signal, 
                        self.RSI, 
                        self.MACD, 
                        self.BollingerBands]
                    )
                else:
                    self.exchange.log_order(order_response, self.row_num)
                self.row_num += 1
            except Exception as e:
                logging.error(e)
            time.sleep(config.interval)
            
if __name__ == '__main__':
    bot = Bot()
    bot.run(currency_pair=config.currency_pair)
