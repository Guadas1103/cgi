#!C:/Python311/python.exe
import mysql.connector
import os
import cgi
import cgitb
cgitb.enable()
print("Content-type: text/html")
print()
metodo = os.environ["REQUEST_METHOD"]

if metodo == "POST":
    datos = cgi.FieldStorage()
    email = datos.getvalue("email")
    password = datos.getvalue("password")
    name = datos.getvalue("name")
    avatar = datos.getvalue("avatar")
    role = datos.getvalue("role")

    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='foro')
    cur = con.cursor()
    sql = "UPDATE users SET password=sha1('{}'), name='{}', avatar='{}', role='{}' WHERE email='{}'".format( password, name, avatar, role, email)
    cur.execute(sql)
    con.commit()
    con.close()
    print("<h1>Usuario Actualizado</h1>")
else:
    print("<h1>Metodo no Permitido</h1>")