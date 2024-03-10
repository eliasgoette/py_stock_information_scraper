import requests
from bs4 import BeautifulSoup

class YahooScraper:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def get_stock_price(self):
        symbol = self.symbol
        url = f"https://finance.yahoo.com/quote/{symbol}"
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find the fin-streamer tag
            fin_streamer = soup.find('fin-streamer', {'data-symbol': symbol, 'data-test': 'qsp-price', 'data-field': 'regularMarketPrice'})
            
            if fin_streamer:
                # Extract the value attribute containing the price
                price = fin_streamer.get('value')
                if price:
                    return price.strip()
                else:
                    print("Price attribute not found in fin-streamer tag.")
            else:
                print("Fin-streamer tag not found.")
        else:
            print("Failed to fetch data or page not available.")
