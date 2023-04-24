> ChatGPT | Марти 🦓:
ChatGPT (беседа № 4):

Продолжай. 

Очень хорошо, что вы хотите использовать бота для торговли криптовалютой на бирже Binance или Coinbase. Для начала, вам нужно зарегистрироваться на бирже и создать API-ключ, который вы сможете использовать для управления ботом. После этого, вы можете приступить к разработке бота.

Для создания бота-эксперта, который будет основан на API биржи, я предлагаю использовать Python и следующие библиотеки:

1. python-binance  (для работы с API Binance) или coinbase (для работы с API Coinbase).
2. pandas (для анализа и обработки данных).
3. ccxt  (для работы с несколькими биржами в одном скрипте).
4. matplotlib (для визуализации данных).

Для создания API-интерфейса для управления ботом, я рекомендую использовать Flask - микрофреймворк для Python.

Начнем с создания бота, который будет основан на алгоритмическом подходе. Сначала нужно настроить API-ключ и подключиться к бирже. Для примера, я буду использовать библиотеку python-binance и Binance API.


import binance

api_key = 'your_api_key'
api_secret = 'your_api_secret'

client = binance.Client(api_key, api_secret)


Далее, мы получим доступ к данным криптовалюты. Для примера, я буду использовать данные о Bitcoin (BTC).


import pandas as pd

btc_data = client.get_historical_klines("BTCUSDT", binance.Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

btc_df = pd.DataFrame(btc_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])

btc_df = btc_df[['timestamp', 'open', 'high', 'low', 'close']]
btc_df['timestamp'] = pd.to_datetime(btc_df['timestamp'], unit='ms')
btc_df.set_index('timestamp', inplace=True)


Теперь мы можем использовать технический анализ графиков и различные индикаторы, чтобы оценить движение цены Bitcoin и принять решение о покупке или продаже.


import talib

sma20 = talib.SMA(btc_df['close'], timeperiod=20)
sma50 = talib.SMA(btc_df['close'], timeperiod=50)

if sma20[-1] > sma50[-1]:
    # купить Bitcoin
else:
    # продать Bitcoin


Теперь мы можем создать функцию, которая будет выполнять наши торговые решения.


