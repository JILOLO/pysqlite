import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')


conn = sqlite3.connect('mydb.db')
c = conn.cursor()

#install SQLite3 browser, you'll see the content with it
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS myTable(unix REAL,datestamp TEXT,keyword TEXT,value REAL)")

def data_entry():
    c.execute("INSERT INTO myTable VALUES(881101,'2019-10-19','python',6)")
    conn.commit()    

def dynamic_data_entry():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO myTable(unix,datestamp,keyword,value) VALUES(?,?,?,?)", (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM myTable')
    #c.execute('SELECT * FROM myTable WHERE value = 6')
    #c.execute('SELECT * FROM myTable WHERE unix > 20')
    #c.execute('SELECT value, datestamp FROM myTable WHERE unix > 20')
    data = c.fetchall()
    #print(data)

    for row in data:
        print(row)
        #print(row[0])
    ##another equivalent syntax
    #[print(row) for row in data]    

def graph_data():
    '''
    Simply parse part of the table to plot 
    '''
    c.execute('SELECT datestamp, value FROM myTable')
    data = c.fetchall()
    dates = []
    values = []
    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])
    plt.plot_date(dates, values, '-')
    plt.show()

def del_and_update():
    #update things
    c.execute('UPDATE myTable SET value = 99 WHERE value = 6')
    conn.commit()
    #delete things
    c.execute('DELETE FROM myTable WHERE value = 99')
    conn.commit()


'''
tests
'''
create_table()
#data_entry()

#dynamically enter a row with time
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)

#graph_data()

del_and_update()
read_from_db()

c.close()
conn.close()




