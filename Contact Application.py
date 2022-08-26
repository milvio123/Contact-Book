from re import A
from sqlite3 import connect
from typing import final
import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user = user_name,
            password = user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


pw = #Put your MySQL Terminal password 

#Database name 
db = 'contactdb'

connection = create_server_connection("localhost", "root", pw)

def create_database(connection,query):
    cursor = connection.cursor()
    try: 
        cursor.execute(query)
        print("Databse create succesfully")
    except Error as err: 
        print(f"Error: '{err}'")
create_database_query = "Create database contactdb"
create_database(connection,create_database_query)

#Connect to databse

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL databse connection succesful")
    except Error as err:
         print(f"Error: '{err}'")
    return connection



userchoice = int(input("Press 1 to sign up or 2 to sign in"))

if userchoice==1:
    def execute_query_createLogin(connection, query):
        cursor = connection.cursor()
        username = input("Username" )
        password = input("Password")
        record = (username, password)
        
        try:
            cursor.execute(query, record)
            connection.commit()
            print("Query was succesful")
        except Error as err:
            print(f"Error: '{err}'")
            connection.commit()
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
     
    edit_user_column = """
        INSERT INTO Userslogin(
        Usernames,
        Passwords)
        VALUES (%s, %s)
    """

    connection = create_db_connection("localhost", "root", pw, db)
    execute_query_createLogin(connection, edit_user_column)


elif userchoice == 2:
    def execute_query_checkLogin(connection, query):
        cursor = connection.cursor(buffered=True)
        global usernamefrom 
        usernamefrom = input("Username" )
        global passwordfrom 
        passwordfrom = input("Password")
        record = (usernamefrom, passwordfrom)

        try:
            cursor.execute(query, record)
            connection.commit()
            result = cursor.fetchall()
            global trueresult
            trueresult = result[0][0]
            print(trueresult)
        except Error as err:
            print(f"Error: '{err}'")
            connection.commit()
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    check_login_column = """
        SELECT ISNULL((SELECT Usernames FROM UsersLogin WHERE Usernames = %s AND Passwords = %s));
    """
    connection = create_db_connection("localhost", "root", pw, db)

    execute_query_checkLogin(connection, check_login_column)


def loginSuccess(connection,query):
    cursor = connection.cursor(buffered=True)
    record = (usernamefrom,passwordfrom)
    if trueresult==0:
        print("Succesfully login")
        try:
            cursor.execute(query, record)
            connection.commit()
            aresult = cursor.fetchall()
            global realresult
            actualresult = aresult
            realresult = actualresult[0][0]
        except Error as err:
            print(f"Error: '{err}'")
            connection.commit()
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()     
    elif trueresult==1:
        print("Please try again")

get_Id = """
SELECT ID FROM UsersLogin WHERE Usernames = %s AND Passwords = %s
"""
connection = create_db_connection("localhost", "root", pw, db)
loginSuccess(connection,get_Id)

userinput = 0
while userinput!=4:
    userinput = int(input("Press 1 to Add Contact, Press 2 to Edit Contact, Press 3 to Delete Contact, Press 4 to exit"))
    if userinput==1:
        def usersadd(connection,query):
            cursor = connection.cursor(buffered=True)
            global Contactname
            Contactname = input("Enter the name of the contact you want to add: ")
            global Contactnumber
            Contactnumber = int(input("Enter the number of the contact you want to add"))
            global Contactemail
            Contactemail = input("Enter the email of the contact you want to add: ")
            record = (realresult, Contactname,Contactnumber, Contactemail )
            try:
                cursor.execute(query, record)
                connection.commit()
            except Error as err:
                print(f"Error: '{err}'")
                connection.commit()
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()                  
        add_contactinformation = """
                        INSERT INTO UsersContacts(
                        id,
                        ContactName,
                        ContactNumber,
                        ContactEmail)
                        VALUES (%s, %s, %s,%s)
                """
        connection = create_db_connection("localhost", "root", pw, db)
        usersadd(connection, add_contactinformation)

    if userinput == 2:
        usertodo = int(input("Press 1 to edit name, Press 2 to edit number, Press 3 to edit email"))
        if(usertodo==1):
            def usereditname(connection,query):
                Contacttoedit = input("Enter the name of the contact you want to edit: ")
                global WhatToEditTo
                WhatToEditTo = input("What do you want to edit to")
                record = (WhatToEditTo,Contacttoedit, realresult)
                cursor = connection.cursor(buffered=True)
                try:
                    cursor.execute(query, record)
                    connection.commit()
                except Error as err:
                    print(f"Error: '{err}'")
                    connection.commit()
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()

            edit_contactinformation = """
                        UPDATE UsersContacts
                        SET ContactName = %s
                        WHERE ContactName = %s AND id = %s
                    """
            connection = create_db_connection("localhost", "root", pw, db)
            usereditname(connection, edit_contactinformation)
        if(usertodo==2):
            def usereditnumber(connection,query):
                Contacttoedit = input("Enter the name of the contact you want to edit: ")
                global WhatToEditTo
                WhatToEditTo = input("What do you want to edit the number to")
                record = (WhatToEditTo,Contacttoedit, realresult)
                cursor = connection.cursor(buffered=True)
                try:
                    cursor.execute(query, record)
                    connection.commit()
                except Error as err:
                    print(f"Error: '{err}'")
                    connection.commit()
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()

            edit_contactnumber = """
                        UPDATE UsersContacts
                        SET ContactNumber = %s
                        WHERE ContactName = %s AND id = %s
                    """
            connection = create_db_connection("localhost", "root", pw, db)
            usereditnumber(connection, edit_contactnumber)
        if(usertodo==3):
            def usereditemail(connection,query):
                Contacttoedit = input("Enter the name of the contact you want to edit: ")
                global WhatToEditTo
                WhatToEditTo = input("What do you want to edit the email to")
                record = (WhatToEditTo,Contacttoedit, realresult)
                cursor = connection.cursor(buffered=True)
                try:
                    cursor.execute(query, record)
                    connection.commit()
                except Error as err:
                    print(f"Error: '{err}'")
                    connection.commit()
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()

            edit_contactemail = """
                        UPDATE UsersContacts
                        SET ContactEmail = %s
                        WHERE ContactName = %s AND id = %s
                    """
            connection = create_db_connection("localhost", "root", pw, db)
            usereditemail(connection, edit_contactemail)
    if userinput==3:
        def userdelete(connection,query):
            Contacttoedit = input("Enter the name of the contact you want to delete: ")
            record = (Contacttoedit, realresult)
            cursor = connection.cursor(buffered=True)
            try:
                cursor.execute(query, record)
                connection.commit()
            except Error as err:
                print(f"Error: '{err}'")
                connection.commit()
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()                  
        add_contactinformation = """
                        DELETE FROM UsersContacts
                        WHERE ContactName = %s AND id = %s
                """
        connection = create_db_connection("localhost", "root", pw, db)
        userdelete(connection, add_contactinformation)







