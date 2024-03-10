import requests
from bs4 import BeautifulSoup
from decimal import Decimal

class YahooScraper:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.session = requests.Session()

    def _fetch_page(self) -> BeautifulSoup:
        symbol = self.symbol
        url = f"https://finance.yahoo.com/quote/{symbol}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Failed to fetch data: {e}")
            return None

    def _find_fin_streamer(self, soup: BeautifulSoup, data_field: str):
        symbol = self.symbol
        return soup.find('fin-streamer', {'data-symbol': symbol, 'data-field': data_field})

    def _extract_value(self, fin_streamer) -> Decimal:
        if fin_streamer:
            value = fin_streamer.get('value')
            if value:
                return Decimal(value.replace(",", ""))
            else:
                print(f"Value attribute not found in fin-streamer tag.")
        else:
            print("Fin-streamer tag not found.")
        return Decimal(0)  # Return 0 if value extraction fails

    def get_stock_price(self) -> Decimal:
        soup = self._fetch_page()
        if soup:
            fin_streamer = self._find_fin_streamer(soup, 'regularMarketPrice')
            return self._extract_value(fin_streamer)
        return Decimal(0)  # Return 0 if fetching soup fails

    def get_volume(self) -> Decimal:
        soup = self._fetch_page()
        if soup:
            fin_streamer_volume = self._find_fin_streamer(soup, 'regularMarketVolume')
            return self._extract_value(fin_streamer_volume)
        return Decimal(0)  # Return 0 if fetching soup fails
