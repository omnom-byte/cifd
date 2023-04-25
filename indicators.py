python
def bands(data):
    """
    Вычисление Bollinger Bands для данных

    :param data: данные для вычисления (например, список цен закрытия биржевых сделок)
    :type data: list[float]

    :return: результаты вычислений Bollinger Bands
    :rtype: tuple[float, float, float]
    """

    # вычисляем среднее и стандартное отклонение цен закрытия
    average = sum(data) / len(data)
    std = (sum((d - average) ** 2 for d in data) / len(data)) ** 0.5

    # вычисляем крайние точки Bollinger Bands
    upper_band = average + std * 2
    lower_band = average - std * 2

    return (upper_band, average, lower_band)
  
def rsi(data, period=14):
    """
    Вычисление Relative Strength Index (RSI) для данных

    :param data: данные для вычисления (например, список цен закрытия биржевых сделок)
    :type data: list[float]

    :param period: период RSI
    :type period: int

    :return: RSI для данных
    :rtype: float
    """

    # рассчитываем изменение цены между текущим и предыдущим днем
    deltas = [data[i + 1] - data[i] for i in range(len(data) - 1)]

    # рассчитываем псевдо-максимум и псевдо-минимум
    up = [d for d in deltas if d >= 0]
    down = [abs(d) for d in deltas if d < 0]
    # рассчитываем среднее значение изменений
    avg_up = sum(up) / period
    avg_down = sum(down) / period
    # рассчитываем отношение средних изменений
    rs = avg_up / avg_down
    # рассчитываем RSI
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi
