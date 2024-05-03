import mysql.connector


conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Ameer@12345",
    database="new_schema"
)
cursor = conn.cursor()

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
    
        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        existing_member = cursor.fetchone()
        if not existing_member:
            print("Error: Member does not exist.")
            return


        cursor.execute("INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)", 
                       (member_id, date, duration_minutes, calories_burned))
        conn.commit()
        print("Workout session added successfully.")
    except mysql.connector.Error as e:
        print("An error occurred:", e)


add_workout_session(1, '2024-05-03', 244, 300)  


conn.close()