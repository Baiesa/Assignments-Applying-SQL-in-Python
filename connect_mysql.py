
import mysql.connector
from mysql.connector import Error

db_name = "new_schema" 
host = "127.0.0.1"
user = "root"
password = "Ameer@12345"
  
try:
    conn = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    if conn.is_connected():
        print("Connected to MYSQL database successfully.")
except Error as e:
    print(f"Error: {e}")
finally:
    if conn and conn.is_connected():
        conn.close()
        print("MYSQL connection is closed")
        



