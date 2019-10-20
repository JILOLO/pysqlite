# Inserting into a Database with SQLite

import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS myTable(unix REAL, datestamp TEST, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(881101,'2019-10-19','python',6)")
    conn.commit()
    c.close()

create_table()
data_entry()

conn.close()