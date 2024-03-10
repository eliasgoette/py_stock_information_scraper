# Paste example outside of this module
from py_stock_information_scraper.yahoo_scraper import YahooScraper

symbol = ''

while symbol == '':
    symbol = input('Ticker symbol (case-sensitive) > ')

print('Fetching price')
scraper = YahooScraper(symbol)
price = scraper.get_stock_price()
print(f'Price of {symbol}: ${price}')
