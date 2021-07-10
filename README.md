# Coin-Market-Analysis

Scraping historical data of cryptocurrencies from website then store to the MySQL database, analyze and predict the next 30 days.

## Set up driver for selenium
1.  Check you have installed latest version of chrome brwoser -> `chromium-browser -version`

2.  If not, install latest version of chrome -> `sudo apt-get install chromium-browser`

3.  Get appropriate version of chrome driver from [here](https://chromedriver.storage.googleapis.com/index.html)

4.  Unzip the chromedriver.zip -> `unzip chromedriver.zip`

5.  Move the file to /usr/bin directory `sudo mv chromedriver /usr/bin`

6.  Go to /usr/bin directory `cd /usr/bin`

7.  Now, you would need to run something like `sudo chmod a+x chromedriver` to mark it executable.

8.  Finally you can execute the code.

## Start analyze 
1.  Run docker-compose.yml to install all packages and create a new database -> `docker-compose up` 

2.  Run main.py to get data from website and store to the database.

3.  Run jupyter notebook to analyze and predict price of cryptocurrencies. 