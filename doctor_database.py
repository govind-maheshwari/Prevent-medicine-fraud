import sqlite3
def createTable():
    connection = sqlite3.connect("govind.db")
    connection.execute("CREATE TABLE DOCTOR(ROLE TEXT NOT NULL, USERNAME TEXT NOT NULL UNIQUE, NAME TEXT NOT NULL, EMAIL TEXT NOT NULL, MOBILE_NO INTEGER NOT NULL, PASSWORD TEXT NOT NULL,CONFIRM_PASSWORD TEXT NOT NULL)")
    #connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?)",('DOCTOR','go840159','Govind Maheshwari','govindmaheshwari159@gmail.com','8409108489','1234','1234'))
    connection.commit()
    result = connection.execute("DESC DOCTOR")
    connection.close()
createTable()
