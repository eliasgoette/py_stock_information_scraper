from yahoo_scraper import YahooScraper

# Example usage:
example_symbol = 'AAPL'  # Example stock symbol (Apple Inc.)
scraper = YahooScraper()
stock_price = scraper.get_stock_price(example_symbol)
if stock_price:
    print(f"The current price of {example_symbol} is {stock_price}")
