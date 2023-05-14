import sqlite3

# addContact stores (name and phoneNum) to the SQlite file
# returns False if user already exists else True

def addContact(name, phoneNum, conn):
    cursor = conn.cursor()
    cursor.execute("insert into numbers (name, number) values ('" + name + "','" +  phoneNum + "')")
    conn.commit()
    return cursor.rowcount

def deleteName (name, conn):
    cursor = conn.cursor()
    cursor.execute("delete from numbers where name = '" + name +"' ")
    conn.commit()
    return cursor.rowcount

def updatename (name, number, conn):
    cursor = conn.cursor()
    cursor.execute("update numbers set number = '" + number+ "' where name = '" + name+ "' ")
    conn.commit()
    return cursor.rowcount

def searchname (name, conn):
    cursor = conn.cursor()
    res = cursor.execute("select name, number from numbers where name like '%" +name+ "%'")
    return res.fetchall()

def findname (name, conn):
    cursor = conn.cursor()
    res = cursor.execute("select  name from numbers where  upper('" + name + "') like upper(name)")
    return res.fetchone()

def searchNumber (number, conn):
    cursor = conn.cursor()
    res = cursor.execute("select name, number from numbers where number like '%" + number+ "%'")
    return res.fetchone()

def selectAll (conn):
    cursor = conn.cursor()
    res = cursor.execute("select name, number from numbers")
    return res.fetchall()