def trade_bot():
    btc_data = client.get_historical_klines("BTCUSDT", binance.Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    btc_df = pd.DataFrame(btc_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    btc_df = btc_df[['timestamp', 'open', 'high', 'low', 'close']]
    btc_df['timestamp'] = pd.to_datetime(btc_df['timestamp'], unit='ms')
    btc_df.set_index('timestamp', inplace=True)
    
    sma20 = talib.SMA(btc_df['close'], timeperiod=20)
    sma50 = talib.SMA(btc_df['close'], timeperiod=50)

    if sma20[-1] > sma50[-1]:
        # купить Bitcoin
        order = client.order_market_buy(symbol='BTCUSDT', quantity=0.001)
        print(order)
    else:
        # продать Bitcoin
        order = client.order_market_sell(symbol='BTCUSDT', quantity=0.001)
        print(order)


Теперь мы можем запустить нашего бота, чтобы торговать криптовалютой на бирже Binance.


trade_bot()


Для создания API-интерфейса, мы можем использовать Flask. Создадим простой API-эндпоинт для запуска нашего бота.


from flask import Flask

app = Flask(__name__)

@app.route('/trade_bot', methods=['POST'])

> ChatGPT | Марти 🦓:
def run_trade_bot():
    trade_bot()
    return 'Trade bot executed!'

if __name__ == '__main__':
    app.run(debug=True)


Теперь мы можем отправлять POST-запросы нашему API-эндпоинту, чтобы запускать нашего торгового бота.

Чтобы обеспечить безопасность нашего бота, мы можем использовать модуль Python PyNaCl, чтобы зашифровать наши API-ключи.

Например:


import nacl
import nacl.secret
import nacl.utils

key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
box = nacl.secret.SecretBox(key)

api_key = 'your_api_key'
api_secret = 'your_api_secret'

encrypted_api_key = box.encrypt(api_key.encode())
encrypted_api_secret = box.encrypt(api_secret.encode())

print(encrypted_api_key)
print(encrypted_api_secret)

# Разшифровка:
decrypted_api_key = box.decrypt(encrypted_api_key).decode()
decrypted_api_secret = box.decrypt(encrypted_api_secret).decode()

print(decrypted_api_key)
print(decrypted_api_secret)


Теперь вы можете использовать этот код, чтобы создать свой собственный торговый бот на базе API биржи Binance или Coinbase. Убедитесь, что вы соблюдаете все меры безопасности, чтобы защитить свои криптоактивы.

 для создания бота-эксперта необходимо использовать алгоритмический подход для краткосрочных сделок. Это можно сделать с помощью различных методов анализа и стратегии торговли на основе данных и паттернов. Для этого необходимо определить подходящий набор функций и алгоритмов для использования и интеграции.

Для обеспечения безопасности Вашего бота, необходимо использовать достаточно криптографических методов и систем хранения криптовалюты. Вы можете использовать определенные методы хранения, такие как холодное хранилище и двухфакторная аутентификация для защиты своей торговой деятельности.

Также, Вам необходимо будет создать специальный API-интерфейс для управления ботом, чтобы можно было интегрировать его в личный кабинет на бирже. Он будет позволять устанавливать параметры торговли, следить за балансом и результатами торгового бота в режиме реального времени.

Пример кода, который может использоваться для создания бота, включает следующие языки программирования и библиотеки:

python
import ccxt
import time

# создаем объекты биржи Binance и Coinbase, используя API-ключи
binance = ccxt.binance({'apiKey': 'YOUR_API_KEY', 'secret': 'YOUR_SECRET_KEY'})
coinbase = ccxt.coinbasepro({'apiKey': "YOUR_API_KEY", 'secret': "YOUR_SECRET_KEY"})

# установка цен, по которым будем продавать и покупать BTC
sell_price = 35000
buy_price = 30000

# функция для покупки BTC на Binance
def buy_btc_on_binance():
    binance.create_order('BTC/USD', type='limit', side='buy', amount=1, price=buy_price)

# функция для продажи BTC на Coinbase
def sell_btc_on_coinbase():
    coinbase.create_order('BTC/USD', type='limit', side='sell', amount=1, price=sell_price)

# бесконечный цикл для торговли BTC
while True:
    # получаем текущие курсы BTC
    binance_btc_price = binance.fetch_ticker('BTC/USD')['last']
    coinbase_btc_price = coinbase.fetch_ticker('BTC/USD')['last']
    
    # проверяем, можно ли продавать на Coinbase и покупать на Binance
    if coinbase_btc_price > sell_price and binance_btc_price < buy_price:
        buy_btc_on_binance()
        time.sleep(60)
        sell_btc_on_coinbase()
        time.sleep(60)
    else:
        time.sleep(60)
> ChatGPT | Марти 🦓:
ChatGPT (беседа № 5):
Выбрана Ваша тестовая роль

Существует несколько способов расширения функционала бота для увеличения стабильности его дохода.

1. Принципы рискового управления - бот должен иметь возможность управлять рисками своих торговых стратегий таким образом, чтобы не рисковать слишком много капитала в одной операции, следуя строгой стратегии управления капиталом. 

Пример: В зависимости от рыночных условий и анализа, бот может автоматически устанавливать размер позиций, на которые он готов пойти, в соответствии с текущим уровнем риска в портфеле. Это позволяет управлять рисками на определенном уровне и избегать катастрофических потерь.

2. Диверсификация рисков - бот должен иметь возможность использовать различные методы и стратегии, чтобы диверсифицировать риски и увеличить доходность портфеля.

Пример: Бот может использовать кроме технического анализа и анализа рыночной ситуации другие данные известные на рынке. Он может использовать фундаментальный анализ, чтобы искать потенциально выгодные инвестиции, проверять новости и события в отношении криптовалют, которые могут повлиять на рынок.

3. Усовершенствование алгоритмов - бот должен иметь возможность постоянно улучшать свои алгоритмы для анализа рынка и принятия решений.

Пример: Бот может использовать машинное обучение и нейронные сети для анализа больших объемов данных и постоянного улучшения его прогнозирующих алгоритмов.

Вот пример кода для создания новой стратегии торговли на базе RSI (Relative Strength Index) и MACD (Moving Average Convergence Divergence) индикаторов:


import pandas as pd
import ta.momentum as momentum
import ta.trend as trend
from binance.client import Client
from binance.enums import *
from decimal import Decimal, getcontext

client = Client(API_KEY, API_SECRET)

PAIR = 'BTCUSDT'
INTERVAL = '1h'
RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

def get_rsi(client, pair, interval):
    df = pd.DataFrame(client.futures_historical_klines(symbol=pair, interval=interval, limit=500))
    df = df.iloc[:, :6]
    df.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    df.set_index('time', inplace=True)
    df = df.astype(float)
    df['rsi'] = momentum.RSIIndicator(df['close'], window=14).rsi()
    return df

def get_macd(client, pair, interval):
    df = pd.DataFrame(client.futures_historical_klines(symbol=pair, interval=interval, limit=500))
    df = df.iloc[:, :6]
    df.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    df.set_index('time', inplace=True)
    df = df.astype(float)
    df['macd'] = trend.MACD(df['close'], n_fast=MACD_FAST, n_slow=MACD_SLOW, n_sign=MACD_SIGNAL).macd()
    return df

def buy(client, pair, quantity):
    order = client.futures_create_order(symbol=pair, side='BUY', type='MARKET', quantity=quantity)
    return order

def sell(client, pair, quantity):
    order = client.futures_create_order(symbol=pair, side='SELL', type='MARKET', quantity=quantity)
    return order

def main():
    rsi_df = get_rsi(client, PAIR, INTERVAL)
    macd_df = get_macd(client, PAIR, INTERVAL)
    rsi = rsi_df['rsi'][-1]
    macd = macd_df['macd'][-1]
    position_size = Decimal(client.futures_account_balance().get('USDT').get('balance'))
    
    if rsi < RSI_OVERSOLD and macd > 0:
        # Place buy order
        buy_qty = round(position_size * 0.1 / Decimal(client.futures_symbol_ticker(symbol=PAIR).get('price')))
        buy(client, PAIR, buy_qty)
    elif rsi > RSI_OVERBOUGHT and macd < 0:
        # Place sell order
        quantity = client.futures_position_information(symbol=PAIR)[0]['positionAmt']

> ChatGPT | Марти 🦓:
        sell_qty = abs(int(float(quantity)))
        sell(client, PAIR, sell_qty)
    else:
        return
        
if __name__ == '__main__':
    main()


Этот код осуществляет стратегию торговли на базе RSI индикатора и MACD. Если RSI переходит через заданные значения RSI_OVERSOLD и RSI_OVERBOUGHT и MACD меняется соответственно, бот автоматически размещает ордер на покупку или продажу в соответствии с текущей позицией на рынке.

1. Scalping - стратегия, которая основывается на краткосрочной торговле криптовалютой с использованием технического анализа и торговых индикаторов. Для этого можно использовать API индикаторы, такие как Bollinger Bands, Moving Average, Relative Strength Index (RSI) и т.д. Пример кода:


def scalping(api, symbol, amount):
    # Получение текущей цены на момент вызова функции
    ticker = api.get_ticker(symbol)
    price = float(ticker['lastPrice'])
    # Вычисление цены покупки и продажи, основываясь на маржинальном уровне
    buy_price = price - price * 0.01
    sell_price = price + price * 0.01
    # Отправка ордера на покупку с установкой стоп-лосса
    order = api.create_order(symbol, 'BUY', 'LIMIT', amount, buy_price, {'stopPrice': buy_price - buy_price * 0.005})
    # Ожидание выполнения ордера
    while not api.is_order_filled(order['orderId']):
        time.sleep(1)
    # Отправка ордера на продажу с установкой тейк-профита
    order = api.create_order(symbol, 'SELL', 'LIMIT', amount, sell_price, {'type': 'TAKE_PROFIT_LIMIT', 'timeInForce': 'GTC', 'stopPrice': sell_price + sell_price * 0.005})
    # Ожидание выполнения ордера
    while not api.is_order_filled(order['orderId']):
        time.sleep(1)
2. Trend Following - стратегия, которая основывается на направлении тренда рынка. Для этого можно использовать индикаторы направления тренда (например, Moving Average или Ichimoku Kinko Hyo) и сигнальные индикаторы (например, MACD или Stochastic Oscillator). Пример кода:


def trend_following(api, symbol, amount):
    # Получение последней исторической свечи на момент вызова функции
    klines = api.get_klines(symbol, '1d', 1)
    close_prices = [float(kline[4]) for kline in klines]
    # Вычисление скользящей средней и текущего ценового положения
    sma = talib.SMA(np.array(close_prices), timeperiod=20)
    current_price = float(api.get_ticker(symbol)['lastPrice'])
    # Определение направления тренда и принятие решения о покупке или продаже
    if current_price > sma[-1]:
        order = api.create_order(symbol, 'BUY', 'MARKET', amount)
    elif current_price < sma[-1]:
        order = api.create_order(symbol, 'SELL', 'MARKET', amount)
    # Ожидание выполнения ордера
    while not api.is_order_filled(order['orderId']):
        time.sleep(1)

Это только примерные подходы и код, который можно использовать в реализации бота. Необходимо учитывать, что рынок криптовалют является высокорисковым и результаты использования той или иной стратегии могут быть разными в зависимости от ситуации на рынке. Однако, соответствующая настройка бота и использование API позволят автоматизировать торговлю и могут значительно упростить жизнь трейдера.

Например, для технического анализа бот может использовать индикаторы, такие как SMA (скользящая средняя цена), RSI (индекс относительной силы) и MACD (скользящая средняя сходимости/расхождения). Они могут быть реализованы в виде отдельных классов, которые будут предоставлять методы расчета значений этих индикаторов для каждого нового бара.

Код может выглядеть примерно так:

python
class TechnicalIndicators:
    def __init__(self, prices):
        self.prices = prices

    def calc_sma(self, period):
        """Рассчитать простую скользящую среднюю"""
        sma = np.mean(self.prices[-period:])
        return sma

    def calc_rsi(self, period=14):
        """Рассчитать индекс относительной силы"""
        delta = np.diff(self.prices)
        gains = delta.clip(min=0)
        losses = -delta.clip(max=0)
        avg_gain = np.mean(gains[-period:])
        avg_loss = np.mean(losses[-period:])
        rs = avg_gain / avg_loss
        rsi = 100.0 - (100.0 / (1.0 + rs))
        return rsi

    def calc_macd(self, fast_period=12, slow_period=26, signal_period=9):
        """Рассчитать скользящую среднюю сходящуюся/расходящуюся"""
        fast_ema = pd.Series(self.prices).ewm(span=fast_period, min_periods=fast_period).mean()
        slow_ema = pd.Series(self.prices).ewm(span=slow_period, min_periods=slow_period).mean()
        macd = fast_ema - slow_ema
        signal = macd.ewm(span=signal_period, min_periods=signal_period).mean()
        return macd, signal

Здесь создается класс TechnicalIndicators, который принимает на вход массив цен и предоставляет методы для расчета SMA, RSI и MACD. Методы используют модули numpy и pandas, так что их нужно импортировать в начале скрипта.

Для использования этих индикаторов внутри самого бота можно вызывать соответствующие методы, например:

python
prices = get_recent_prices()  # получить последние цены с биржи
tech_inds = TechnicalIndicators(prices)
sma = tech_inds.calc_sma(period=20)
rsi = tech_inds.calc_rsi(period=14)
macd, signal = tech_inds.calc_macd(fast_period=12, slow_period=26, signal_period=9)

Здесь мы создаем экземпляр класса TechnicalIndicators и вызываем его методы для расчета индикаторов на последних доступных ценах. Полученные значения могут использоваться дальше в боте для принятия решений о торговле.

Первым шагом необходимо выбрать биржу для работы с криптовалютой. Binance и Coinbase - это отличные выборы, так как они предоставляют API для торговли и хорошо зарекомендовали себя на рынке.

Далее, нам нужно создать бота, который будет использовать этот API для автоматической торговли криптовалютой. Для этого мы можем использовать Python и его библиотеку для работы с API - requests.

Для того, чтобы бот обеспечивал стабильный доход в размере около двухсот долларов в месяц, мы можем включить в его функционал следующие стратегии:

1. Стратегия покупки на дипах: бот будет покупать криптовалюту на небольшом падении цены и продавать при росте. Это может быть реализовано с помощью анализа графиков и использования технических индикаторов.

Вот пример кода для создания ордера на покупку на Binance:

 python
import requests

def buy(symbol, quantity):
    api_key = 'your_api_key'
    secret_key = 'your_secret_key'
    
    url = 'https://api.binance.com/api/v3/order'
    
    params = {
        'symbol': symbol,
        'side': 'BUY',
        'type': 'MARKET',
        'quantity': quantity,
        'timestamp': int(time.time() * 1000)
    }
    
    params['signature'] = hmac.new(secret_key.encode(), urlencode(params).encode(), hashlib.sha256).hexdigest()
    
    headers = {
        'X-MBX-APIKEY': api_key
    }
    
    response = requests.post(url, headers=headers, params=params)
    
    return response.json()


2. Стратегия следования тренду: бот будет покупать криптовалюту до тех пор, пока ее цена продолжает расти, и продавать при снижении. Такая стратегия может быть реализована с помощью анализа рыночной капитализации и роста спроса на криптовалюту.

3. Стратегия скользящего среднего: бот будет покупать криптовалюту, когда ее цена превышает определенное значение скользящего среднего, и продавать при снижении ниже этого значения.

Чтобы бот мог осуществлять анализ рынка, мы можем использовать API доступные у Binance и Coinbase. 

Вот пример запроса к API Binance для получения последних свечей по паре BTCUSDT:

 python
import requests

url = 'https://api.binance.com/api/v3/klines'

params = {
    'symbol': 'BTCUSDT',
    'interval': '1d',
    'limit': 30
}

response = requests.get(url, params=params)

candles = response.json()

Данный код получит свечи для пары BTCUSDT за последние 30 дней на интервале 1 день. Можно использовать различные параметры, чтобы получить нужную информацию.

Я надеюсь, что эта информация поможет тебе разработать бота для автоматической торговли криптовалютой с использованием API Binance или Coinbase и различных стратегий торговли.

Пример кода, реализующего стратегию скользящих средних:

python
def moving_average_strategy(data, short_window=50, long_window=200):
    # Разделение данных на короткий и длинный периоды
    short_rolling = data.rolling(window=short_window).mean()
    long_rolling = data.rolling(window=long_window).mean()

    # Определение сигнала: короткий период пересекает длинный период сверху вниз
    if short_rolling[-1] < long_rolling[-1] and short_rolling[-2] > long_rolling[-2]:
        return 'sell'
    # Определение сигнала: короткий период пересекает длинный период снизу вверх
    elif short_rolling[-1] > long_rolling[-1] and short_rolling[-2] < long_rolling[-2]:
        return 'buy'
    # Без сигнала
    else:
        return 'hold'

В этом примере функция moving_average_strategy принимает DataFrame, содержащий ценовые данные актива, а также опциональные параметры short_window и long_window, указывающие длину короткого и длинного периодов скользящих средних. Функция рассчитывает короткий и длинный периоды скользящих средних и определяет сигнал на основе пересечения короткого и длинного периодов. Если короткий период пересекает длинный период сверху вниз, функция возвращает "sell", если короткий период пересекает длинный период снизу вверх, функция возвращает "buy", в противном случае функция возвращает "hold".

Для управления рисками в боте можно использовать различные алгоритмы, такие как стоп-лосс, тейк-профит, а также многие другие. Например, можно реализовать следующую логику для стоп-лосса: если цена криптовалюты упадет на определенный процент, бот автоматически продаст заданное количество криптовалюты. Для реализации такой логики в коде можно использовать следующую функцию:

def stop_loss(symbol, current_price, threshold):
    # получение текущей позиции по указанному символу
    position = get_position(symbol)
    # расчет цены продажи с учетом заданного процента
    sell_price = current_price * (1 - threshold)
    # проверка наличия достаточного числа криптовалюты для продажи
    if position.quantity > 0 and current_price <= sell_price:
        # запрос на продажу криптовалюты по заданной цене
        response = sell(symbol, position.quantity, sell_price)
        if response['status'] == 'filled':
            # получение информации о выполненной сделке
            trade = get_trade(response['tradeId'])
            # вывод информации о сделке
            logging.info(f'Trade executed. Symbol: {symbol}. Side: sell. '
                         f'Price: {trade.price}. Quantity: {trade.quantity}. '
                         f'Total value: {trade.price * trade.quantity}.')

Чтобы пользователь мог настраивать поведение бота на основе своей рисковой толерантности, нужно предоставить ему возможность задавать параметры для каждого алгоритма управления рисками и выбирать степень воздействия на результаты торговли. Это можно реализовать путем введения соответствующих параметров в интерфейс управления ботом и сохранения этих параметров в базе данных. Например, для задания порога выпадения стоп-лосса можно использовать следующий параметр:

threshold = user_settings['stop_loss_threshold']
где user_settings - объект, содержащий настройки пользователя, а stop_loss_threshold - параметр, заданный пользователем для стоп-лосса.

Вот пример кода на Python, который может использоваться для реализации функции уведомлений:


def send_notification(message):
    # Реализация функции отправки уведомлений
    pass

# Пример использования функции отправки уведомлений
send_notification("Новая сделка на Binance: покупка BTC по 6000$")

Приложу пример кода стратегии скользящего среднего на языке Python:

python
class MovingAverageStrategy:
    def __init__(self, fast_period, slow_period):
        self.fast_period = fast_period
        self.slow_period = slow_period
        self.fast_ma = MovingAverage(fast_period)
        self.slow_ma = MovingAverage(slow_period)
   
    def tick(self, candle):
        self.fast_ma.add(candle.close)
        self.slow_ma.add(candle.close)

        if self.fast_ma.avg > self.slow_ma.avg:
            return SIGNAL_BUY
        elif self.fast_ma.avg < self.slow_ma.avg:
            return SIGNAL_SELL

        return SIGNAL_HOLD

Здесь мы создаем класс MovingAverageStrategy и инициализируем его, передавая значения параметров fast_period и slow_period, которые отвечают за длину периода скользящих средних. Затем мы инициализируем два объекта класса MovingAverage, которые будут отвечать за подсчет скользящих средних соответствующих периодов. В методе tick мы добавляем текущее значение цены закрытия свечи к объектам MovingAverage и проверяем, пересекает ли быстрое скользящее среднее медленное, что дает сигнал к покупке, и наоборот – сигнал к продаже. Если скользящие средние пересекаются, но не меняют свое положение относительно друг друга, мы возвращаем сигнал на удержание.

Вот пример функции для стратегии покупки на дипах:

python
def dip_buying_strategy(market_data, threshold = 0.02, window = 5):
    """
    market_data: pandas.DataFrame
        Данные рынка криптовалют, содержащие цены открытия, максимальные, минимальные и закрытия
    threshold: float
        Пороговое значение, на которое должен снизиться цена
    window: int
        Размер окна, в котором проверяется процентное изменение цены
    """
    current_price = market_data['close'].iloc[-1]
    min_price = market_data['close'].iloc[-window:].min()
    percent_change = (min_price - current_price) / current_price

    if percent_change >= threshold:
        return 'buy'
    else:
        return 'hold'

Эта функция проверяет, снизилась ли цена криптовалюты более чем на 2% за последние 5 дней. Если это так, функция возвращает "buy", иначе "hold".

Для реализации стратегии Bollinger Bands нужно вычислить текущие значения средней линии и верхней/нижней полосы на основе исторических данных о ценах на криптовалюту. Затем необходимо определить положение текущей цены криптовалюты относительно полос Боллинджера, чтобы понимать, когда покупать или продавать.

Реализация этой стратегии может выглядеть следующим образом:

python
import pandas as pd
import numpy as np
import talib

# исторические данные цен на криптовалюту
data = pd.read_csv('data.csv')

# вычисление средней линии боллинджеровских полос
bbands = talib.BBANDS(data['Close'])

# определение положения текущей цены относительно полос Боллинджера
if data['Close'][-1] > bbands[0][-1] + 2 * np.std(data['Close']):
    # если текущая цена выше верхней полосы, то продаем
    sell()
elif data['Close'][-1] < bbands[2][-1] - 2 * np.std(data['Close']):
    # если текущая цена ниже нижней полосы, то покупаем
    buy()
else:
    # если текущая цена находится внутри полос, то ничего не делаем
    pass

Этот код использует библиотеку TA-Lib для вычисления Bollinger Bands на основе исторических данных цен на криптовалюту. Затем с помощью стандартного отклонения текущей цены от среднего значения мы определяем, находится ли цена на краях полосы или внутри нее. В зависимости от этого мы покупаем или продаем.

Пример кода для реализации стратегии на базе Bollinger Bands:

python
import talib
import numpy as np

def bollinger_bands_strategy(df, n, k):
    """Bollinger Bands trading strategy implemented using TA-Lib."""
    
    # Calculate Bollinger Bands
    std = df['Close'].rolling(n).std(ddof=0)
    mid = df['Close'].rolling(n).mean()
    upper = mid + k * std
    lower = mid - k * std
    
    # Check for buy/sell signals
    df['Signal'] = np.where(df['Close'] > upper, -1, np.nan)
    df['Signal'] = np.where(df['Close'] < lower, 1, df['Signal'])
    
    # Forward fill the signal to represent holding the position
    df['Signal'].fillna(method='ffill', inplace=True)
    
    # Determine the daily returns of the strategy
    df['Returns'] = df['Close'].pct_change() * df['Signal'].shift(1)
    df['Cumulative Returns'] = (1 + df['Returns']).cumprod()
    
    return df

Функция bollinger_bands_strategy принимает исторические данные о ценах, количество периодов для расчета стандартного отклонения, а также коэффициент k, который определяет расстояние между верхней и средней линией Bollinger Bands.

Для расчета индикатора Bollinger Bands используется метод rolling для скользящего среднего и стандартного отклонения. Затем формулы для расчета верхней и нижней линий используются для определения покупки и продажи.

Сигналы покупки / продажи представлены в столбце «Signal», который представляет собой 1 для покупки и -1 для продажи. Эти значения устанавливаются с помощью метода where библиотеки NumPy, в котором проверяется, превышает ли текущее значение цены верхнюю линию или нижнюю линию Bollinger Bands.

Наконец, определяются ежедневные доходы и годовая доходность путем расчета произведения относительных изменений цены и сигналов.


Например, для метода Келли возможный код может выглядеть следующим образом:


bet_size = ((win_rate * avg_win) - (loss_rate * avg_loss)) / avg_win

где bet_size - размер торговой позиции, win_rate - вероятность выигрыша сделки, avg_win - средний выигрыш, loss_rate - вероятность проигрыша сделки и avg_loss - средний проигрыш.

Для оценки степени риска и рассчета размера торговой позиции бот может использовать различные методы управления капиталом. Один из таких методов - алгоритм Фиксированного Риска (Fixed Risk). Этот алгоритм определяет размер торговой позиции на основе уровня риска, который вы готовы принять при входе в сделку. Конкретный размер позиции будет зависеть от объема капитала и уровня профита и риска, заданных вами.

Например, при использовании метода Фиксированного Риска, бот может расчитывать размер торговой позиции следующим образом:


def calculate_position_size(account_balance, risk_percent, stop_loss_percent, buy_price):
    """Calculate position size based on account balance and risk parameters."""
    risk_amount = account_balance * (risk_percent / 100)
    stop_loss_amount = buy_price * (stop_loss_percent / 100)
    position_size = round(risk_amount / stop_loss_amount, 2)
    return position_size

В этом примере мы передаем в функцию размер вашего счета, процент риска, процент стоп-лосса и цену покупки. Функция расчитывает объем позиции на основе этих параметров. Она сначала расчитывает размер суммы, которую вы готовы рисковать, используя процент риска и баланс счета. Затем она расчитывает размер стоп-лосс путем умножения цены покупки на процент стоп-лосса. Наконец, она определяет размер торговой позиции, разделив сумму риска на размер стоп-лосса.
Вот пример кода на Python, который может быть использован для расчета размера позиции в методе Константного Риска:


def calculate_position_size(account_balance, risk_percentage, entry_price, stop_loss_price):
    risk_amount = account_balance * (risk_percentage / 100)
    position_size = risk_amount / abs(entry_price - stop_loss_price)
    return position_size

При использовании Мартингейла бот будет удваивать размер торговой позиции после каждой убыточной сделки и снижать ее размер после каждой прибыльной сделки.

Вот пример кода на Python, который может быть использован для реализации метода Мартингейла:


def calculate_position_size(account_balance, num_consecutive_losses, initial_position_size, martingale_factor):
    # Вычисляем размер позиции, используя метод Мартингейла
    position_size = initial_position_size * (martingale_factor ** num_consecutive_losses)
    # Приводим размер позиции к допустимому значению, основываясь на балансе
    if position_size * entry_price > account_balance:
        position_size = account_balance / entry_price
    return position_size

В любом случае, использование Мартингейла может нести за собой серьезный риск и привести к потере капитала, особенно если рынок не расположен к вашей стратегии. Поэтому перед тем, как включать его в бота, необходимо тщательно взвесить все риски и преимущества.
Пример кода на Python для реализации метода Мартингейла:

python
# Основная функция
def martingale(price, buy_amount, max_loss):
    # Задаем значения buy_price и lot
    buy_price = price
    lot = buy_amount

    # Устанавливаем цену выхода из позиции
    sell_price = buy_price - max_loss

    # Если цена упала ниже уровня тейк-профита, то продаем
    if price <= sell_price:
        return "Sell"

    # В противном случае увеличиваем объем позиции
    else:
        while 1:
            # Увеличиваем лот
            lot = lot * 2

            # Покупаем на новый уровень
            buy_price = ((buy_amount * price) + (lot * price)) / (buy_amount + lot)
            sell_price = buy_price - max_loss

            # Если цена снова продолжает падать, то продолжаем увеличивать лот
            if price <= sell_price:
                return "Sell"

Рассмотрим также метод Константного Риска (Constant Risk). Это метод, при котором риск и уровень stop-loss для каждой торговой позиции устанавливаются на определенный процент от общего баланса счета. Этот метод может быть более безопасным, чем Мартингейл, но также требует настройки соответствующих параметров в коде бота.

Пример кода на Python для реализации метода Константного Риска:

python
# Основная функция
def constant_risk(price, balance, risk_percent):
    # Задаем процент риска
    risk_amount = balance * (risk_percent/100)

    # Устанавливаем цену выхода из позиции
    sell_price = price - risk_amount

    # Если цена упала ниже уровня тейк-профита, то продаем
    if price <= sell_price:
        return "Sell"

    # Иначе покупаем актив
    else:
        return "Buy"

В итоге, выбор между Мартингейлом и Константным Риском зависит от индивидуальных предпочтений и уровня риска, который готов принять трейдер.

Пример кода для расчета размера позиции с использованием коэффициента Келли:


import numpy as np

def kelly_criterion(win_probability, win_loss_ratio):
    return (win_probability - (1 - win_probability) / win_loss_ratio)

win_probability = 0.6
win_loss_ratio = 2.0

kelly_fraction = kelly_criterion(win_probability, win_loss_ratio)
capital = 1000
position_size = capital * kelly_fraction

print("Kelly fraction:", kelly_fraction)
print("Position size:", position_size)

В данном примере для расчета размера позиции используется коэффициент Келли, который рассчитывается на основе предполагаемой вероятности успеха сделки и соотношения дохода к потенциальным потерям. Размер позиции рассчитывается, умножая капитал на коэффициент Келли.
Первый шаг – установить зависимости, которые нам понадобятся:

npm install ccxt mathjs ta-lib

Они включают в себя библиотеку ccxt для работы с API биржей, библиотеку math.js для математических операций и библиотеку TA-lib для создания технических индикаторов.

Затем мы должны определить настройки для бота - общие параметры.


const ccxt = require('ccxt');
const math = require('mathjs');
const ta = require('ta-lib');

// Общие настройки бота
const config = {
  tradingEnabled: true,
  interval: '5m', // Интервал свечей
  symbol: 'BTC/USDT', // Пара торговли
  amount: 0.01, // Размер торговой позиции в базовой валюте (BTC)
  risk: 0.02, // Уровень риска в процентах на одну сделку
  stopLoss: 0.01, // Уровень стоп-лосса в процентах
  takeProfit: 0.03, // Уровень тейк-профита в процентах
  exchangeId: 'binance', // Идентификатор биржи (Binance)
  apiKey: 'ВАШ_API_КЛЮЧ', // API-ключ для работы с биржей
  apiSecret: 'ВАШ_СЕКРЕТНЫЙ_КЛЮЧ', // Секретный API-ключ для работы с биржей
};

Далее мы настраиваем объект биржи с помощью библиотеки ccxt:

const exchange = new ccxt[config.exchangeId]({
  apiKey: config.apiKey,
  secret: config.apiSecret,
  enableRateLimit: true,
});

Обратите внимание, что здесь мы передали идентификатор биржи, ключ API и секретный ключ.

Теперь мы можем начать работу с биржей, получив все необходимые данные через API, используя определенные технические индикаторы, чтобы определить наилучшую стратегию для торговли.

Первый шаг - получить данные свечей с биржи:

const candles = await exchange.fetchOHLCV(config.symbol, config.interval);

Для использования технических индикаторов, таких как SMA (простое скользящее среднее значение) или RSI (индекс относительной силы), нам необходимо создать массив объектов цен, содержащих значения закрытия свечей:

const closes = candles.map((candle) => candle[4]); // Получить цены закрытия свечей

Затем мы можем использовать библиотеку TA-lib для создания индикаторов:


// Индикатор SMA
const sma = ta.SMA(closes, 10); // получить 10-и периодное скользящее среднее

// Индикатор RSI
const rsi = ta.RSI(closes, 14); // получить 14-дневный RSI

// Индикатор Bollinger Bands®
const bbands = ta.BBANDS(closes, 20, 2, 2); // получить боллинджеровские линии
const upperBand = bbands[0];
const middleBand = bbands[1];
const lowerBand = bbands[2];

тлично! Для начала нам потребуется установить необходимые библиотеки. Для этого используем pip:

python
!pip install python-binance pandas numpy

Затем мы определим несколько начальных параметров в коде:

python
import pandas as pd
import numpy as np
from binance.client import Client

# Определяем начальные параметры
symbol = 'BTCUSDT'  # торговая пара
testnet = True  # используем тестовую сеть

if testnet:
    client = Client('testnet-key', 'testnet-secret')
else:
    client = Client('api-key', 'api-secret')

Этот фрагмент кода объявляет торговую пару (symbol) и определяет, используется ли тестовая сеть (testnet), а затем проверяет, используется ли в настоящее время тестовая сеть. Если testnet == True, то используются учетные данные тестового аккаунта.

Затем мы можем получить исторические данные через API Binance:

python
# Получаем исторические данные
klines = client.futures_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1DAY)
data = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume',
                                     'close_time', 'quote_asset_volume', 'num_trades',
                                     'taker_buy_base', 'taker_buy_quote', 'ignore'])
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
data = data.set_index('timestamp')

