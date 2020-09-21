import sqlite3

conn = sqlite3.connect("botdata.db")

c = conn.cursor()
def insert_game_id(id,valo=None,rockstar=None,epic=None, steam=None,Quote="You can add your custom quote here by using $quote"):
    c.execute(f"insert into Gameid values({id},'{valo}','{rockstar}','{epic}','{steam}')")
    conn.commit()

def dele():
    c.execute("delete from Gameid")

def search_game_id(id):
    c.execute(f"select * from Gameid where id = {id}")
    r = c.fetchone()
    return r

def update_valo(valo,id):
    c.execute(f"update Gameid set valorant = '{valo}' where id = {id}")
    conn.commit()

def update_rockstar(rock,id):
    c.execute(f"update Gameid set rockstar = '{rock}' where id = {id}")
    conn.commit()

def update_epic(gameid,id):
    c.execute(f"update Gameid set epic = '{gameid}' where id = {id}")
    conn.commit()

def update_steam(gameid,id):
    c.execute(f"update Gameid set steam = '{gameid}' where id = {id}")
    conn.commit()

def update_quote(quote,id):
    c.execute(f"update Gameid set quote = '{quote}' where id = {id}")
    conn.commit()

# def show_data():
#     c.execute("Select * from test")
#     tdata = c.fetchall()
#     return tdata

# c.execute("Create table Gameid(id int primary key,valorant text, rockstar text, epic text, steam text)")
# c.execute("Alter table Gameid add Quote text")
conn.commit()
conn.close()