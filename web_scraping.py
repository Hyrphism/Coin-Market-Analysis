import urllib
import urllib.request
import re

from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class NavigateWebsite:
  def __init__(self, url: str, coin_list: list) -> None:
    self.url = url
    self.coin_list = coin_list
    self.chrome_options = Options()

  def get_input_date(self) -> None:
    self.end = datetime.today().date() - timedelta(days=1)
    self.start = (self.end - timedelta(days=365)).strftime(r'%d-%m-%Y')
    self.end = self.end.strftime(r'%d-%m-%Y')

  def get_options(self) -> None:
    self.chrome_options.add_argument('--ignore-certificate-errors')
    self.chrome_options.add_argument('--incognito')
    self.chrome_options.add_argument('--headless')

  def get_driver(self) -> None:
    self.driver = webdriver.Chrome(options=self.chrome_options,
                                   executable_path=r'..\\Project\\WebDriver\\chromedriver.exe')
    self.driver.get(self.url)

  def get_page_source(self) -> list:
    page_sources = {}

    self.get_input_date()
    self.get_options()
    self.get_driver()

    for coin in self.coin_list:
      self.driver.find_element_by_xpath(f'//*[@title="{coin}"]').click()
      self.driver.implicitly_wait(1)

      historial_data_coin = self.driver.find_element_by_link_text('Historical Data').click()

      self.driver.implicitly_wait(1)
      input_date = self.driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div/div/span').click()

      start_date = self.driver.find_element_by_xpath('//*[@name="startDate"]')
      start_date.send_keys(self.start)
      start_date.send_keys(Keys.RETURN)

      end_date = self.driver.find_element_by_xpath('//*[@name="endDate"]')
      end_date.send_keys(self.end)
      end_date.send_keys(Keys.RETURN)

      apply_button = self.driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button').click()

      # Scroll to the end of page
      for _ in range(50):
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)

      page_sources[coin] = self.driver.page_source

      self.driver.find_element_by_xpath('//*[@title="Cryptocurrencies"]').click()

      