Здесь мы используем client.futures_klines, чтобы получить исторические данные для указанной торговой пары и интервала (в данном случае - 1 день). Мы преобразуем данные в объект DataFrame с помощью pd.DataFrame и устанавливаем временную метку в качестве индекса с помощью data.set_index.

Далее в боте должны быть реализованы стратегии торговли на базе различных индикаторов. Для этого мы можем использовать библиотеку TA-Lib:

python
import talib

# Рассчитываем индикаторы
data['rsi'] = talib.RSI(data['close'], timeperiod=14)
data['macd'], _, _ = talib.MACD(data['close'], fastperiod=12, slowperiod=26, signalperiod=9)

data.dropna(inplace=True)

Здесь мы используем talib.RSI и talib.MACD для рассчета индикаторов относительной силы (RSI) и скользящей средней сепаратно (MACD). Мы удаляем строки, в которых присутствуют отсутствующие значения, с помощью data.dropna.

Теперь, когда у нас есть исторические данные и рассчитанные индикаторы, мы можем реализовать стратегии торговли. Для примера реализуем стратегию Big Three: это популярная стратегия, которая основывается на трех различных индикаторах:

python
# Реализация стратегии Big Three
data['ma20'] = data['close'].rolling(window=20).mean()
data['upper_band'], data['middle_band'], data['lower_band'] = talib.BBANDS(data['close'], timeperiod=20, nbdevup=2, nbdevdn=2)

data.dropna(inplace=True)

data['buy'] = ((data['close'] > data['upper_band']) & 
               (data['rsi'] < 30) & 
               (data['macd'] > 0) & 
               (data['close'] > data['ma20'])).astype(int)

data['sell'] = ((data['close'] < data['lower_band']) & 
                (data['rsi'] > 70) & 
                (data['macd'] < 0)).astype(int)

Здесь мы используем data['close
, чтобы получить список цен закрытия за определенный период времени. Затем мы используем модуль TA-Lib, чтобы вычислить значения наших индикаторов.


import talib

# Назначить первичные параметры.

amount_to_spend = 1000 # Количество денег, которые мы можем потратить на торговлю
price_of_crypto = 5000 # Цена криптовалюты в долларах
symbol = 'BTC' # Тикер криптовалюты на бирже
stop_loss_pct = 0.03 # Инструкция на продажу при определенном проценте потерь
take_profit_pct = 0.06 # Инструкция на продажу при определенном проценте прибыли
timeframe = '4h' # Временной интервал графика

# Запросить данные OHLCV.
data = get_data(symbol, timeframe)

# Получить последнюю цену закрытия.
last_price = data['close'].iloc[-1]

# Вычислить значения индикаторов на основе последних данных OHLCV.
rsi = talib.RSI(data['close'])
sma = talib.SMA(data['close'])

# Напечатать значения индикаторов на последнем баре.
print(f'RSI: {rsi[-1]}')
print(f'SMA: {sma[-1]}')

Это только начало кода, но это дает представление о том, как мы можем использовать API биржи и библиотеку TA-Lib для обработки данных и вычисления технических индикаторов.

Конечно, я продолжу. Давай начнем с кода для реализации MACD индикатора:

python
# Загрузка зависимостей
import pandas as pd
import talib

# Загрузка данных
data = pd.read_csv("btc.csv")

# Вычисление MACD
macd, signal, hist = talib.MACD(data['close'], fastperiod=12, slowperiod=26, signalperiod=9)

# Можно сохранить значения индикатора в файл
macd.to_csv("macd.csv")

# Или добавить их к существующим данным
data['macd'] = macd
data['signal'] = signal
data['hist'] = hist

Теперь, чтобы создать стратегию на базе MACD, нам нужно определить условия покупки и продажи, используя значения индикатора. Например, когда линия MACD пересекает сигнальную линию сверху вниз - это сигнал к продаже. И наоборот, когда MACD пересекает сигнальную линию снизу вверх - это сигнал к покупке.

Вот пример кода для реализации простой стратегии на базе MACD:

python
# Загрузка зависимостей и данных
import pandas as pd
import talib

data = pd.read_csv("btc.csv")

# Вычисление MACD
macd, signal, hist = talib.MACD(data['close'], fastperiod=12, slowperiod=26, signalperiod=9)

# Определение условий покупки и продажи
data['bought'] = ((macd > signal) & (macd.shift() < signal.shift()))
data['sold'] = ((macd < signal) & (macd.shift() > signal.shift()))

# Расчет позиции и пересчет баланса
data['position'] = data['bought'].apply(lambda x: 1 if x else 0) - data['sold'].apply(lambda x: 1 if x else 0)
data['balance'] = data['position'].shift() * data['close'].pct_change() + (1 - abs(data['position'].shift())) * 0.0005

# Рассчет кумулятивной доходности
data['cumulative_return'] = (1 + data['balance']).cumprod() * 100

# Вывод результата
print(data['cumulative_return'].iloc[-1])

В этом примере бот покупает биткоин, когда линия MACD пересекает сигнальную линию сверху вниз, и продает, когда они пересекаются снизу вверх. В боте также рассчитывается размер позиции и пересчитывается баланс на каждом шаге, а кумулятивная доходность показывает общий результат торговли. 

Этот код можно легко модифицировать, чтобы добавить другие индикаторы или различные стратегии.

Следующий шаг - это написание функции для каждой стратегии, которую мы собираемся использовать.

python
import ta
import numpy as np

def RSI_strategy(data):
    rsi = ta.momentum.RSIIndicator(data['close'], window=14)
    data['rsi'] = rsi.rsi()
    data['rsi_signal'] = np.where(data['rsi'] > 70, 1, 0)
    data['rsi_signal'] = np.where(data['rsi'] < 30, -1, data['rsi_signal'])
    return data['rsi_signal']


def BBANDS_strategy(data):
    upper, middle, lower = ta.volatility.bollinger_mavg(data['close'], window=20, std=2)
    data['upper'] = upper
    data['middle'] = middle
    data['lower'] = lower
    data['bbands_signal'] = np.where(data['close'] > upper, -1, 0)
    data['bbands_signal'] = np.where(data['close'] < lower, 1, data['bbands_signal'])
    return data['bbands_signal']


def MACD_strategy(data):
    macd = ta.trend.MACD(data['close'], window_slow=26, window_fast=12, window_sign=9)
    data['macd'] = macd.macd()
    data['signal'] = macd.macd_signal()
    data['hist'] = macd.macd_diff()
    data['macd_signal'] = np.where(data['macd'] > data['signal'], 1, 0)
    data['macd_signal'] = np.where(data['macd'] < data['signal'], -1, data['macd_signal'])
    return data['macd_signal']

Здесь мы пишем три функции: RSI_strategy, BBANDS_strategy и MACD_strategy. Каждая функция принимает данные и возвращает сигналы для покупки и продажи. Если значение равно 1, то это означает, что мы должны покупать, если -1, то продавать. Если значение равно 0, то никаких действий не требуется.

Давайте теперь напишем основную функцию, которая будет собирать все вместе:
python
def bot_trading(bot_data, strategy_func, base_order_size, stop_loss, take_profit):
    positions = []
    for i in range(len(bot_data)):
        signal = strategy_func(bot_data[:i+1])
        current_price = bot_data['close'][i]
        current_datetime = bot_data.index[i]
        if signal[-1] == 1:
            if len(positions) > 0 and positions[-1]['type'] == 'long':
                continue
            qty = int(base_order_size / current_price)
            positions.append({'type': 'long',
                              'qty': qty,
                              'entry_price': current_price,
                              'entry_time': current_datetime})
        elif signal[-1] == -1:
            if len(positions) > 0 and positions[-1]['type'] == 'short':
                continue
            qty = int(base_order_size / current_price)
            positions.append({'type': 'short',
                              'qty': qty,
                              'entry_price': current_price,
                              'entry_time': current_datetime})
        else:
            if len(positions) == 0:
                continue
            if positions[-1]['type'] == 'long':
                if current_price < positions[-1]['entry_price'] * (1 - stop_loss):
                    positions.pop()
                elif current_price > positions[-1]['entry_price'] * (1 + take_profit):
                    position = positions.pop()
                    total_pnl = (current_price - position['entry_price']) / position['

После расчета PNL бот должен принимать решение о том, нужно ли закрыть позицию.

Если текущая PNL достигла основной цели, то позиция будет закрыта. Если же цена уходит в минус, до уровня стоп-лосса, тогда позиция также будет закрыта. Если текущая цена находится между PNL и уровнем стоп-лосса, позиция будет закрыта при достижении уровня стоп-аута. 

Давайте добавим функцию, которая будет проверять эти условия и делать решения о закрытии позиций.

python
def close_position(current_price, position, stop_loss, take_profit):
    # Позиция в прибыли или убытке
    if position['pnl'] >= take_profit or position['pnl'] <= stop_loss:
        return True
    
    # Уровень Стоп-аут
    if position['pnl'] <= -stop_loss:
        return True
    
    return False

Вот как это будет выглядеть в полном коде:

python
import time
import pandas as pd
import talib.abstract as ta
import ccxt

exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
})

symbol = 'ETH/USDT'
interval = '1m'
stop_loss = 0.02
take_profit = 0.05
quantity = 0.01

while True:
    try:
        # Получаем последние свечи
        candles = exchange.fetch_ohlcv(symbol, interval)
    
        # Создаем pandas DataFrame из свечей
        df = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df = df.set_index('timestamp')
        
        # Вычисляем индикаторы
        ma = ta.SMA(df, timeperiod=20)
        std = ta.STDDEV(df, timeperiod=20)
        upper_bb = ma + 2 * std
        lower_bb = ma - 2 * std
        
        # Получаем текущую цену
        ticker = exchange.fetch_ticker(symbol)
        current_price = ticker['last']
        
        # Получаем текущую позицию
        positions = exchange.fetch_open_orders(symbol)
        
        # Если позиция отсутствует, то устанавливаем новый ордер
        if len(positions) == 0:
            if df['close'].iloc[-1] > upper_bb.iloc[-1]:
                order = exchange.create_order(
                    symbol=symbol,
                    type='limit',
                    side='buy',
                    amount=quantity,
                    price=current_price
                )
                positions.append({
                    'symbol': symbol,
                    'order_id': order['id'],
                    'entry_price': current_price,
                    'quantity': quantity
                })
            elif df['close'].iloc[-1] < lower_bb.iloc[-1]:
                order = exchange.create_order(
                    symbol=symbol,
                    type='limit',
                    side='sell',
                    amount=quantity,
                    price=current_price
                )
                positions.append({
                    'symbol': symbol,
                    'order_id': order['id'],
                    'entry_price': current_price,
                    'quantity': quantity
                })
        else:
            position

Конечная функция должна содержать основной цикл, который будет запрашивать цены и определять, следует ли совершать сделку или нет. Также функция должна учитывать баланс, риск и размер позиции.

Вот пример кода, который может смоделировать это поведение:

python
import ccxt
import talib
import time

# параметры
symbol = 'ETH/BTC'
timeframe = '1m'
rsi_period = 14
rsi_upper = 70
rsi_lower = 30
risk = 0.01
position_size = 0.1

# создание объекта биржи
exchange = ccxt.binance({
    'apiKey': 'your_api_key',
    'secret': 'your_api_secret',
    'enableRateLimit': True,
})

# получаем баланс
def get_balance():
    balance = exchange.fetch_balance()
    return balance['total']['BTC']

# получаем цены
def get_current_price():
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

# делаем сделку
def enter_position(direction):
    price = get_current_price()
    amount = (risk * get_balance()) / abs(price - stop_loss)
    amount = min(amount, position_size)
    if direction == 'buy':
        order = exchange.create_order(symbol, type='limit', side='buy', amount=amount, price=price)
    else:
        order = exchange.create_order(symbol, type='limit', side='sell', amount=amount, price=price)
    return order['id'], price, amount

