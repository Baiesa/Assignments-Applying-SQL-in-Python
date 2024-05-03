import mysql.connector


conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Ameer@12345",
    database="new_schema"
)
cursor = conn.cursor()

def add_member(id, name, age, trainer_id):
    try:

        cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
        existing_member = cursor.fetchone()
        if existing_member:
            print("Error: Member ID already exists.")
            return

  
        cursor.execute("INSERT INTO Members VALUES (%s, %s, %s, %s)", (id, name, age, trainer_id))
        conn.commit()
        print("Member added successfully.")
    except mysql.connector.Error as e:
        print("An error occurred:", e)


add_member(1, 'John Doe', 30, 101)
add_member(2, 'Mikel', 43, 100)
add_member(3, 'Koly', 21, 104)
add_member(4, 'Nail', 24, 105)




conn.close()