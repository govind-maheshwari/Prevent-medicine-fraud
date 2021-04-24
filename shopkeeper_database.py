import sqlite3
def createTable():
    connection = sqlite3.connect("govind.db")
    connection.execute("CREATE TABLE SHOPKEEPER(ROLE TEXT NOT NULL, USERNAME TEXT NOT NULL UNIQUE, NAME TEXT NOT NULL, EMAIL TEXT NOT NULL, MOBILE_NO INTEGER NOT NULL, PASSWORD TEXT NOT NULL, CONFIRM_PASSWORD TEXT NOT NULL)")
    connection.commit()
    result = connection.execute("DESC SHOPKEEPER")
    connection.close()
createTable()