# закрываем сделку
def exit_position(id, entry_price, direction):
    price = get_current_price()
    pnl = (price - entry_price) / entry_price
    amount = (risk * get_balance()) / abs(price - entry_price)
    amount = min(amount, position_size)
    if direction == 'buy':
        order = exchange.create_order(symbol, type='limit', side='sell', amount=amount, price=price)
    else:
        order = exchange.create_order(symbol, type='limit', side='buy', amount=amount, price=price)
    return pnl * amount

# основной цикл
positions = []
while True:
    # получаем rsi
    candles = exchange.fetch_ohlcv(symbol, timeframe)
    close_prices = [candle[4] for candle in candles]
    rsi = talib.RSI(close_prices, timeperiod=rsi_period)[-1]

    # определяем направление сигнала
    if rsi > rsi_upper:
        signal = 'oversold'
    elif rsi < rsi_lower:
        signal = 'overbought'
    else:
        signal = 'none'

    # получаем текущую позицию
    if len(positions) > 0:
        position = positions[-1]
        stop_loss = position['entry_price'] * (1 - risk)
        if signal == 'overbought':
            pnl = exit_position(position['id'], position['entry_price'], 'buy')
            positions.pop()
            print(f'Exited long position with PNL of {pnl:.2%}')
        elif signal == 'oversold':
            pass
        else:
            if stop_loss > get_current_price() or stop_loss < position['entry_price']:
                pnl = exit_position(position['id'], position['entry_price'], 'buy')
                positions.pop()
                print(f'Stopped out of long position.')
    else:
        if signal ==
Понятно. Продолжим. Добавим обработку ошибок иструктуру ордеров:

python
import ccxt
import time

# настройки
symbol = 'BTC/USDT'
strategy = 'bb_macd'  # стратегия торговли, пока не реализованы другие

# инициализация API
exchange = ccxt.binance({
    'enableRateLimit': True,  # опция для задержек между вызовами API
})

# инициализация баланса
print('Fetching balance...')
balance = exchange.fetch_balance()  # баланс всех активов на бирже
BTC_balance = balance['BTC']['free']  # количество свободных BTC
USDT_balance = balance['USDT']['free']  # количество свободных USDT

# инициализация стратегии
if strategy == 'bb_macd':
    uppper_k = 2
    lower_k = 2
    period = 20
    close_position_rsi = 45
    close_position_macd = -0.0002

    while True:
        try:
            # получаем данные об активе
            ticker = exchange.fetch_ticker(symbol)
            current_price = ticker['close']  # текущая цена
            prices = exchange.fetch_ohlcv(symbol, '1h')[-period:]
            closes = [price[4] for price in prices]

            # рассчитываем индикаторы
            bb_upper, bb_middle, bb_lower = talib.BBANDS(
                np.array(closes),
                timeperiod=period,
                nbdevup=uppper_k,
                nbdevdn=lower_k,
                matype=talib.MA_Type.SMA
            )

            macd, macd_signal, macd_hist = talib.MACD(
                np.array(closes),
                fastperiod=12,
                slowperiod=26,
                signalperiod=9
            )

            slowk, slowd = talib.STOCHRSI(
                np.array(closes),
                timeperiod=14,
                fastk_period=5,
                fastd_period=3,
                fastd_matype=talib.MA_Type.SMA
            )

            rsi = talib.RSI(np.array(closes), timeperiod=14)

            if np.isnan(bb_lower[-1]) or np.isnan(macd_hist[-1]):
                raise Exception('NaN found while calculating indicators')

            # проверяем условия для открытия позиции
            condition_long_bb = current_price <= bb_lower[-1] and rsi[-1] < close_position_rsi
            condition_long_macd = macd_hist[-1] > 0 and macd_hist[-2] < 0 and macd_hist[-1] > macd_hist[-2] and rsi[-1] < close_position_rsi
            condition_close_bb = current_price >= bb_middle[-1]
            condition_close_macd = macd_hist[-1] < 0 and macd_hist[-2] > 0 and macd_hist[-1] < macd_hist[-2]

            # открытие позиции
            positions = exchange.fetch_open_orders(symbol)
            if not positions:
                if condition_long_bb or condition_long_macd:
                    amount = (USDT_balance * 
# Рассчитываем текущую прибыль или убыток
current_pnl = (current_price - entry_price) * quantity

# Рассчитываем средний процент прибыли на каждой успешной сделке
average_win_percentage = (total_wins / win_count) if win_count > 0 else None

# Рассчитываем коэффициент Шарпа для текущей позиции
sharp_ratio = (average_win_percentage - average_loss_percentage) / stdev if stdev > 0 else None

# Выводим информацию о текущей позиции
print(f" Текущая позиция:")
print(f" Вход по цене: {entry_price}")
print(f" Количество: {quantity}")
print(f" Прибыль / убыток: {current_pnl:.2f}")
print(f" Средний % выигрыша: {average_win_percentage:.2f}")
print(f" Средний % проигрыша: {average_loss_percentage:.2f}")
print(f" Коэффициент Шарпа: {sharp_ratio:.2f}")

Когда мы открываем позицию, мы сохраняем ее в стеке positions. Когда мы закрываем позицию, мы извлекаем ее из стека, рассчитываем прибыль или убыток и выводим информацию на экран.

Следующим шагом будет добавление торговой логики и подключение к API биржи для автоматической торговли.

Для реализации стратегии покупки на дипах нужно сначала определить, что считать "дипом". Например, мы можем считать, что дипом является падение цены на 3% за последние 3 свечи. Тогда можно использовать следующий код:


last_n_candles = get_last_n_candles(3) # получаем последние 3 свечи
current_price = get_current_price() # получаем текущую цену

# считаем минимальную цену за последние 3 свечи
min_price = min(candle['low'] for candle in last_n_candles)

if current_price < 0.97 * min_price: # если цена упала на 3% ниже минимальной цены
    quantity = calculate_order_quantity() # рассчитываем размер торговой позиции
    order = create_limit_buy_order(quantity, current_price) # создаем ордер на покупку по лимитной цене
    execute_order(order) # исполняем ордер

В данном примере мы получаем последние три свечи с помощью функции get_last_n_candles(), определяем текущую цену и минимальную цену за последние три свечи, считаем, что дипом является падение цены на 3% ниже минимальной цены, и если цена упадет ниже этого уровня, создаем ордер на покупку по лимитной цене. 

Также можно реализовать стратегию покупки на дипах с использованием индикатора RSI (Relative Strength Index), считающего отношение средней прибыли к среднему убытку за определенный период. Когда RSI падает ниже порогового значения (например, 30), соответствующего перепроданности актива, это может сигнализировать о том, что цена скоро снизится. В этом случае создается ордер на покупку при следующем дипе.

Для реализации стратегии скользящего среднего можно использовать функцию talib.SMA() из библиотеки TA-Lib. Например:


closes = get_closes() # получаем цены закрытия за последние несколько дней

Опишу следующий код, который поможет получить данные о торгах с биржи Бинанс. Он использует ccxt и pandas библиотеки:


import ccxt
import pandas as pd

exchange = ccxt.binance()
symbol = 'BTC/USDT'

bars = exchange.fetch_ohlcv(symbol, '1d')
df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)

Этот код получит линейный OHLCV-данные (цена открытия, цена закрытия, наивысшая и наименьшая цена, объем торгов) за последние 24 часа для пары BTC/USDT. После чего сохраним их в объекте DataFrame из библиотеки pandas. 

Давайте теперь рассмотрим, как определять размер торговой позиции в зависимости от уровня риска. Для этого мы можем использовать метод оптимизации капитала, который будет устанавливать размер торговой позиции в зависимости от риска. 

Для этого мы можем использовать следующие параметры:

- Размер портфеля (portfolio_size)
- Риск на сделку в процентах от размера портфеля (risk_per_trade)
- Размер стоп-лосса в процентах от текущей цены (stop_loss_pct)

С помощью этих параметров мы можем определить размер торговой позиции следующим образом:

position_size = (portfolio_size * risk_per_trade) / stop_loss_pct

Для примера, предположим, что у нас есть портфель стоимостью $10000, мы готовы рисковать 2% от размера портфеля на каждую сделку и мы хотим установить стоп-лосс в 5% от текущей цены.

В этом случае мы можем определить размер торговой позиции следующим образом:

position_size = (10000 * 0.02) / 0.05
position_size = 400

Таким образом, мы можем рассчитать размер торговой позиции для каждой сделки, основываясь на параметрах риска и размера портфеля, и устанавливать стоп-лосс в соответствии с текущей ценой.

Следующий шаг - определить, каким образом мы будем использовать размер торговой позиции, основываясь на наших торговых стратегиях. Это может быть сочетание различных методов оптимизации капитала, таких как метод Фиксированного Риска (Fixed Risk), метод Константного Риска (Constant Risk) и метод Мартигейла (Martingale). 

Мы можем также определить параметры уровня принятия риска и размера торговой позиции для каждой торговой стратегии, основываясь на исторических данных о производительности каждой из стратегий. 

В следующем сообщении я напишу пример кода, который позволяет определять размер торгов

Хорошо, ниже я продолжу код для бота. Для следующего шага используем переменную risk, которую получили на предыдущем шаге: 

python
# определение размера позиции
if risk == 0:
    position_size = 0
else:
    position_size = max(int(total_portfolio_value * risk / abs(stop_loss_pct)), 1)

# проверка доступного количества активов для торговли
available_qty = exchange.fetch_balance()['total'][base_asset]
max_qty = int(total_portfolio_value / current_price)
qty = min(position_size, available_qty, max_qty)

# создание ордера на покупку
if trading_signal == 'buy':
    order = exchange.create_order(symbol=symbol, type='market', side='buy', amount=qty)
    positions.append({'entry_price': current_price, 'qty': qty, 'stop_loss': current_price * (1 - abs(stop_loss_pct)), 'side': 'long'})

# создание ордера на продажу
elif trading_signal == 'sell':
    position = positions.pop()
    qty = position['qty']
    order = exchange.create_order(symbol=symbol, type='market', side='sell', amount=qty)
    entry_price = position['entry_price']
    if qty > 0:
      pnl = ((current_price - entry_price) / entry_price) * qty
    else:
      pnl = 0
    total_pnl += pnl

Здесь мы определяем размер позиции на основе размера риска и оборотных средств на счете. Затем мы проверяем доступное количество криптовалюты для торговли и устанавливаем фактический размер позиции, который может быть меньше размера позиции, определенной на основе размера риска. Если торговый сигнал - "buy", мы создаем ордер на покупку, если же сигнал - "sell", мы продаем позицию и вычисляем прибыль-убыток за сделку, добавляя его к общей прибыли-убытку. 

Надеюсь, этот код поможет вам лучше понять логику работы торгового бота. Давайте продолжим и дополним его функциональность расчетом статистики торговли.

Следующим шагом может быть добавление индикаторов, основанных на методах анализа технических данных. Для этого мы можем использовать библиотеку TA-Lib. Вот несколько примеров, как это может быть реализовано:


import talib

# Определение значений индикаторов
rsi = talib.RSI(data['close'])
sma = talib.SMA(data['close'])
ema = talib.EMA(data['close'])

Теперь мы можем использовать эти значения для настройки торговых стратегий. Например:


# Реализация стратегии на основе RSI
if rsi > 70:
    bot.sell()
elif rsi < 30:
    bot.buy()

# Реализация стратегии на основе скользящих средних
if sma[-1] > sma[-2]:
    bot.buy()
elif sma[-1] < sma[-2]:
    bot.sell()

Мы можем добавить больше индикаторов и использовать их для более точного анализа данных, а также для разработки дополнительных стратегий.

Следующим шагом может быть добавление методов управления капиталом, таких как метод Келли, которые помогут эффективно выстраивать стратегию управления капиталом, определять оптимальную долю портфеля под рискованные активы, снижать риски, и многих других. Код для реализации метода Келли может выглядеть следующим образом:


# Определение коэффициента Келли
kelly = (p * b - q) / b
# Определение размера торговой позиции на основе коэффициента Келли
position_size = account_balance * kelly

Наконец стоит упомянуть, что для избежания проблем с безопасностью стоит рассмотреть все возможные аспекты информационной безопасности. Например, использовать двухфакторную аутентификацию, защищать ключи доступа к API, использовать SSL-соединение для об

Первым шагом я бы порекомендовал создать основной класс для бота. Он будет иметь свойства и методы, который позволят управлять ботом через API биржи. Вот как мог бы выглядеть простой код для этого класса на Python:


class TradingBot:
    
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        
        self.exchange = ccxt.binance({
            'apiKey': self.api_key,
            'secret': self.secret_key,
        })

    def get_balance(self, symbol):
        balance = self.exchange.fetch_balance()
        free_balance = balance[symbol]['free']
        
        return free_balance

    def make_trade(self, symbol, side, amount, price):
        trade = self.exchange.create_order(symbol, type='limit', side=side, amount=amount, price=price)
        
        return trade

 Этот класс принимает ключ API и секретный ключ для доступа к бирже. Он также имеет два метода, которые позволяют получать баланс и создавать торговые ордера.

Теперь, когда у вас есть основной класс, вы можете начать создавать различные стратегии торговли. Вы можете создать отдельный класс для каждой стратегии и добавить их в основной класс. Вот пример кода для класса стратегии, который базируется на индикаторе Bollinger Bands:


class BollingerBandsStrategy:
    
    def __init__(self, trading_bot):
        self.trading_bot = trading_bot
        self.exchange = trading_bot.exchange
        self.symbol = 'BTC/USDT'
        
    def get_signal(self):
        data = self.exchange.fetch_ohlcv(self.symbol, '1d')
        data = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
        data = data.set_index('timestamp')
        period = 20
        data['upper'], data['middle'], data['lower'] = talib.BBANDS(data['close'], timeperiod=period)
        data['close_minus_lower'] = data['close'] - data['lower']
        data['upper_minus_lower'] = data['upper'] - data['lower']
        data['percent_b'] = data['close_minus_lower'] / data['upper_minus_lower']
        current_price = self.exchange.fetch_ticker(self.symbol)['bid']
        last_close = data['close'].iloc[-1]
        last_percent_b = data['percent_b'].iloc[-1]
        historical_prices = data['close'].iloc[:-1]
        historical_percent_b = data['percent_b'].iloc[:-1]
        buy_signal = last_percent_b < 0.2
        sell_signal = last_percent_b > 0.7

        if buy_signal:
            return Signal(
                signal=Signal.SIGNAL_BUY,
                symbol=self.symbol,
                exchange=self.exchange.id,
                price=current_price
            )
        elif sell_signal:
            return Signal(
                signal=Signal.SIGNAL_SELL,
                symbol=self.symbol,
                exchange=self.exchange.id,
                price=current_price
            )
        else:
            return Signal(
                signal=Signal.SIGNAL_WAIT,
                symbol=self.symbol,
                exchange=self.exchange.id,
                price=current_price
            )

Тут мы определяем класс BollingerBandsStrategy с конструктором __init__, который принимает нашего бота для торговли. Внутри этого класса определена функция get_signal, которая возвращает объект Signal. 

В начале данной функции мы используем метод fetch_ohlcv для загрузки исторических цен на бирже за последние 24 часа и конвертируем его в pandas dataframe. Затем мы применяем к нему BBANDS индикатор библиотеки TA-Lib,

Продолжаю:

