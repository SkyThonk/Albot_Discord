import sqlite3

conn = sqlite3.connect("botdata.db")

c = conn.cursor()
def insert_data(data):
    c.execute(f"insert into test values('{data}')")
    conn.commit()

def show_data():
    c.execute("Select * from test")
    tdata = c.fetchall()
    return tdata