import requests
from bs4 import BeautifulSoup

class YahooScraper:
  def get_stock_price(self, symbol):  # Add self as the first parameter
    url = f"https://finance.yahoo.com/quote/{symbol}"
    response = requests.get(url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      # Attempt to find the fin-streamer tag, where the price should be displayed
      fin_streamer = soup.find('fin-streamer', {'data-symbol': symbol, 'data-test': 'qsp-price', 'data-fie>
      if fin_streamer:
        price = fin_streamer['value']
        return price
      else:
        print("Price not found on the page.")
    else:
      print("Failed to fetch data")