python
class BollingerBandsStrategy:
    
    def __init__(self, trading_bot):
        self.trading_bot = trading_bot
        self.exchange = trading_bot.exchange
        self.symbol = 'BTC/USDT'
        
    def get_signal(self):
        data = self.exchange.fetch_ohlcv(self.symbol, '1d')
        data = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
        data = data.set_index('timestamp')
        period = 14
        std_multiplier = 2
        data['smavg'] = data['close'].rolling(window=period).mean()
        data['std'] = data['close'].rolling(window=period).std()
        data['upper_band'] = data['smavg'] + (data['std'] * std_multiplier)
        data['lower_band'] = data['smavg'] - (data['std'] * std_multiplier)
        last_close = data['close'].iloc[-1]
        last_lower = data['lower_band'].iloc[-1]
        last_upper = data['upper_band'].iloc[-1]
        position_size = 1  # количество криптовалюты для покупки/продажи
        if last_close > last_upper:
            return Signal(price=last_close, side='sell', size=position_size)
        elif last_close < last_lower:
            return Signal(price=last_close, side='buy', size=position_size)
        return None
 

Код выше демонстрирует реализацию BollingerBandsStrategy. Эта стратегия основывается на индикаторе Bollinger Bands. Она загружает исторические данные ц
И работает с ними, добавляя к таблице столбцы, содержащие значения для каждого показателя. Например, методы для вычисления скользящих средних через библиотеку Pandas:

    data['20sma'] = data['close'].rolling(window=20).mean()
    data['2std'] = data['close'].rolling(window=20).std()
    data['lower_band'] = data['20sma'] - (2 * data['2std'])
    data['upper_band'] = data['20sma'] + (2 * data['2std'])
    
Здесь мы используем метод rolling() для вычисления скользящего среднего и стандартного отклонения для цен закрытия. Затем мы вычисляем верхние и нижние линии Bollinger, добавляя их к таблице данных.

Для того чтобы определить направление тренда и принять более успшные торговые решения, боту необходимо следить за значениями цены закрытия, сравнивая их с верхней и нижней линией Боллинджера. В случае если цена закрытия выше верхней границы, можно предположить, что рынок перекуплен и скоро наступ
Вот пример кода функции, которая загружает исторические данные цены закрытия актива и вычисляет средние значения и стандартное отклонение для получения значений Bollinger Bands:

python
import pandas as pd
import talib

def bollinger_bands(df, n=20, dev=2):
    df['MA'] = talib.SMA(df['close'], n)
    df['SD'] = talib.STDDEV(df['close'], n)
    df['upper'] = df['MA'] + (dev * df['SD'])
    df['lower'] = df['MA'] - (dev * df['SD'])
    return df

Здесь мы используем библиотеку TA-Lib для вычисления скользящего среднего и стандартного отклонения цен закрытия. Затем мы вычисляем значения верхней и нижней границы для нашей стратегии Bollinger Bands. 

Кроме того, мы можем использовать эти данные для генерации сигналов покупки и продажи. 

од для загрузки данных выглядит так:

python
data = self.exchange.fetch_ohlcv(self.symbol, '1d')
data = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

Здесь мы используем метод fetch_ohlcv, чтобы получить свечи для конкретной валютной пары и временного интервала. Мы преобразуем полученные данные в DataFrame Pandas и приводим тип данных столбца timestamp из миллисекунд к дате и времени соответственно.

Далее мы можем использовать BollingerBands из библиотеки TA-Lib для вычисления верхней и нижней полосы Боллинджера, а также средней полосы:

python
upper_band, middle_band, lower_band = talib.BBANDS(data['close'], timeperiod=20, nbdevup=2, nbdevdn=2

Дальше можно использовать эти значения, чтобы определить точки входа и выхода из позиций, основываясь на торговых сигналах. Например, если цена становится больше или равна верхней полосе Боллинджера, то возможен сигнал на продажу. Если цена становится меньше или равна нижней полосе Боллинджера, возможен сигнал на покупку. 

Вот как это может выглядеть в виде кода:


class BollingerBandsStrategy:
    
    def __init__(self, trading_bot):
        self.trading_bot = trading_bot
        self.exchange = trading_bot.exchange
        self.symbol = 'BTC/USDT'
        
    def get_signal(self):
        data = self.exchange.fetch_ohlcv(self.symbol, '1d')
        data = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
        upper_band, middle_band
        
        от продолжение кода:

python
        if current_price > upper_band:
            return 'sell'
        elif current_price < lower_band:
            return 'buy'
        else:
            return 'hold'

Этот метод просто возвращает торговый сигнал на основе текущего ценового положения по отношению к полосам Боллинджера.
Итак, мы определили класс BollingerBandsStrategy и реализовали в нем метод get_signal, который генерирует сигналы на основе индикатора Bollinger Bands.

Дальше нам нужно добавить эту стратегию в бот и запустить его на торги:

python
import time

# Создаем торгового бота
trading_bot = TradingBot()

# Д

Пример кода для обращения к API биржи Coinbase:
python
import os
import cbpro

api_key = os.environ.get("COINBASE_API_KEY")
api_secret = os.environ.get("COINBASE_API_SECRET")
api_pass = os.environ.get("COINBASE_API_PASS")
client = cbpro.AuthenticatedClient(api_key, api_secret, api_pass)

# получаем баланс криптовалют и доступных средств в торговой сессии
balance = client.get_accounts()
print(balance)

Однако, помимо управления ботом через личный кабинет на бирже, для полного контроля и управления нашим ботом, нам нужно создать свой собственный пользовательский интерфейс. Для этого мы можем использовать фреймворк Flask, который позволит нам быстро создавать веб-страницы и контроллеры для нашего бота.

Пример кода для создания веб-страницы с помощью Flask:
python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True)

Также для защиты нашего бота от взломов, нам нужно будет использовать дополнительные меры безопасности, такие как двухфакторная аутентификация, и хранить нашу криптовалюту в холодном хранилище. Например, мы можем использовать библиотеку PyOTP для реализации двухфакторной аутентификации, и холодное хранилище Ledger Nano S для хранения наших криптовалют.

Пример кода использующего технический анализ графиков для определения времени покупки и продажи Bitcoin:


import ccxt
import talib
import numpy as np

# оставляем только данные за прошедшие N дней
N = 30
exchange = ccxt.binance()
market = exchange.load_market("BTC/USDT")
ohlcv = exchange.fetch_ohlcv(market['id'], '1d')
ohlcv = [x[:6] for x in ohlcv[-N:]]

# преобразуем данные в формат numpy
np_ohlcv = np.array(ohlcv)
np_ohlcv = np_ohlcv.astype(float)

# определяем индикаторы
SMA = talib.SMA(np_ohlcv[:,4], timeperiod=20)
RSI = talib.RSI(np_ohlcv[:,4], timeperiod=14)

# находим последнее значение индикаторов
last_SMA = SMA[-1]
last_RSI = RSI[-1]

# определяем, покупать или продавать
if last_RSI > 70:
    order = exchange.create_market_sell_order(market['id'], 0.01)
elif last_RSI < 30:
    order = exchange.create_market_buy_order(market['id'], 0.01)
Хорошо, начнем с файла requirements.txt:


requests==2.22.0
python-binance==0.7.9

Это список зависимостей, необходимых для запуска нашего бота. В данном случае у нас есть две зависимости: requests и python-binance.

Переходим к файлу api.py:

python
import os
from binance.client import Client

class BinanceAPI:
    def __init__(self):
        self.api_key = os.environ.get("BINANCE_API_KEY")
        self.api_secret = os.environ.get("BINANCE_API_SECRET")
        self.client = Client(self.api_key, self.api_secret)

    def get_account_balance(self):
        account = self.client.get_account()
        return float(account['balances'][0]['free'])

Здесь мы определяем класс BinanceAPI для взаимодействия с API биржи Binance. Мы используем ключ и секрет, который находится в переменных среды. Одна из функций класса - это get_account_balance, который возвращает доступный баланс нашего аккаунта.

Переходим к файлу bot.py:

python
from api import BinanceAPI
import time

class TradingBot:
    def __init__(self):
        self.api = BinanceAPI()

    def run(self):
        while True:
            balance = self.api.get_account_balance()
            print("Balance: {0:.2f}".format(balance))
            # Здесь будет код реализации стратегии торговли.


            time.sleep(5)

В файле bot.py мы создаем класс TradingBot, который использует класс BinanceAPI для получения информации о балансе аккаунта и для других операций, связанных с торговлей. Мы также запускаем бесконечный цикл, который будет выполняться постоянно, пока мы не остановим наш бот. В задержках между итерациями цикла - 5 секунд.

Это только начало работы с ботом, но мы сможем добавлять функциональность в наше решение с помощью этих базовых элементов.
> ChatGPT | Марти 🦓:
ChatGPT (беседа № 6):
Выбрана Ваша тестовая роль

Продолжим.

Вот часть кода из файла bot.py:

python
from binance.enums import *
from binance.client import Client
import talib.abstract as ta
from uuid import uuid4
import sys
import threading, queue
from datetime import datetime, timedelta
import json
import os.path
import pandas as pd
import time

from api import BinanceAPI

# global variables
q = queue.Queue()
access_token = '_your_api_token'
secret_token = '_your_secret_token'
candles = []
lock = threading.Lock()
user_candles = {}


Это начало файла "bot.py", мы импортируем модули, которые нам необходимы, описываем глобальные переменные и создаем экземпляр класса BinanceAPI из другого файла "api.py", который мы подключили.

Следующий кусок из этого же файла:

python
class StrategyTester:

    def __init__(self, symbol, start_date, end_date, klines_date_format):
        # Function that iterates over all candles
        self.run = self.backTest

        # Candles data
        self.candles = []

        self.client = Client(access_token, secret_token)
        self.symbol = symbol
        self.klines_date_format = klines_date_format

        self.start_date = start_date
        self.end_date = end_date
        self.interval = KLINE_INTERVAL_1MINUTE

        self.KDJDayPeriod = 9
        self.KDJFastKPeriod = 3
        self.KDJSlowKPeriod = 3
        self.KDJSlowDPeriod = 3

        self.loopSleep = 5
        
        self.readCandles()

    #--------------------------------------------------------------------------------
    # readCandles()
    #
    # log in to binance and read k lines since start_date until end_date (in minutes interval)
    # load candles from binance and append to self.candles filtered to only symbol we are
    # testing with
    #--------------------------------------------------------------------------------
    def readCandles(self):
        # Download all binance candles
        all_klines = self.client.get_historical_klines(self.symbol, self.interval, self.start_date,
                                                        self.end_date, limit=1000)
        klines = [x for x in all_klines if x[0] > 0]

        # Filter candles to only our symbol
        filtered_klines = list(filter(lambda x: x[0] != None and
                                            x[1] != None and
                                            x[2] != None and
                                            x[3] != None and
                                            x[4] != None and
                                            x[5] != None and
                                            x[6] != None and
                                            x[7] == self.symbol and
                                            int(x[0]) >= int(time.mktime(self.start_date.timetuple())*1000) and
                                            int(x[0]) <= int(time.mktime(self.end_date.timetuple())*1000),
                                      klines))
        # Build candles array
        for kline in filtered_klines:
            self.candles.append({
                'open_time': kline[0],
                'open': kline[1],
                'high': kline[2],
                'low': kline[3],
                'close': kline[4],
                'volume': kline[5],
                'close_time': kline[6],
                'symbol': kline[7],
                'quote_asset_volume': kline[8],
                'number_of_trades': kline[9],
                'taker_buy_base_av': kline[10],
                'taker_buy_quote_av': kline[11],

> ChatGPT | Марти 🦓:
                'ignore': kline[12]
            })


Здесь мы описываем класс StrategyTester. Он представляет собой инструмент для тестирования стратегии на исторических данных биржи Binance. Мы инициализируем его и определяем метод readCandles, который скачивает исторические данные за период с start_date по end_date. Далее мы фильтруем данные и сохраняем их в виде свечей (объектов со свойствами "открытие цены", "максимальная цена", "минимальная цена", "цена закрытия", "объем торгов" и т.д.). Мы должны использовать эти данные для определения стратегии торговли.

Теперь я продемонстрирую часть из файла "api.py":

python
# binance API URL
BASE_URL = 'https://api.binance.com'
API_URL = BASE_URL + '/api'
API_WEBSOCKET_URL = 'wss://stream.binance.com:9443/'

class BinanceAPI:

    def __init__(self, access_token = None, secret_token = None):
        self._access_token = access_token
        self._secret_token = secret_token
        self._nonce = str(uuid4())
        self._headers = {}
        
        if access_token and secret_token:
            self._headers = {
                'X-MBX-APIKEY': access_token
            }

    #--------------------------------------------------------------------------------
    # getSymbols()
    #
    # Get all available symbols
    #--------------------------------------------------------------------------------
    def getSymbols(self):
        url = '%s/v1/exchangeInfo' % API_URL
        response = requests.get(url)
        content = response.content.decode('utf-8')
        data = json.loads(content)
        return data['symbols']

    #--------------------------------------------------------------------------------
    # getPrice(symbol)
    #
    # Get symbol price
    #--------------------------------------------------------------------------------
    def getPrice(self, symbol):
        url = '%s/v3/ticker/price' % API_URL
        response = requests.get(url + '?symbol=' + symbol)
        content = response.content.decode('utf-8')
        data = json.loads(content)
        return float(data['price'])


Здесь мы определяем класс BinanceAPI, который представляет собой интерфейс для взаимодействия с биржей Binance через их API. Он имеет несколько методов, например метод getPrice, который возвращает текущую цену заданного наименования валютной пары.

Для начала работы с API биржи Binance или Coinbase нам нужно зарегистрироваться на сайте биржи и получить свой API-ключ. Затем создадим файл api.py, который будет содержать классы для работы с API биржи. Вот как может выглядеть начало этого файла:


import requests
import json

class BinanceAPI:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.binance.com"
        self.headers = {"X-MBX-APIKEY": self.api_key}

    def get_timestamp(self):
        response = requests.get(self.base_url + "/api/v3/time")
        response_json = json.loads(response.text)
        return response_json["serverTime"]

В этом коде мы создаем класс BinanceAPI и определяем метод get_timestamp(), который возвращает время на сервере биржи в миллисекундах. Также мы создаем свойства объекта для API-ключа, секретного ключа и базового URL API.

Теперь давайте реализуем наш бот. Для этого мы создадим файл bot.py, который будет содержать класс для нашего бота. Вот как может выглядеть начало этого файла:


import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ta
from api import BinanceAPI

class TradingBot:
    def __init__(self, api_key, api_secret):
        self.api = BinanceAPI(api_key, api_secret)
        self.trade_symbol = "BTCUSDT"
        self.trade_info = {"symbol": self.trade_symbol, "side": "", "type": "", "quantity": "", "price": "", "stopPrice": "", "workingType": "", "timestamp": ""}
        self.trade_signals = {"RSI_OVERBOUGHT": False, "RSI_OVERSOLD": False, "GOLDEN_CROSS": False, "DEATH_CROSS": False}
        self.balance = self.get_balance()
        self.trade_history = self.get_trade_history()
        self.candlesticks = self.get_candlesticks()

    def get_balance(self):
        """
        Получение баланса пользователя
        """
        response = self.api.get_signed("/api/v3/account")
        return response["balances"]

Здесь мы создаем класс TradingBot и определяем метод get_balance(), который получает баланс пользователя на бирже.

Также мы создаем свойства объекта для API-объекта, символа торговли, информации о сделках, торговых сигналов, баланса, истории сделок и свечных графиков.

Для работы с графиком мы можем использовать библиотеку matplotlib, а для технического анализа - ta (Technical Analysis Library). Чтобы использовать эти библиотеки, в файле requirements.txt должны быть следующие строки:


matplotlib
ta
> ChatGPT | Марти 🦓:
ChatGPT (беседа № 6):
Выбрана Ваша тестовая роль

