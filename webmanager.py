from flask import Flask, render_template, abort
import contactmanager as cm
import sqlite3
 

#conn = sqlite3.connect("contacts.db")
#c = conn.cursor()
#c.execute(""" create table numbers(
#        name text integer primary key,
#        number integer    
#            )""")

webmanager = Flask(__name__)

@webmanager.errorhandler(404)
def not_found(e):
    return render_template("404.html")
    #return "Sorry for your loss"

@webmanager.route('/addContact/<name>/<phoneNum>')
def addContact(name, phoneNum):
    conn = sqlite3.connect("contacts.db")
    count = cm.addContact(name, phoneNum, conn)
    return "Thank you! Added " + str(count) + " rows"

@webmanager.route('/deletename/<name>')
def deletename(name):
    conn = sqlite3.connect("contacts.db")
    count = cm.deleteName(name, conn)
    return "Thank you! Deleted " + str(count) + " rows"

@webmanager.route('/updatename/<name>/<phoneNum>')
def updatename(name, phoneNum):
    conn = sqlite3.connect("contacts.db")
    count = cm.updatename(name, phoneNum, conn)
    return "Thank you! Updated " + str(count) + " rows"

@webmanager.route('/searchname/<name>')
def searchname(name):
    conn = sqlite3.connect("contacts.db")
    count = cm.searchname(name, conn)
    return "name is "+ str(count[0])+ " and the number is " + str(count[1])

@webmanager.route('/searchnumber/<number>')
def searchnumber(number):
    conn = sqlite3.connect("contacts.db")
    count = cm.searchNumber(number, conn)
    return "name is "+ str(count[0])+ " and the number is " + str(count[1])

@webmanager.route('/selectAll')
def selectAll():
    conn = sqlite3.connect("contacts.db")
    res = cm.selectAll(conn)
    i = 1
    response = "| # | Name    |   Number |<br>"
    for values in res:
        response = response + "| " + str(i) + " | " + str(values[0])+ "   |   " + str(values[1]) + " |<br>"
        i = i + 1
    return response


if __name__ == "__main__":
    webmanager.run(debug=True)