python
import requests
import config


class Bot():
    def __init__(self):
        self.base_url = config.BASE_URL
        self.api_key = config.API_KEY
        self.secret_key = config.SECRET_KEY

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

if __name__ == '__main__':
    bot = Bot()
