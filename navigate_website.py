from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class NavigateWebsite:
  def __init__(self, url: str, coin_list: list) -> None:
    self.url = url
    self.coin_list = coin_list

  def get_input_date(self) -> list:
    '''
    Input date to website
    '''

    end = datetime.today().date() - timedelta(days=1)
    start = (end - timedelta(days=365)).strftime(r'%d-%m-%Y')
    end = end.strftime(r'%d-%m-%Y')

    return [start, end]

  def get_options(self):
    '''
    Add options 
    '''

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')

    return options

  def get_driver(self):
    '''
    Navigate to website
    '''

    chrome_options = self.get_options()

    driver = webdriver.Chrome(options=chrome_options,
                              executable_path=r'..\\Project\\WebDriver\\chromedriver.exe')
    driver.get(self.url)

    return driver

  def get_page_source(self) -> list:
    '''
    Getting and storing page sources of coin lists to a list
    '''

    page_sources = {}

    start, end = self.get_input_date()
    driver = self.get_driver()

    for coin in self.coin_list:
      coin_name = coin + 'USD'

      driver.find_element_by_xpath(f'//*[@title="{coin_name}"]').click()
      driver.implicitly_wait(1)

      historial_data_coin = driver.find_element_by_link_text('Historical Data').click()
      driver.implicitly_wait(1)

      input_date = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div/div/span').click()

      start_date = driver.find_element_by_xpath('//*[@name="startDate"]')
      start_date.send_keys(start)
      start_date.send_keys(Keys.RETURN)

      end_date = driver.find_element_by_xpath('//*[@name="endDate"]')
      end_date.send_keys(end)
      end_date.send_keys(Keys.RETURN)

      apply_button = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button').click()

      # Scroll to the end of page
      for _ in range(50):
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)

      page_sources[coin] = driver.page_source

      driver.find_element_by_xpath('//*[@title="Cryptocurrencies"]').click()

    return page_sources