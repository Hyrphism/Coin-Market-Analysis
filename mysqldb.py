import mysql.connector

class MysqlDB:
  def __init__(self, coin_name) -> None:
      self.cursor = None
      self.coin_name = coin_name

  def connect_db(self) -> None:
    '''
    Connect to database MySQL.
    '''

    try:
      self.mydb = mysql.connector.connect(
            host="localhost",
            database="mysqldb",
            user="root",
            password="ba4569852",
            port=3308
      )

      self.cursor = self.mydb.cursor()

    except Exception as e:
      print(e)

  def close_db(self) -> None:
    '''
    Close database.
    '''

    self.mydb.close()

  def create_table(self) -> None:
    '''
    Create new table by coin's name.
    Delete table if it already exists.
    '''

    try:
      self.cursor.execute(f"DROP TABLE IF EXISTS {self.coin_name}")

      self.cursor.execute(f'''CREATE TABLE {self.coin_name} (
            name VARCHAR(255),
            symbol VARCHAR(255),
            date DATE,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume FLOAT)'''
      )

      print(f'Create Table {self.coin_name} Successfully')

    except Exception as e:
      print(e)

  def insert(self, *data: list) -> None:
    '''
    Insert data to table.
    '''

    try:
      self.cursor.executemany(f'''INSERT INTO {self.coin_name} (name, symbol, date, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', data
      )

      self.mydb.commit()

      print(self.cursor.rowcount, "record inserted.")

    except Exception as e:
      print(e)

  def update(self) -> None:
    '''
    Update new data to table.
    '''
    
    pass