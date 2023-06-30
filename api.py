import requests


class BinanceAPI:

    def __init__(self):
        self.base_url = 'https://api.binance.com/api/v3'

    """Метод  для получения последних цен на криптовалюты"""

    def get_crypto_price(self, symbol):
        url = f"{self.base_url}/ticker/price?symbol={symbol}USDT"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return float(data['price'])
        else:
            raise Exception(f"Ошибка при получении цены для {symbol}. Код ошибки: {response.status_code}")
