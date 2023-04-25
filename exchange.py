python
import ccxt
import requests
import base64
import hashlib
import hmac
import urllib.parse
import time
from config import *

class Exchange():
    BASE_URL = 'https://cex.io/api'
    def __init__(self, api_key=API_KEY, secret_key=SECRET_KEY):
        self.api_key = api_key
        self.secret_key = secret_key
    def _nonce(self):
        """
        Метод создания нового значения параметра nonce для запросов к API биржи
        """
        return '{:.10f}'.format(time.time()).split('.')[0]

    def _sign_request(self, params):
        """
        Метод создания подписи запроса к API биржи
        """
        message = self._nonce() + self.api_key + urllib.parse.urlencode(params)
        signature = hmac.new(bytes(self.secret_key, 'latin-1'), 
                             msg=bytes(message, 'latin-1'),
                             digestmod=hashlib.sha256).digest()
        return base64.encodebytes(signature).rstrip().decode('utf-8')

    def _make_request(self, method, path, params):
        """
        Метод выполнения запроса к API биржи
        """
        headers = {'User-Agent': 'Mozilla/5.0'}
        params['nonce'] = self._nonce()
        params['signature'] = self._sign_request(params)
        response = requests.request(method, f'{self.BASE_URL}{path}',
                                    headers=headers,
                                    data=params,
                                    auth=(self.api_key, self.secret_key))
        return response.json()
    
     def get_data(self, currency_pair: str, time_interval: int):
    """
    Метод для получения котировок из биржи за определенный временной интервал

    :param currency_pair: Пара валют, для которой запрашиваем котировки
    :type currency_pair: str

    :param time_interval: Интервал времени
    :type time_interval: int

    :return: данные
    :rtype: код ответа биржи (например, 200) и JSON с ответом в случае успеха
    """

    binance = ccxt.binance()
    ohlcv = binance.fetch_ohlcv(currency_pair, time_interval)

    # Теперь данные, полученные с биржи, хранятся в переменной ohlcv
    # Осталось просто вернуть их
    return 200, ohlcv

def create_order(self, currency_pair: str, order_type: str, amount: float, price: float):
    """
    Метод для создания ордера на покупку или продажу валюты

    :param currency_pair: Пара валют, для которой создается ордер
    :type currency_pair: str

    :param order_type: Тип ордера ('buy' или 'sell')
    :type order_type: str

    :param amount: Количество валюты для покупки/продажи
    :type amount: float

    :param price: Цена за единицу валюты
    :type price: float

    :return: ID ордера, если его удалось создать; None в случае ошибки
    :rtype: int or None
    """

    # Реализация метода здесь
    pass

    def get_order_status(self, currency_pair, order_id):
        """
        Метод получения состояния ордера на бирже
        """
        # реализация получения состояния ордера
        return {}

    def get_order_history(self, currency_pair=None):
        """
        Метод получения истории ордеров на бирже
        """
        # реализация получения истории ордеров
        return []

    def log_order(self, order_response, row_num):
        """
        Метод логирования ордера в Google Sheets
        """
        # реализация логирования ордера
        return {}
