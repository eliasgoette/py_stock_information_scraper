from collections import deque
from statistics import mean
from yahoo_scraper import YahooScraper
import time

def calculate_moving_average(data, window_size):
    if len(data) < window_size:
        return None
    return mean(data)

def main():
    sma_price_period = 6
    sma_volume_period = 6
    symbol = input('Enter ticker symbol (case-sensitive) > ')
    
    price_window = deque(maxlen=sma_price_period)  # Moving average window for price
    volume_window = deque(maxlen=sma_volume_period)  # Moving average window for volume
    
    while True:
        scraper = YahooScraper(symbol)
        price = scraper.get_stock_price()
        volume = scraper.get_volume()
        
        if price is not None and volume is not None:
            price_window.append(price)
            volume_window.append(volume)
            
            price_ma = calculate_moving_average(price_window, sma_price_period)
            volume_ma = calculate_moving_average(volume_window, sma_volume_period)
            
            print(f"Price: {price}, Volume: {volume}, Price Moving Average: {price_ma}, Volume Moving Average: {volume_ma}")
        else:
            print("Failed to fetch price or volume.")
        
        time.sleep(15)  # Wait for 15 seconds before fetching data again

if __name__ == "__main__":
    main()
