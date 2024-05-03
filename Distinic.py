import mysql.connector


conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Ameer@12345",
    database="new_schema"
)
cursor = conn.cursor()

def list_distinct_trainers():
    try:
  
        cursor.execute("SELECT DISTINCT trainer_id FROM Members")
        distinct_trainers = cursor.fetchall()
        return distinct_trainers
    except mysql.connector.Error as e:
        print("An error occurred:", e)
        return []


distinct_trainers = list_distinct_trainers()
print("Distinct trainers:", distinct_trainers)

conn.close()