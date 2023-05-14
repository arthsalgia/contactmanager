from flask import Flask, render_template, abort, render_template_string, request, redirect, url_for
import contactmanager as cm
import sqlite3
from werkzeug import exceptions

webmanager = Flask(__name__, static_folder='html')

class UnrecognizedParametersOrCombination(exceptions.HTTPException):
    code = 304
    description = 'Resource not modified!'

def handle_304(code):
    return render_template('304.html')


webmanager.register_error_handler(UnrecognizedParametersOrCombination, handle_304)
#conn = sqlite3.connect("contacts.db")
#c = conn.cursor()
#c.execute(""" create table numbers(
#        name text integer primary key,
#        number integer    
#            )""")

"""
@webmanager.route('/', methods = ['GET', 'POST'])
def trial():
    request_method = request.method
    if request.method == 'POST':
        print('-----------')
        print(request.form)
        print('-----------')
        return redirect(url_for('name'))
    return render_template('hello.html', request_method = request_method)    

@webmanager.route('/name')
def name():
    return 'name'
"""

@webmanager.errorhandler(404)
def not_found(e):
    return "Sorry, page not found"

@webmanager.route('/')
def homepage():
    return webmanager.send_static_file("index.html")

@webmanager.route('/addContact/v1/<name>', methods= ['POST'])
def addContact(name):
    phoneNum = request.form.get('phoneNum')
    conn = sqlite3.connect("contacts.db")
    count = cm.addContact(name, phoneNum, conn)
    return "Thank you! Added " + str(count) + " rows"

@webmanager.route('/addContact', methods= ['GET','POST'])
def addContactV2():
    name = request.form.get('name')
    phoneNum = request.form.get('phoneNum')
    conn = sqlite3.connect("contacts.db")
    searchname = cm.findname(name, conn) 
    if searchname: 
        return "Sorry this name is already in your contacts<br><a href='/html/update.html'>Click here to update the info</a><br><a href='/'>Home</a>"
    else: 
        count = cm.addContact(name, phoneNum, conn)
        return render_template("template.html", action="Added", count=count, name=name)
    #return "Thank you! Added " + str(count) + " rows" + "<br><a href='/'>Home</a>"

@webmanager.route('/deletename', methods= ['DELETE', 'POST'])
def deletename():
    name = request.form.get('name')
    conn = sqlite3.connect("contacts.db")
    count = cm.deleteName(name, conn)
    return "Thank you! Deleted " + str(count) + " rows" + "<br><a href='/'>Home</a>"

@webmanager.route('/updatename', methods= ['PATCH', "POST"])
def updatename():
    name = request.form.get('name')
    phoneNum = request.form.get('phoneNum')
    conn = sqlite3.connect("contacts.db")
    count = cm.updatename(name, phoneNum, conn)
    return "Thank you! Updated " + str(count) + " rows" + "<br><a href='/'>Home</a>"

@webmanager.route('/searchname', methods= ['GET'])
def searchname():
    name = request.args.get("name")
    print("got name ", name)
    conn = sqlite3.connect("contacts.db")
    records = cm.searchname(name, conn)
    if records:
        output = "found <b>" + str(len(records)) + "</b> records: <ol>"
        for entry in records:
            output += "<li> <b>" + entry[0] + "</b> " + str(entry[1]) + "</li>"
        return output + "</ol><br><a href='/'>Home</a>"
    else:
        return "Contact information not found for name " + name + "<br><a href='/'>Home</a>"

@webmanager.route('/searchnumber', methods= ['GET'])
def searchnumber():
    number = request.args.get('number')
    conn = sqlite3.connect("contacts.db")
    record = cm.searchNumber(number, conn)
    if record:
        return "name is "+ str(record[0])+ " and the number is " + str(record[1]) + "<br><a href='/'>Home</a>"
    else:
        return "Contact information not found for number " + number + "<br><a href='/'>Home</a>"

@webmanager.route('/list', methods= ['GET'])
def selectAll():
    conn = sqlite3.connect("contacts.db")
    res = cm.selectAll(conn)
    i = 1
    response = "| # | Name    |   Number |<br>"
    for values in res:
        response = response + "| " + str(i) + " | " + str(values[0])+ "   |   " + str(values[1]) + " |<br>"
        i = i + 1
    return response + "<br><a href='/'>Home</a>"


if __name__ == "__main__":
    webmanager.run(debug=True)