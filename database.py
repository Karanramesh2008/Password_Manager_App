import sqlite3

s='vault.db'
conn=sqlite3.connect(s)
cursor=conn.cursor()
def createdb():
    cursor.execute("CREATE TABLE IF NOT EXISTS master (hash TEXT NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, site TEXT,username TEXT, password TEXT)")
    conn.commit()
    return


def is_master_set()->bool:
    cursor.execute("SELECT * FROM master")
    f=cursor.fetchall()
    if f:
        return True
    else:
        return False

def save_master_hash(hash:str):
    cursor.execute("INSERT INTO master (hash) VALUES(?)",(hash,))
    conn.commit()
    return

def get_master_hash()->str:
    cursor.execute("SELECT * FROM master")
    d=cursor.fetchone()
    return d[0]
    
def add_password(site:str,username:str,encryp:str):
    cursor.execute("INSERT INTO passwords (site,username,password) VALUES(?,?,?)",(site,username,encryp))
    conn.commit()

def get_all_password()->list:
    cursor.execute("SELECT * FROM passwords")
    return cursor.fetchall()

def search_password(site:str)->list:
    cursor.execute("SELECT * FROM passwords WHERE site LIKE ?",(f"%{site}%",))
    return cursor.fetchall()
    

def delete_password(site:str):
    cursor.execute("DELETE FROM passwords WHERE site LIKE ?",(f"%{site}%",))
    conn.commit()
    print("Successfully Deleted.")
