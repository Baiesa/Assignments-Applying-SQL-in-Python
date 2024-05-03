import mysql.connector


conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Ameer@12345",
    database="new_schema"
)
cursor = conn.cursor()

def count_members_per_trainer():
    try:
     
        cursor.execute("SELECT trainer_id, COUNT(*) FROM Members GROUP BY trainer_id")
        members_per_trainer = cursor.fetchall()
        return members_per_trainer
    except mysql.connector.Error as e:
        print("An error occurred:", e)
        return []

members_per_trainer = count_members_per_trainer()
print("Members per trainer:", members_per_trainer)


conn.close()