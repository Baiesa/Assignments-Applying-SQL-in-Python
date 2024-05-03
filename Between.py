import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
     host="127.0.0.1",
    user="root",
    password="Ameer@12345",
    database="new_schema"
)
cursor = conn.cursor()

def get_members_in_age_range(start_age, end_age):
    try:

        cursor.execute("SELECT * FROM Members WHERE age BETWEEN %s AND %s", (start_age, end_age))
        members_in_age_range = cursor.fetchall()
        return members_in_age_range
    except mysql.connector.Error as e:
        print("An error occurred:", e)
        return []

members_in_age_range = get_members_in_age_range(25, 30)
print("Members in age range:", members_in_age_range)

conn.close()