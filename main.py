from api import BinanceAPI
from checking import CryptoChecker

# Создаем экземпляры классов
binance_api = BinanceAPI()
cryptocurrencies = ['BTC', 'ETH', 'XRP', 'LTC', 'EOS']
crypto_checker = CryptoChecker(binance_api, cryptocurrencies)

# Получаем цены криптовалют
crypto_prices = crypto_checker.get_crypto_prices()

# Записываем цены в файл
crypto_checker.write_prices_to_file(crypto_prices, 'crypto_prices.txt')

print(crypto_prices)
