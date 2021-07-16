import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
    options.add_argument('--kiosk')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')

    return options

  def get_page_source(self) -> dict:
    '''
    Get page sources of coin lists 
    '''

    page_sources = {}

    start, end = self.get_input_date()

    chrome_options = self.get_options()
    
    # connect to website
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.get(self.url)

    # myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    for coin in self.coin_list:
      coin_name = coin + ' USD'

      # coin's page
      time.sleep(5)
      driver.find_element_by_xpath(f'//*[@title="{coin_name}"]').click()

      # historical data page
      time.sleep(5)
      driver.find_element_by_link_text('Historical Data').click()

      # input date
      time.sleep(5)
      driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div/div/span').click()

      start_date = driver.find_element_by_xpath('//*[@name="startDate"]')
      start_date.send_keys(start)
      start_date.send_keys(Keys.RETURN)

      end_date = driver.find_element_by_xpath('//*[@name="endDate"]')
      end_date.send_keys(end)
      end_date.send_keys(Keys.RETURN)

      driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button').click()

      # Scroll to the end of page
      for _ in range(50):
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)

      page_sources[coin] = driver.page_source

      # go back to main page
      for _ in range(3):
        driver.back()
        time.sleep(2)
    
    driver.quit()

    return page_sources