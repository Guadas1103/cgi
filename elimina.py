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
   

    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='foro')
    cur = con.cursor()
    sql = "DELETE FROM users WHERE email='{}'".format(email)
   # sql = f"DELETE FROM users WHERE email='{email}'"
    cur.execute(sql)
    con.commit()
    con.close()
    print("<h1>Usuario Eliminado</h1>")
else:
    print("<h1>Metodo no Permitido</h1>")