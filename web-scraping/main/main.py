from scraping_website import *

if __name__ == "__main__":
  coin_list = ['Bitcoin', 'Ethereum', 'Tether', 'Litecoin'] # Name of cryptocurrencies you want to get
  WebScraping(coin_list).scarping()