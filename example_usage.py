# From outside of this module
from py_stock_price_scraper.yahoo_scraper import YahooScraper

scraper = YahooScraper()
symbol = 'MSFT'
price = scraper.get_stock_price(symbol)
print(price)
