import contactmanager as cm
import sqlite3

conn = sqlite3.connect("contacts.db")

#c = conn.cursor()
#c.execute(""" create table numbers(
#        name text integer primary key,
#        number integer   
#            )""")

end = ""
while end != "continue": 
    print ("""
        What would you like to do: 
        1: Add a new number
        2: Delete a Contact
        3: Update a number
        4: Find a contact by name
        5: Find a contact by number
        6: View all numbers
        7: End
        """)
    x = input('Please enter the number of what you want: ')

    if x == "1" or x == "one" or x == "One":
        addname = str(input("Enter the name of the person you would like to add: "))
        number = str(input("Enter the number of the person you would like to add: "))
        count = cm.addContact(addname, number, conn)
        print("\n Processing... ")
        print("Saved " + str(count) + " rows")
    
    elif x == "2" or x == "two" or x =="Two":
        delname = str(input("Enter the name of the person you would like to delete: "))
        count = cm.deleteName(delname, conn)
        print("\nProcessing... ")
        print("Deleted " + str(count) + " rows")
            
    elif x == "3" or x == "three" or x == "Three":
        updatename = str(input("Enter the name of the person you would like to update: "))
        updatenumber = str(input("Enter the number of the person you would like the name to update to: "))
        count = cm.updatename(updatename, updatenumber, conn)
        print("\nProcessing... ")
        print("Updated " + str(count) + " rows")

    elif x == "4" or x == "four" or x == "Four":
        findname = str(input("Enter the name of the person you would like to find: "))
        record = cm.searchname(findname, conn)
        print("\nname is "+ str(record[0])+ " and the number is " + str(record[1]))

    elif x == "5" or x == "five" or x == "Five":
        findnumber = str(input("Enter the number of the person you would like to find: "))
        record = cm.searchNumber(findnumber, conn)
        print("\nname is "+ str(record[0])+ " and the number is " + str(record[1]))

    elif x == "6" or x == "six" or x == "Six":
        print("\n|-----------------------|")
        print("| # | Name    |   Number |")
        print("|-----------------------|")
        res = cm.selectAll(conn)
        i = 1
        for values in res:
            print( "| " + str(i) + " | " + str(values[0])+ "   |   " + str(values[1]) + " | ")
            i = i + 1
        print("|-----------------------|")

    elif x == "7" or x == "seven" or x == "Seven":
        print("Thank you for using phonebook.")
        break
    else:
        print("You typed something unexpected please try again ")

conn.close()
