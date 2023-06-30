class CryptoChecker:
    def __init__(self, binance_api, cryptocurrencies):
        self.binance_api = binance_api
        self.cryptocurrencies = cryptocurrencies

    def get_crypto_prices(self):
        prices = {}
        for currency in self.cryptocurrencies:
            try:
                price = self.binance_api.get_crypto_price(currency)
                prices[currency] = price
            except Exception as e:
                print(e)
        return prices

    def write_prices_to_file(self, prices, filename):
        with open(filename, 'w') as file:
            for currency, price in prices.items():
                file.write(f"{currency}: {price}\n")

    def compare_with_btc(self, prices):
        btc_price = prices['BTC']
        lower_than_btc = []
        for currency, price in prices.items():
            if price < btc_price:
                lower_than_btc.append(currency)
        return lower_than_btc