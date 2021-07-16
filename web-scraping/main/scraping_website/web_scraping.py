from datetime import datetime
from bs4 import BeautifulSoup
from scraping_website import NavigateWebsite
from mysqldb import MysqlDB

class WebScraping:
  def __init__(self, coin_list: list) -> None:
      self.coin_list = coin_list
      self.page_sources = NavigateWebsite(url=r"https://finance.yahoo.com/cryptocurrencies", 
                                          coin_list=coin_list).get_page_source()

  def to_float(self, number: str) -> float:
    try:
      return float(''.join(number.split(',')))
    except:
      return 'NULL'

  def format_date(self, date: str) -> str:
    '''
    Format date 
    '''

    try:
      date = datetime.strptime(date, r'%b %d, %Y')
      date = datetime.strftime(r'%d-%m-%Y')
      return date
    except:
      return date

  def scarping(self) -> None:
    '''
    Get and store data of cryptocurrencies from website
    '''

    for coin in self.coin_list:
      soup = BeautifulSoup(self.page_sources[coin], 'lxml')

      symbol = soup.find('h1').text.split()[2][1:-1]
      tbody = soup.find('tbody').find_all('tr')

      data_list = []
      for data in tbody:
        row = [coin, symbol] + [coin_data.text for idx, coin_data in enumerate(data) if idx != 5]
        row[2] = self.format_date(row[2])
        row[3:] = map(self.to_float, row[3:])
        data_list.append(tuple(row))

      # Insert data to table
      table = MysqlDB(coin)
      table.create_table()
      table.insert(data_list)