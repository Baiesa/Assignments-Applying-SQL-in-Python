import mysql.connector


conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Ameer@12345",
    database="new_schema"
)
cursor = conn.cursor()

def update_member_age(member_id, new_age):
    try:
    
        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        existing_member = cursor.fetchone()
        if not existing_member:
            print("Error: Member does not exist.")
            return

 
        cursor.execute("UPDATE Members SET age = %s WHERE id = %s", (new_age, member_id))
        conn.commit()
        print("Member age updated successfully.")
    except mysql.connector.Error as e:
        print("An error occurred:", e)


update_member_age(1, 35)

# Close the connection
conn.close()