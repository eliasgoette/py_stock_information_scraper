# Paste example outside of this module
from py_stock_price_scraper.yahoo_scraper import YahooScraper

scraper = YahooScraper()
symbol = ''

while symbol == '':
    symbol = input('Ticker symbol (case-sensitive) > ')

print('Fetching price')
price = scraper.get_stock_price(symbol)
print(price)
