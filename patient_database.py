import sqlite3
def createTable():
    connection = sqlite3.connect("govind.db")
    connection.execute("CREATE TABLE PATIENT(PATIENT_NAME TEXT NOT NULL, PATIENT_AGE INTEGER NOT NULL, PATIENT_GENDER CHAR(1) NOT NULL, PATIENT_AADHAR INTEGER NOT NULL UNIQUE, MEDICINES TEXT NOT NULL, DOCTOR_NAME TEXT NOT NULL, STATUS BOOLEAN, Shop_keeper STRING(30) REFERENCES SHOPKEEPER(ROLE),code INT(10))")
    connection.commit()
    result = connection.execute("DESC PATIENT")
    connection.close()
createTable()
    
                       
                       