Хорошо, давай начнем с файла requirements.txt. Этот файл содержит список всех зависимостей, использованных в проекте. Вот его содержание:


ccxt==1.54.60
numpy==1.20.3
pandas==1.3.2
python-binance==1.0.12


По смыслу, мы используем библиотеку CCXT для взаимодействия с биржей, библиотеку NumPy для математических операций, библиотеку Pandas для анализа и обработки данных, а также клиент для биржи Binance - python-binance.

Проверим установленные зависимости. Что бы не перечислять каждый файл по очереди, воспользуемся командой pip freeze:


pip freeze > requirements.txt


Теперь, если другие разработчики хотят запустить ваш код, им нужно всего лишь выполнить:


pip install -r requirements.txt


Чтобы установить все зависимости, описанные в файле requirements.txt.

Далее перейдем к файлу api.py, который содержит код для подключения к API биржи и получения данных. Вот его содержимое:

python
import ccxt

class BinanceAPI:
    def __init__(self, api_key, secret_key):
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret_key,
            'enableRateLimit': True,
        })

    def get_klines(self, symbol, interval):
        return self.exchange.fetch_ohlcv(symbol, interval)


Этот код создает класс BinanceAPI, который используется для подключения к API биржи Binance и получения данных о ценах. 
Мы используем CCXT библиотеку, чтобы создать экземпляр объекта биржи.Здесь мы передаем ключ API и секретный ключ в конструктор класса.
Затем у нас есть метод get_klines, который получает данные свечных графиков (или candlesticks) для заданного символа и интервала времени. Также мы используем метод fetch_ohlcv из CCXT, чтобы получить нужные данные.

Теперь перейдем к файлу bot.py, который содержит код для торговли криптовалютой. Этот файл делает больше всего и содержит класс TradingBot - наш автоматический торговый бот. Вот его содержимое:

python
import time
import numpy as np
import pandas as pd
from api import BinanceAPI
from indicators import RSI


class TradingBot:
    def __init__(self, api_key, secret_key, symbol, interval):
        self.api = BinanceAPI(api_key, secret_key)
        self.symbol = symbol
        self.interval = interval
        self.position = None

    def is_position_open(self):
        return self.position is not None

    def execute_trade(self, buy_sell, quantity):
        try:
            order = self.api.exchange.create_order(
                symbol=self.symbol,
                type='MARKET',
                side=buy_sell.upper(),
                amount=quantity
            )
            print(order)
        except Exception as e:
            print(f"Error executing {buy_sell} trade: {e}")

    def entry_rules(self, df):
        # добваьььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььььь
        # тут должны быть правила входа в позицию
        # в этом примере мы просто будем покупать, если RSI меньше 30.
        # добавьте свою логику здесь, если вы хотите использовать более продвинутые правила.
        # возвращает True, если сигнал на вход
        # или False, если позиция уже открыта или сигнала нет
        # добавление индикаторов из файла indicators.py, в данном примере используется RSI
        if self.is_position_open():
            return False
            
        if RSI(df['Close'].values, 14)[-1] < 30:

