import sqlite3
import teen

def initDb():
  #Initialize a new database to store the teen's details
  conn = sqlite3.connect('teen.db')
  conn.execute("PRAGMA foreign_keys = 1")
  c = conn.cursor()
  sql = '''
  CREATE TABLE IF NOT EXISTS basicInfo (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    username TEXT,
    password TEXT);
  CREATE TABLE IF NOT EXISTS dataInfo (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    budget INTEGER,
    earning INTEGER,
    item_name TEXT,
    item_value INTEGER,
    classify TEXT,
    UserID INTEGER NOT NULL,
    FOREIGN KEY (UserID)
    REFERENCES BasicInfo (UserID));
    '''
  c.executescript(sql)
  conn.commit()
  conn.close()
  #conn = sqlite3.connect('teen.db')
  #c = conn.cursor()
  #c.execute(sql_data)
  #conn.commit()
  #conn.close()


def log(teen):
  '''
  logs the expenditure in the database.
    self.name: string,
    self.email: string,
    self.username: string,
    self.password: string
  '''

  data = (teen.name, teen.email, teen.username, teen.password)
  print(data,"data in dbconnect")
  conn = sqlite3.connect('teen.db')
  c = conn.cursor()
  sql = 'INSERT INTO basicInfo  (name,email,username,password) VALUES (?,?,?,?)'
  c.execute(sql,(teen.name,teen.email,teen.username,teen.password))
  print("inserting in db")
  conn.commit()
  conn.close()
  
def DataLog(data):
  data_set = (data.monthly_budget, data.monthly_earning, data.item_name, data.item_value, data.classify)
  print(data_set, 'printing data from Add Data')
  conn = sqlite3.connect('teen.db')
  #conn.execute("PRAGMA foreign_keys = 1")
  c= conn.cursor()
  sql = 'INSERT INTO dataInfo(budget, earning, item_name, item_value, classify) VALUES (?,?,?,?,?)'
  c.execute(sql, (data.monthly_budget, data.monthly_earning, data.item_name, data.item_value, data.classify))
  print("creating DataLog table")
  conn.commit()
  conn.close()
  
  
def view(teen, name=None):
  '''
  returns the teens available in table
  '''
  conn = sqlite3.connect('teen.db')
  c = conn.cursor()
  if name:
    print("reached if")
    sql = '''
    SELECT * FROM basicInfo WHERE name = '{}'
    '''.format(name)
  else:
    print("reached else block")
    sql = '''
      SELECT * FROM basicInfo
      '''.format(name)
    c.execute(sql)
    results = c.fetchall()

    conn.close()

    return results

def login(username,password):
  #print(username, password)
  conn = sqlite3.connect('teen.db')
  c = conn.cursor()
  sql1 = '''
  SELECT * FROM basicInfo WHERE username = '{}' AND password='{}'
  '''.format(username,password)
  c.execute(sql1)
  results = c.fetchall()
  conn.close()

  return results



#def add_data(teen)