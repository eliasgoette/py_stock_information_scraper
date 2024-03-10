import requests
from bs4 import BeautifulSoup

class YahooScraper:
    def __init__(self, symbol):
        self.symbol = symbol

    def _fetch_page(self):
        symbol = self.symbol
        url = f"https://finance.yahoo.com/quote/{symbol}"
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            print("Failed to fetch data or page not available.")
            return None

    def _find_fin_streamer(self, soup, data_field):
        symbol = self.symbol
        return soup.find('fin-streamer', {'data-symbol': symbol, 'data-field': data_field})

    def _extract_value(self, fin_streamer):
        if fin_streamer:
            value = fin_streamer.get('value')
            if value:
                return float(value.replace(",", ""))
            else:
                print(f"Value attribute not found in fin-streamer tag.")
        else:
            print("Fin-streamer tag not found.")
        return None

    def get_stock_price(self):
        soup = self._fetch_page()
        if soup:
            fin_streamer = self._find_fin_streamer(soup, 'regularMarketPrice')
            return self._extract_value(fin_streamer)
        return None

    def get_volume(self):
        soup = self._fetch_page()
        if soup:
            fin_streamer_volume = self._find_fin_streamer(soup, 'regularMarketVolume')
            return self._extract_value(fin_streamer_volume)
        return None
