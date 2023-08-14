import mysql.connector
conn=mysql.connector.connect(host='localhost',password='Teja124015129',user='root')

if conn.is_connected():
                             print("connection established....")
                             
