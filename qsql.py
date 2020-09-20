import sqlite3

conn = sqlite3.connect("botdata.db")

c = conn.cursor()

# c.execute("Create table test(msg text)")
def insert_data(data):
    c.execute(f"insert into test values('{data}')")

conn.commit()
conn.close()