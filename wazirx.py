class Wazirx:
    def __init__(self):
        self.base = 'https://api.wazirx.com/'

    def get_market_status(self):
        api_url = self.base + '/api/v2/market-status'

    def get_ticker(self):
        api_url = self.base + '/api/v2/tickers'

    def get_market_depth(self):
        api_url = self.base + '/api/v2/depth'

    def get_trade_history(self):
        api_url = self.base + '/api/v2/trades'

    def get_price(self, currency1, currency2):
        pass


if __name__ == '__main__':
    wzx = Wazirx()
    wzx.get_price()