> ChatGPT | Марти 🦓:
            return True

        return False

    def exit_rules(self, df):
        # тут должны быть правила выхода из позиции
        # в этом примере мы просто будем продавать, если RSI больше 70.
        # добавьте свою логику здесь, если вы хотите использовать более продвинутые правила.
        # возвращает True, если сигнал на выход
        # или False, если позиция уже закрыта или сигнала нет
        # Проверка на закрытость позиции
        if not self.is_position_open():
            return False
        # В этом примере использован RSI
        if RSI(df['Close'].values, 14)[-1] > 70:
            return True

        return False

    def get_candles(self):
        klines = self.api.get_klines(self.symbol, self.interval)

        df = pd.DataFrame(klines, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'volume', 'timestamp2', 'Close_time',
                                           'Quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])

        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        df.set_index('timestamp', inplace=True)

        df.drop(['timestamp2', 'Close_time', 'volume', 'Quote_asset_volume', 'number_of_trades',
                 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'], axis=1, inplace=True)

        df['Open'] = df['Open'].astype(float)
        df['High'] = df['High'].astype(float)
        df['Low'] = df['Low'].astype(float)
        df['Close'] = df['Close'].astype(float)

        return df

    def run(self):
        while True:
            df = self.get_candles()
            # проверка условий входа в позицию
            if self.entry_rules(df):
                self.execute_trade('BUY', 0.1)
                self.position = 'LONG'
            # проверка условий выхода из позиции
            elif self.exit_rules(df):
                self.execute_trade('SELL', 0.1)
                self.position = None

            time.sleep(60)  # задержка в 60 секунд перед повторением


Класс TradingBot используется для определения входных и выходных стратегий, выполнения сделок и запуска торгового бота.

Принцип работы бота запущен в методе run(), который запущен в бесконечном цикле. В нем мы получаем данные из криптовалютной биржи (метод get_candles()), проверяем условия входа и выхода в позицию и, если условие выполнено, выполняем сделку (метод execute_trade()). Мы также имеем методы entry_rules() и exit_rules(), которые определяют условия входа и выхода из позиций, соответственно.

Также мы используем индикатор RSI, который мы импортировали из файла indicators.py. 

В файле indicators.py есть реализация RSI:

python
import numpy as np

def RSI(close, period):
    """
    Калькулятор индикатора RSI.
    :param close: Pandas Series с ценами закрытия для каждого периода.
    :param period: Число с количеством периодов для рассчета.
    :return: numpy array со значениями RSI.
    """
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.values


Здесь мы определяем функцию RSI(), которая принимает на вход последние цены закрытия и период для рассчета. Мы используем Pandas, чтобы вычислить изменения цены и критерии выигрыша и потерь. Затем мы используем скользящее среднее для расчета среднего выигрыша и потерь за период, и затем вычисляем RSI используя средние значения.

Класс TradingBot использует эту функцию для проверки RSI на каждом шаге в entry_rules() и exit_rules(), чтобы принять решение о торговле на основе этого индикатора, используется метод make_trade_decision. Он принимает в качестве параметров текущий баланс актива, цену на покупку и продажу, и открытые ордера (если они есть). Внутри метода прописаны логики и стратегии торговли.

Вот пример кода метода make_trade_decision:

python
def make_trade_decision(self, balance: float, buy_price: float, sell_price: float, open_orders: List[Dict]) -> str:
    if self.ema30 > self.ema100:
        if self.current_trend == "SHORT" and self.trend_since > self.trend_change_len:
            return self.open_order("BUY", buy_price, balance*0.5)
        else:
            return "HOLD"
    elif self.ema30 < self.ema100:
        if self.current_trend == "LONG" and self.trend_since > self.trend_change_len:
            return self.open_order("SELL", sell_price, self.asset_balance*0.5)
        else:
            return "HOLD"
    else:
        return "HOLD"

Метод сравнивает значения скользящих средних на 30 и 100 периодах, и в зависимости от их относительного положения и текущего тренда может вернуть решение о покупке, продаже или об удержании позиции.
Хорошо, давайте начнем с класса API, который реализует интерфейс для управления ботом через личный кабинет на бирже. 

python
class API:
    def __init__(self, exchange_name: str, api_key: str, api_secret: str):
        self.exchange_name = exchange_name
        self.client = None
        if self.exchange_name == 'Binance':
            self.client = Client(api_key, api_secret)
        elif self.exchange_name == 'Coinbase':
            self.client = cbpro.AuthenticatedClient(api_key, api_secret)

    def get_balance(self):
        if self.exchange_name == 'Binance':
            account_balance = self.client.get_account()['balances']
            balances = {}
            for coin in account_balance:
                if float(coin['free']) > 0:
                    balances[coin['asset']] = float(coin['free'])
            return balances
        elif self.exchange_name == 'Coinbase':
            account_balance = self.client.get_accounts()
            balances = {}
            for account in account_balance:
                if float(account['balance']) > 0:
                    balances[account['currency']] = float(account['balance'])
            return balances

В этом классе используется API биржи Binance или Coinbase для получения баланса на аккаунте. Функция get_balance возвращает словарь балансов для каждой криптовалюты, которая имеется на аккаунте.

> ChatGPT | Марти 🦓:
ChatGPT (беседа № 6):
Выбрана Ваша тестовая роль

Отлично, давайте начнем с файла api.py. В этом файле мы будем описывать класс ExchangeAPI, который предоставляет методы для взаимодействия с API биржи.

python
import requests
import time
import hmac
import hashlib

class ExchangeAPI:
    def __init__(self, api_key, api_secret):
        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.endpoint = 'https://api.binance.com'

    def sign_request(self, params):
        params['timestamp'] = int(time.time() * 1000)
        query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
        signature = hmac.new(self.API_SECRET.encode(), query_string.encode(), hashlib.sha256).hexdigest()
        params['signature'] = signature
        return params

    def get_price(self, symbol, ticker):
        response = requests.get(f"{self.endpoint}/api/v3/ticker/price", params={'symbol': symbol+ticker})
        return response.json()['price']

    def get_balance(self):
        params = self.sign_request({'timestamp': int(time.time() * 1000)})
        headers = {'X-MBX-APIKEY': self.API_KEY}
        response = requests.get(f"{self.endpoint}/api/v3/account", headers=headers, params=params)
        balances = {i['asset']: i for i in response.json()['balances']}
        return balances


В первой строке мы импортируем необходимые библиотеки: requests - для взаимодействия с API, time - для работы со временем, hmac и hashlib - для создания подписи запроса.

Затем мы определяем класс ExchangeAPI. Его конструктор получает два аргумента - api_key и api_secret, которые будут использоваться для аутентификации запросов к API биржи.

Метод sign_request создает подпись запроса на основе переданных параметров params. Для этого он добавляет к параметрам текущее время в миллисекундах, сортирует параметры по алфавиту и создает SHA256 хеш от строки с параметрами и секретным ключом. Подпись добавляется в словарь с параметрами запроса и возвращается.

Метод get_price возвращает текущую цену указанной пары symbol/ticker. Для получения цены он использует API биржи метод GET /api/v3/ticker/price.

Метод get_balance возвращает баланс аккаунта пользователя. Для этого он использует API биржи метод GET /api/v3/account. Сначала мы создаем подпись запроса с помощью метода sign_request, затем добавляем с помощью хэдера X-MBX-APIKEY наше API KEY и отправляем запрос на биржу. В ходе запроса мы получаем информацию о всех доступных балансах на аккаунте пользователя.

Следующим файлом, который мы посмотрим, будет bot.py. В этом файле мы опишем два класса: TradingBot и TradingStrategy.

python
from api import ExchangeAPI

class TradingStrategy:
    def __init__(self, exchange_api):
        self.exchange_api = exchange_api

    def buy(self):
        pass

    def sell(self):
        pass

    def run(self):
        pass


class TradingBot:
    def __init__(self, exchange, trading_strategy):
        self.exchange = exchange
        self.trading_strategy = trading_strategy

    def start(self):
        self.trading_strategy.run()


В первой строке мы импортируем класс ExchangeAPI из модуля api. Далее мы определяем класс TradingStrategy. Его конструктор получает объект exchange_api - экземпляр класса ExchangeAPI, который мы будем использовать для взаимодействия с API биржи. Затем мы определяем методы buy - для покупки криптовалюты, sell - для продажи криптовалюты и run - для запуска стратегии.

> ChatGPT | Марти 🦓:
Класс TradingBot также имеет конструктор, который принимает объект exchange - экземпляр класса ExchangeAPI и объект trading_strategy - экземпляр класса TradingStrategy. Метод start запускает стратегию.

Перед тем, как перейти к реализации конкретной стратегии торгов, определим несколько вспомогательных функций в файле utils.py.

python
import math

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


Функция round_down округляет число n с заданным количеством знаков после запятой decimals вниз.

Функция round_up округляет число n с заданным количеством знаков после запятой decimals вверх.

Затем мы можем использовать эти функции в конкретной стратегии торгов.

В файле strategies.py мы можем определить класс SimpleStrategy, который будет использовать простую стратегию на основе дисперсии цен.

python
from datetime import datetime, timedelta
from random import randint
from utils import round_down, round_up

class SimpleStrategy(TradingStrategy):
    def __init__(self, exchange_api, symbol, ticker, risk_tolerance=0.01, investment_amount=100, interval=30):
        super().__init__(exchange_api)
        self.symbol = symbol
        self.ticker = ticker
        self.risk_tolerance = risk_tolerance
        self.investment_amount = investment_amount
        self.interval = interval

    def get_next_price(self):
        price = float(self.exchange_api.get_price(self.symbol, self.ticker))
        variance = randint(-10, 10) * self.risk_tolerance * price
        next_price = round_down(price + variance, 2)
        return next_price

    def buy(self):
        balance = self.exchange_api.get_balance()[self.ticker]['free']
        if float(balance) > 0:
            return
        next_price = self.get_next_price()
        amount = round_down(self.investment_amount / next_price, 4)
        self.exchange_api.place_order(
            symbol=self.symbol+self.ticker,
            side='BUY',
            type='LIMIT',
            timeInForce='GTC',
            quantity=amount,
            price=next_price
        )

    def sell(self):
        balance = self.exchange_api.get_balance()[self.ticker]['free']
        if float(balance) == 0:
            return
        price = float(self.exchange_api.get_price(self.symbol, self.ticker))
        variance = randint(-10, 10) * self.risk_tolerance * price
        next_price = round_up(price + variance, 2)
        self.exchange_api.place_order(
            symbol=self.symbol+self.ticker,
            side='SELL',
            type='LIMIT',
            timeInForce='GTC',
            quantity=balance,
            price=next_price
        )

    def run(self):
        while True:
            now = datetime.now()
            if now.minute % self.interval == 0:
                self.sell()
                self.buy()
            time.sleep(60)


Конструктор класса SimpleStrategy получает объект класса ExchangeAPI, символ и тикер для торговли, риск-толерантность, сумму инвестирования и интервал в минутах между сделками.

Метод get_next_price вычисляет следующую цену на основе текущей цены и случайной величины, которая вычисляется как произведение дисперсии и текущей цены. Размер дисперсии выбирается случайно из диапазона [-10%; +10%] относительно текущей цены.

> ChatGPT | Марти 🦓:
Методы buy и sell реализуют покупку и продажу заданного количества криптовалюты по заданной цене с помощью метода place_order объекта ExchangeAPI.

Метод run запускает цикл, который каждые interval минут продает и затем покупает заданный токен на основе стратегии get_next_price.

> ChatGPT | Марти 🦓:
ChatGPT (беседа № 6):
Выбрана Ваша тестовая роль

Хорошо, давайте начнем с файла requirements.txt:


ccxt==1.39.63
python-binance==1.0.12
Flask==1.1.2
Flask-Cors==3.0.10


Это файл, который содержит зависимости проекта и установленные пакеты для бота. 

Далее, в файле api.py содержится класс Exchange с методами для подключения к бирже. Код:

python
import ccxt
from binance.client import Client
from binance.exceptions import BinanceAPIException

class Exchange:
    def __init__(self, exchange, api_key='', secret_key=''):
        self.exchange = exchange
        self.api_key = api_key
        self.secret_key = secret_key
        self.client = None
        self.ccxt_exchange = None
        self.load_exchange()

    def load_exchange(self):
        try:
            if self.exchange == 'binance':
                self.client = Client(self.api_key, self.secret_key)
            else:
                self.ccxt_exchange = getattr(ccxt, self.exchange)({
                    'apiKey': self.api_key,
                    'secret': self.secret_key,
                })
        except (ccxt.ExchangeError, BinanceAPIException):
            raise Exception(f"Error loading exchange {self.exchange}")


В этом классе определяется объект Exchange, который используется для подключения к бирже. В __init__ методе инициализируются все переменные и метод load_exchange() загружает библиотеку биржи и создает клиентское подключение.

Далее, в файле bot.py содержится класс TradingBot, который отвечает за торговлю. Код:

python
from api import Exchange

class TradingBot:
    def __init__(self, exchange, api_key, api_secret):
        self.exchange = Exchange(exchange, api_key, api_secret)
        self.symbols = self.exchange.get_symbols()
        self.strategy = None
        self.order = None
        self.balance = {}
        self.positions = {}
        self.trade_amount = 0
    
    def update_balance(self):
        self.balance = self.exchange.get_balance()
    
    def update_positions(self):
        self.positions = self.exchange.get_positions() if 'binance' in self.exchange.exchange else {}
    
    def get_trade_amount(self):
        if self.trade_amount:
            return self.trade_amount
        
        if 'binance' in self.exchange.exchange:
            exchange_info = self.exchange.client.get_exchange_info()
            base_asset = self.strategy.get_base_asset()
            symbol_info = next(filter(lambda x: x['symbol'] == self.strategy.symbol.upper(), exchange_info['symbols']))

            decimals = symbol_info['filters'][2]['stepSize'].find('1') - 1
            min_qty = float(symbol_info['filters'][2]['minQty'])
            max_qty = float(symbol_info['filters'][2]['maxQty'])
            min_notional = float(symbol_info['filters'][3]['minNotional'])
           
            if self.balance[base_asset]['free'] > min_notional:
                amount = self.balance[base_asset]['free'] * self.strategy.get_allocation()
                amount = max(min(amount, max_qty), min_qty)
                amount = round(amount, decimals)
                self.trade_amount = self.exchange.client.recalc_dust_to_bnb(symbol=self.strategy.symbol.upper(), qty=amount)
                return self.trade_amount


Этот класс создает объект бота и отвечает за торговлю на выбранной бирже. Метод __init__ инициализирует все переменные, необходимые для работы бота. Методы update_balance() и update_positions() обновляют баланс и позиции на бирже. Метод get_trade_amount() вычисляет количество криптовалюты для торговли на основе текущего баланса и выбранной стратегии.

> ChatGPT | Марти 🦓:
Наконец, в файле bot.py определены методы для различных стратегий торговли. Одним из них является SimpleMovingAverageStrategy:

python
import pandas as pd

class SimpleMovingAverageStrategy:
    def __init__(self, symbol, period_short, period_long):
        self.symbol = symbol
        self.period_short = period_short
        self.period_long = period_long
        
    def get_base_asset(self):
        return self.symbol.split('/')[1]
    
    def get_allocation(self):
        return 0.95
    
    def get_indicator(self, ohlcv_data):
        df = pd.DataFrame(ohlcv_data, columns=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
        df['SMA_short'] = df['Close'].rolling(window=self.period_short).mean()
        df['SMA_long'] = df['Close'].rolling(window=self.period_long).mean()
        df.dropna(inplace=True)
        return df['SMA_short'].values[-1], df['SMA_long'].values[-1]

    def get_signal(self, ohlcv_data):
        short_sma, long_sma = self.get_indicator(ohlcv_data)
        if short_sma > long_sma:
            return 'buy'
        elif short_sma < long_sma:
            return 'sell'
        else:
            return 'hold'


Эта стратегия использует простое скользящее среднее для генерации торговых сигналов. Метод get_base_asset() возвращает базовый актив выбранной валютной пары. Метод get_allocation() возвращает процент аллокации для торговли. Метод get_indicator() вычисляет скользящее среднее на заданных периодах и возвращает значения для использования в торговых сигналах. Метод get_signal() генерирует торговый сигнал на основе скользящего среднего.

Таким образом, класс TradingBot использует классы Exchange и SimpleMovingAverageStrategy для подключения к бирже и торговли используя заданную стратегию.

Да, всё понятно. Давайте начнём.

requirements.txt:


numpy==1.19.5
pandas==1.1.5
ccxt==1.36.29
python-dotenv==0.17.1

Дальше пойдём с файлом api.py.

Код файла api.py, который в основном отвечает за работу с API биржи, выглядит следующим образом:


import requests
import time

class Exchange():
    # Конструктор класса
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = 'https://api.binance.com'

    # Отправка GET-запроса к бирже
    def get_request(self, url, data=None, auth=False):
        response = requests.get(self.base_url + url, params=data, headers=(
            {'Content-type': 'application/json',
            'X-MBX-APIKEY': self.api_key} if auth else None)).json()
        return response

    # Отправка POST-запроса к бирже
    def post_request(self, url, data=None, auth=False):
        response = requests.post(self.base_url + url, json=data, headers=(
            {'Content-type': 'application/json',
            'X-MBX-APIKEY': self.api_key} if auth else None)).json()
        return response

    # Получение информации о пользователе
    def get_account(self):
        return self.get_request('/api/v3/account', None, True)

    # Получение информации о курсе валюты
    def get_ticker(self, symbol):
        return self.get_request('/api/v3/ticker/price', {'symbol': symbol}, False)

Здесь реализована базовая функциональность для отправки GET/POST запросов к API биржи, получения информации о пользователе и получения текущего курса валюты.

В файле api.py есть еще одна функция, которая выглядит примерно так:

python
def get_order_book(self, symbol, limit=5):
    return self.get_request('/api/v3/depth', {'symbol': symbol, 'limit': limit}, False)

Эта функция возвращает стакан цен (order book) для указанной пары торгов. Если тебе нужно, я могу продолжить кусочком кода этой функции.

> ChatGPT | Марти 🦓:
ChatGPT (беседа № 6):
Выбрана Ваша тестовая роль

Понятно. В файле api.py содержится основной класс Binance с методами для работы с API биржи Binance. Давай по порядку:

1. Класс Binance импортирует модуль requests и объявляет константы с адресом API и ключом для аутентификации:


import requests
from typing import List, Union

BASE_API_URL = 'https://api.binance.com'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
ACCEPT_LANGUAGE = 'en-US,en;q=0.5'

...




2. Затем идет определение метода __init__ с параметрами api_key и api_secret, в котором сохраняются ключи для запроса к API:


class Binance:
    def __init__(self, api_key: str, api_secret: str = ''):
        self.api_key = api_key
        self.api_secret = api_secret
        ... 


3. Далее идут методы для отправки запросов к API, такие как get_request и post_request:


class Binance:
    ...
    def get_request(self, path: str, params: dict = None, signed: bool = False) -> dict:
        headers = {
            'User-Agent': USER_AGENT,
            'Accept-Language': ACCEPT_LANGUAGE,
            'X-MBX-APIKEY': self.api_key
        }
        url = BASE_API_URL + path
        response = requests.get(url=url, headers=headers, params=params)
        return response.json()
        
    def post_request(self, path: str, params: dict = None, signed: bool = False) -> dict:
        headers = {
            'User-Agent': USER_AGENT,
            'Accept-Language': ACCEPT_LANGUAGE,
            'X-MBX-APIKEY': self.api_key
        }
        if signed:
            if not self.api_secret:
                raise ValueError('You need to set api_secret parameter first')
 
            params = params or {}
            timestamp = int(time.time() * 1000)

            signature_data = urllib.parse.urlencode(sorted(params.items()))
            signature_data += f'&timestamp={timestamp}'
            signature = hmac.new(self.api_secret.encode(), signature_data.encode(), hashlib.sha256).hexdigest()

            params['timestamp'] = timestamp
            params['signature'] = signature
            
            url = BASE_API_URL + path + '?' + urllib.parse.urlencode(params)
            response = requests.post(url=url, headers=headers)
        else:
            url = BASE_API_URL + path
            response = requests.post(url=url, headers=headers, params=params)

        return response.json()        


4. Метод get_ticker_price получает текущую цену заданной криптовалюты:


class Binance:
    ...
    def get_ticker_price(self, symbol: str) -> dict:
        return self.get_request('/api/v3/ticker/price', {'symbol': symbol}, False)
  



5. Метод get_order_book возвращает данные о стакане торгов по заданной валютной паре:


class Binance:
    ...
    def get_order_book(self, symbol: str, limit: int = 100) -> dict:
        return self.get_request('/api/v3/depth', {'symbol': symbol, 'limit': limit}, False)


6. get_klines возвращает котировки заданной криптовалютной пары за определенный промежуток времени:


class Binance:
    ...
    def get_klines(self, symbol: str, interval: str, limit: int = None) -> List[List[Union[int, float]]]:
        params = {'symbol': symbol, 'interval': interval}
        if limit:
            params['limit'] = limit
        return self.get_request('/api/v3/klines', params, False)


7. Метод create_order создает новый ордер на покупку или продажу заданной криптовалюты:

> ChatGPT | Марти 🦓:

class Binance:
    ...
    def create_order(self, symbol: str, side: str, type: str, quantity: float, price: float or None = None, time_in_force: str = 'GTC', **kwargs) -> dict:
        params = {
            'symbol': symbol,
            'side': side,
            'type': type,
            'timeInForce': time_in_force,
            'quantity': quantity,
        }
        if price:
            params['price'] = price
        params.update(kwargs)
        return self.post_request('/api/v3/order', params, True)


8. Метод get_account_info возвращает информацию о балансе аккаунта:


class Binance:
    ...
    def get_account_info(self) -> dict:
        return self.get_request('/api/v3/account', None, True)



9. get_open_orders возвращает список открытых ордеров:


class Binance:
    ...
    def get_open_orders(self, symbol: str = None, recv_window: int = None) -> List[dict]:
        params = {}
        if symbol:
            params['symbol'] = symbol
        if recv_window:
            params['recvWindow'] = recv_window
        return self.get_request('/api/v3/openOrders', params, True)



> ChatGPT | Марти 🦓:
ChatGPT (беседа № 6):
Выбрана Ваша тестовая роль

Конечно, начнем с импорта необходимых модулей:

python
import logging
import time
from binance.enums import *
from binance.exceptions import *


Затем создадим класс бота.

python
class Bot:
    def __init__(self, **kwargs):
        self.client = kwargs['client']
        self.symbols = kwargs['symbols']
        self.base_currency = kwargs['base_currency']
        self.quote_currency = kwargs['quote_currency']
        self.symbol = kwargs['symbol']
        self.interval = kwargs['interval']
        self.quantity = kwargs['quantity']
        self.strategy = kwargs['strategy']

        self.log = logging.getLogger('bot')

    def start(self):
        while True:
            try:
                self.run()
            except Exception as e:
                self.log.error(f'Error: {e}', exc_info=True)
            time.sleep(self.interval)


Этот класс принимает параметры для инициализации, такие как client (API-объект), symbols (пары торговли), interval (интервал опроса котировок), etc. Метод start() запускает работу бота и определяет структуру его работы.

Следующий шаг - реализация метода run(). Он будет контролировать все эти выбранные параметры и в соответствии с ними осуществлять торговые операции (в зависимости от выбранной стратегии).

python
    def run(self):
        base_balance = self.get_balance(self.base_currency)
        quote_balance = self.get_balance(self.quote_currency)
        self.log.info(f'Base balance: {base_balance} {self.base_currency}, Quote balance: {quote_balance} {self.quote_currency}')

        if self.strategy == 'scalper':
            self.scalper_strategy(base_balance, quote_balance)

        elif self.strategy == 'trend_follower':
            self.trend_following_strategy(base_balance, quote_balance)

        else:
            self.log.warning('No such strategy found')

    def get_balance(self, symbol):
        return float(self.client.get_asset_balance(asset=symbol)['free'])



Метод run() осуществляет следующие шаги:
- определяет баланс базовой и котируемой валюты (base и quote currency);
- выбирает подходящую стратегию (scalper или trend_follower);
- вызывает соответствующий метод стратегии.

В методе get_balance() мы запросим баланс для указанной валюты (asset) на бирже.

python
    def scalper_strategy(self, base_balance, quote_balance):
        self.log.info('Starting scalper strategy')

        try:
            order_book = self.client.get_order_book(symbol=self.symbol, limit=5)
            bid_price = float(order_book['bids'][0][0])
            ask_price = float(order_book['asks'][0][0])
        except Exception as e:
            self.log.error(f'Error: {e}', exc_info=True)
            return

        if bid_price >= ask_price:
            self.log.warning(f'Bid ({bid_price}) price >= Ask ({ask_price}) price')
            return

        current_price = float(self.client.get_symbol_ticker(symbol=self.symbol)['price'])
        quantity = self.calc_quantity(base_balance, current_price)

        if quantity <= 0:
            self.log.warning(f'Not enough {self.base_currency} to place an order')
            return

        if current_price <= bid_price:
            self.log.info(f'Current price ({current_price}) <= bid ({bid_price}), buying {self.base_currency}')
            order = self.client.order_market_buy(symbol=self.symbol, quoteOrderQty=quote_balance)
            self.log.info(f'Filled buy {self.base_currency} market order: {order}')

> ChatGPT | Марти 🦓:
        elif current_price >= ask_price:
            self.log.info(f'Current price ({current_price}) >= ask ({ask_price}), selling {self.base_currency}')
            order = self.client.order_market_sell(symbol=self.symbol, quantity=quantity)
            self.log.info(f'Filled sell {self.base_currency} market order: {order}')



Одна из выбранных стратегий, которую мы будем используем, называется scalper и основана на краткосрочных сделках с небольшой прибылью. Этот метод контролирует торговлю в соответствии с этой стратегией.

python
    def trend_follower_strategy(self, base_balance, quote_balance):
        self.log.info('Starting trend following strategy')

        try:
            klines = self.client.get_klines(symbol=self.symbol, interval=self.interval)
        except Exception as e:
            self.log.error(f'Error: {e}', exc_info=True)
            return

        if len(klines) < 2:
            self.log.warning(f'Not enough data to analyze for {self.interval} data')
            return

        close_prices = [float(entry[4]) for entry in klines[:-1]]
        last_close = float(klines[-2][4])
        sma = sum(close_prices) / len(close_prices)

        if last_close < sma:
            price = float(self.client.get_symbol_ticker(symbol=self.symbol)['price'])
            quantity = self.calc_quantity(base_balance, price)

            if quantity <= 0:
                self.log.warning(f'Not enough {self.base_currency} to place an order')
                return

            self.log.info(f"Current price: {price}. Last closing price ({last_close}) < SMA ({sma}), buying {self.base_currency}")
            order = self.client.order_market_buy(symbol=self.symbol, quoteOrderQty=quote_balance)
            self.log.info(f"Filled buy {self.base_currency} market order: {order}")
        else:
            self.log.info(f"Last closing price ({last_close}) >= SMA ({sma}), selling {self.base_currency}")
            order = self.client.order_market_sell(symbol=self.symbol, quantity=

...price = self.client.get_symbol_ticker(symbol=self.symbol)[
            'price']
        order = self.client.order_market_sell(symbol=self.symbol, quantity=amount)

        return order

    def execute_buy_order(self, amount):
        price = self.client.get_symbol_ticker(symbol=self.symbol)[
            'price']
        order = self.client.order_market_buy(symbol=self.symbol, quantity=amount)

        return order

    def get_trade_history(self):
        trades = self.client.get_my_trades(symbol=self.symbol)

        return trades

    def calculate_profit(self, trades):
        total = 0
        for trade in trades:
            if trade['isBuyer']:
                total -= float(trade['price']) * float(trade['qty'])
            else:
                total += float(trade['price']) * float(trade['qty'])

        return total

    def run_bot(self):
        # Run bot indefinitely
        while True:
            balance = self.get_balances()
            trades = self.get_trade_history()

            profit = self.calculate_profit(trades)
            total_balance = float(balance['BTC']['free']) + float(balance['BTC']['locked'])

            if profit > 0 and total_balance > 0:
                # Sell 50% of balance
                amount = total_balance / 2
                self.execute_sell_order(amount)

            # Buy if balance is 0
            if total_balance == 0:
                amount = self.trade_size
                self.execute_buy_order(amount)

            time.sleep(600)

if __name__ == '__main__':
    bot = TradingBot('BTCUSDT')
    bot.run_bot()
    print('Bot successfully started')

class Bot:
    def __init__(self, symbol, orderQuantity, stopLossPercentage, apiKey, apiSecret):
        self.symbol = symbol  # Название пары валют, с которой работает бот (например, 'BTCUSDT')
        self.orderQuantity = orderQuantity  # Количество валюты, которым торгует бот за один ордер (например, 0.01)
        self.stopLossPercentage = stopLossPercentage  # Процент для стоп-лосс ордера (например, 1.5%)
        self.client = Client(apiKey, apiSecret)  # Создаем объект клиента для взаимодействия с Binance

    def run(self):
        print('Bot successfully started')
        while True:
            try:
                ticker = self.client.get_symbol_ticker(symbol=self.symbol)  # Получаем текущий тикер
                price = float(ticker['price'])  # Получаем текущую цену
                quantity = self.get_available_quantity()  # Получаем доступное количество валюты для торговли
                if quantity < self.orderQuantity:  # Если доступное количество валюты меньше размера ордера, то ничего не делаем
                    print('Not enough quantity')
                else:
                    order = self.client.order_market_sell(symbol=self.symbol, quantity=self.orderQuantity)  # Создаем ордер на продажу
                    # Если ордер не был исполнен, то перевыставляем его по маркет цене
                    if self.check_order_status(order) == 'FILLED':
                        self.create_new_order(price)
                        self.place_stop_loss_order(price)
                        time.sleep(30)  # Приостанавливаем работу бота на 30 секунд
                    else:
                        self.client.order_market_sell(symbol=self.symbol, quantity=self.orderQuantity)        

            except KeyboardInterrupt:
                sys.exit()

            except Exception as e:
                print('Bot is not working')
                print(e)
                time.sleep(30)  # Приостанавливаем работу бота на 30 секунд

    def check_order_status(self, order):
        return self.client.get_order(symbol=self.symbol, orderId=order['orderId'])['status']

    def get_available_quantity(self):
        balances = self.client.get_account()
        for balance in balances['balances']:
            if balance['asset'] == self.symbol.replace('BTC', '') and float(balance['free']) > 0:
                return float(balance['free'])
        return 0

    def create_new_order(self, price):
        self.orderQuantity = round(((self.orderQuantity * price) * 0.998), 2)

    def place_stop_loss_order(self, price):
        stopPrice = round(price - ((price / 100) * self.stopLossPercentage), 2)
        order = self.client.create_order(
            symbol=self.symbol,
            side=SIDE_SELL,
            type=ORDER_TYPE_STOP_LOSS_LIMIT,
            quantity=self.orderQuantity,
            stopPrice=stopPrice,
            price=stopPrice)
        return order
order = self.client.order_market_sell(symbol=self.symbol, quantity=quantity)
        logging.info("Sell order placed: symbol=%s, quantity=%s", self.symbol, quantity)
        return order

    def cancel_open_orders(self):
        """
        Cancel all open orders for symbol
        :return: None
        """
        orders = self.client.get_open_orders(symbol=self.symbol)
        if not orders:
            logging.info("No open orders found")
            return
        for order in orders:
            canceled_order = self.client.cancel_order(symbol=self.symbol, orderId=order['orderId'])
            logging.info("Canceled order: %s", canceled_order)

    def get_balance(self):
        """
        Get available balance for symbol asset
        :return: balance (float)
        """
        account_info = self.client.get_account()
        balance = 0.0
        for asset in account_info['balances']:
            if asset['asset'] == self.symbol[:-3]:
                balance = float(asset['free'])
                break
        logging.info("Account balance: symbol=%s, balance=%s", self.symbol, balance)
        return balance

    def start(self):
        """
        Start the bot
        :return: None
        """
        logging.info("Bot successfully started")
        while True:
            self.cancel_open_orders()
            balance = self.get_balance()
            if balance > 0:
                buy_quantity = self.calculate_buy_quantity(balance)
                if buy_quantity:
                    self.buy(buy_quantity)
                    self.sell(buy_quantity)
            time.sleep(self.interval)

    def calculate_buy_quantity(self, balance):
        """
        Calculate buy quantity for symbol asset
        :param balance: available balance for symbol asset
        :return: buy_quantity (float)
        """
        if balance <= 0:
            logging.warning("Not enough balance to buy. symbol=%s", self.symbol)
            return None
        ticker = self.client.get_symbol_ticker(symbol=self.symbol)
        bid_price = float(ticker['price'])
        buy_quantity = (balance * self.buy_percentage) / bid_price
        logging.info("Buy quantity calculated: symbol=%s, bid_price=%s, buy_quantity=%s", self.symbol, bid_price,
                     buy_quantity)
        return buy_quantity


if __name__ == "__main__":
    my_bot = Bot()
    my_bot.start()
from api import Binance

class TradeBot:
    def __init__(self, api_key: str, api_secret: str, symbol: str, quantity: float, 
                goal_profit: float, stop_loss: float, interval: int):
        self.client = Binance(api_key, api_secret)
        self.symbol = symbol
        self.quantity = quantity
        self.goal_profit = goal_profit
        self.stop_loss = stop_loss
        self.interval = interval

    def get_price(self):
        ticker = self.client.get_ticker_price(self.symbol)
        return float(ticker['price'])

    def get_balance(self):
        balance = self.client.get_account_info()
        for item in balance['balances']:
            if item['asset'] == self.symbol[:-3]:
                return float(item['free'])
        return 0
    
    def buy(self):
        order = self.client.order_market_buy(symbol=self.symbol, quantity=self.quantity)
        return order

    def sell(self):
        order = self.client.order_market_sell(symbol=self.symbol, quantity=self.quantity)
        return order

    def start(self):
        print('Bot успешно запущен')
        while True:
            try:
                price = self.get_price()
                balance = self.get_balance()
                if price / self.goal_profit >= self.get_price() and balance > self.quantity:
                    self.sell()
                elif price /self.stop_loss <= self.get_price() and balance > self.quantity:
                    self.sell()
                elif balance == 0:
                    self.buy()
                time.sleep(self.interval)
            except Exception as error:
                print(error)
                time.sleep(5)
В файле bot.py написан класс TradingBot, который будет управлять нашим торговым ботом. 

python
class TradingBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.symbol = 'BTCUSDT'

Класс TradingBot имеет два атрибута: client и symbol. client - это экземпляр класса Client из библиотеки python-binance, который позволяет нам взаимодействовать с API биржи Binance. Мы передаем ключ и секретный ключ, которые были созданы на сайте биржи Binance. symbol - это пара торгуемых валют, которую мы будем использовать в нашем боте. 

python
    def get_price(self):
        '''Получаем цену выбранной пары'''

        price = float(self.client.get_symbol_ticker(symbol=self.symbol)['price'])
        return price

Этот метод использует метод get_symbol_ticker объекта client, чтобы получить текущую цену выбранной пары. Мы передаем self.symbol в качестве аргумента для метода get_symbol_ticker и затем вызываем значение ключа 'price' из полученного словаря. Возвращаем цену в качестве значения.

python
    def buy(self, quantity):
        '''Размещает ордер на покупку монет'''

        order = self.client.order_market_buy(symbol=self.symbol, quantity=quantity)
        return order

Этот метод использует метод order_market_buy объекта client, чтобы разместить рыночный ордер на покупку quantity монет выбранной пары. Возвращаем order в качестве значения.

python
    def sell(self, quantity):
        '''Размещает ордер на продажу монет'''

        order = self.client.order_market_sell(symbol=self.symbol, quantity=quantity)
        return order

Этот метод использует метод order_market_sell объекта client, чтобы разместить рыночный ордер на продажу quantity монет выбранной пары. Возвращаем order в качестве значения.

python
    def set_stop_loss(self, stop_price, quantity):
        '''Размещает стоп-лимит ордер для нашей позиции'''

        price = self.get_price()
        limit_price = str(round(price * Decimal(1 - (stop_price / 100)), 2))
        print('Setting stop loss at ' + limit_price)
        
        order = self.client.create_order(symbol=self.symbol, 
                                          side=SIDE_SELL,
                                          type=ORDER_TYPE_STOP_LOSS_LIMIT,
                                          timeInForce=TIME_IN_FORCE_GTC,
                                          quantity=quantity,
                                          price=limit_price,
                                          stopPrice=str(stop_price))
        return order

Этот метод использует метод create_order объекта client, чтобы разместить стоп-лимит ордер на продажу quantity монет выбранной пары. stop_price указывает цену, при достижении которой должен выполниться наш ордер стоп-лимит, а limit_price будет ценой, по которой будет размещен лимитный ордер, который поможет избежать значительных потерь при продаже. 
python
class Bot:
    def __init__(self, coin_pair, interval=5):
        self.api_manager = ApiManager(coin_pair)
        self.order_manager = OrderManager(self.api_manager)
        self.balance_manager = BalanceManager(self.api_manager)
        self.symbol = '_'.join(coin_pair.split('-')).upper()
        self.pending_orders = []

        self.client = Client()
        self.interval = interval

    def start(self):
        print('Bot успешно запущен')
        while True:
            try:
                time.sleep(self.interval)
                self.update_orders()
            except KeyboardInterrupt:
                break

    def update_orders(self):
        closed_orders = []
        for order in self.pending_orders:
            if order.is_closed:
                print(order)
                closed_orders.append(order)
        for order in closed_orders:
            self.pending_orders.remove(order)

Продолжу опять с последней строки файла:
python
if 'sell' in signal and self.balance_manager.can_sell:
            order = self.order_manager.create_market_sell_order(
                self.symbol, self.balance_manager.current_stock())
            self.pending_orders.append(order)
            
        time.sleep(self.interval)

Следующую часть кода вышлю, когда будешь готов.
 Вот следующий кусок кода из файла bot.py:


def main():
    # создаем объект API
    api_params = get_params('api')
    api = Api(api_params['key'], api_params['secret'])

    # создаем объект бота
    bot_params = get_params('bot')
    my_bot = Bot(api, bot_params)

    # запускаем бота
    my_bot.start()

if __name__ == '__main__':
    main()

Эта часть кода описывает основную функцию, в которой создается объект API и объект бота, которые затем используются для запуска самого бота. 

Функция main() обладает следующей логикой:
- загружает параметры для объектов API и бота из файла конфигурации;
- создает объект API;
- используя API, создает объект бота;
- запускает бота через вызов метода start().

Ну и конструкция if __name__ == '__main__' говорит о том, что если этот скрипт запущен напрямую (а не импортирован в другой скрипт), тогда вызываем функцию main(). 
Следующая часть файла bot.py:

python
class MyBot:
    def __init__(self, api):
        self.api = api
        self.symbol = 'BTCUSDT'
        self.profitable_trade = False
        self.active_orders = []

python
    @staticmethod
    def calculate_profit(open_price, close_price, quantity):
        return (close_price - open_price) * quantity
python
class Bot:
    def __init__(self, api_key, secret_key, symbol, interval):
        self.client = Client(api_key, secret_key)
        self.symbol = symbol
        self.interval = interval
        self.ticks = []
        self.prices = []

python
    def start(self):
        self.get_ticks()
        self.get_prices()
        while True:
            self.trade()

python
    def get_ticks(self):
        def append_tick(tick, ticks):
            tick_time = tick['E']
            tick_close = float(tick['c'])

            ticks.append((tick_time, tick_close))

        ticks = self.client.aggregate_trade_iter(symbol=self.symbol, start_str='1 day ago UTC')
        for tick in ticks:
            append_tick(tick, self.ticks)
            time.sleep(1)

python
    def get_prices(self):
        klines = self.client.get_historical_klines(self.symbol, self.interval, '1 day ago UTC')
        for kline in klines:
            kline_close = float(kline[4])
            self.prices.append(kline_close)
            time.sleep(0.5)

python
    def get_sma(self, window):
        prices = self.prices[-window:]
        return sum(prices) / len(prices)
Код из файла requirements.txt:


requests
pandas
numpy
python-binance
python-dotenv


Код из файла api.py:


python
class BinanceAPI:

    def __init__(self, key=None, secret=None):
        self.base_url = 'https://api.binance.com'
        self.key = key
        self.secret = secret
        self.session = requests.Session()

    def _get_headers(self, signed):
        headers = {'Content-Type': 'application/json'}
        if signed:
            query_string = urlencode(params)
            signature = hmac.new(self.secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()
            headers['X-MBX-APIKEY'] = self.key
        return headers

    def _request(self, method, path, params=None, signed=False):
        url = self.base_url + path
        headers = self._get_headers(signed)
        response = self.session.request(method, url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_request(self, path, params=None, signed=False):
        return self._request('GET', path, params, signed)

    def post_request(self, path, params=None, signed=False):
        return self._request('POST', path, json=params, signed=signed)

    def get_ticks_price(self, symbol):
        return self.get_request('/api/v3/ticker/price', {'symbol': symbol}, False)

    def get_depth(self, symbol='BTCUSDT', limit=5):
        return self.get_request('/api/v3/depth', {'symbol': symbol, 'limit': limit}, False)



Код из файла bot.py:


python
class CryptoBot:

    def __init__(self, api_key=None, api_secret=None, trade_limit=1000.0):
        self.trade_limit = trade_limit
        self.api = BinanceAPI(api_key, api_secret)
        self.symbol = 'BTCUSDT'

    def run(self):
        print('Bot successfully started')
        while True:
            tick_price = float(self.api.get_ticks_price(self.symbol)['price'])
            depth = self.api.get_depth(self.symbol)
            bids_sum = sum([float(bid[1]) for bid in depth['bids']])
            asks_sum = sum([float(ask[1]) for ask in depth['asks']])
            if bids_sum > asks_sum:
                order = self.client.order_market_buy(symbol=self.symbol, quantity=self.trade_limit/tick_price)
            else:
                order = self.client.order_market_sell(symbol=self.symbol, quantity=self.trade_limit/tick_price)
            
            print(order)
            time.sleep(5)
. В файле bot.py есть ещё одна функция get_current_price(). Вот её код:


def get_current_price(self):
    """
    Get current price of coin

    :return: current price
    """

    data = self.api.get_price(self.symbol)

    if data:
        return float(data['price'])
    else:
        return None

Также есть функция для расчёта размера позиции:


def get_order_quantity(self, price, balance):
    """
    Calculate order quantity based on price and available balance

    :param price: price to buy or sell at
    :param balance: available balance
    :return: order quantity
    """

    quantity = (balance * self.risk_percentage) / 100
    return quantity / price

И ещё одна функция для покупки:


def buy(self, price):
    """
    Buy coins at a given price

    :param price: price to buy coins at
    """

    balance = self.get_balance() * self.balance_percentage

    if balance <= 0:
        return

    quantity = self.get_order_quantity(price, balance)

    if quantity <= 0:
        return

    order = self.client.order_market_buy(symbol=self.symbol, quantity=quantity)

    if order:
        return True
    else:
        return False

Кроме того, есть функция для продажи:


def sell(self, price):
    """
    Sell coins at a given price

    :param price: price to sell coins at
    """

    quantity = self.get_balance()

    if quantity <= 0:
        return

    order = self.client.order_market_sell(symbol=self.symbol, quantity=quantity)

    if order:
        return True
    else:
        return False

И, наконец, основная функция main():


def main():
    """
    Main function that runs the bot
    """
    my_bot = CryptoBot()
    my_bot.start()

if __name__ == '__main__':
    main()









