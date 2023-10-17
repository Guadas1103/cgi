#!C:/Python311/python.exe
import mysql.connector
import os
import cgi
import cgitb
cgitb.enable()
print("Content-type: text/html")
print()
print("<h1>Consulta Usuarios</h1>")
print("<hr>")

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='foro')
cur = con.cursor()
sql = "SELECT * FROM users"
cur.execute(sql)
for (email, password, name, avatar, role) in cur:
    print("{},{},{},{},{}".format(email, password, name, avatar, role))
    print("<br>")
