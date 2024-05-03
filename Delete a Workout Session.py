import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Ameer@12345",
    database="new_schema"
)
cursor = conn.cursor()

def delete_workout_session(session_id):
    try:

        cursor.execute("SELECT * FROM WorkoutSessions WHERE session_id = %s", (session_id,))
        existing_session = cursor.fetchone()
        if not existing_session:
            print("Error: Session ID does not exist.")
            return


        cursor.execute("DELETE FROM WorkoutSessions WHERE session_id = %s", (session_id,))
        conn.commit()
        print("Workout session deleted successfully.")
    except mysql.connector.Error as e:
        print("An error occurred:", e)


delete_workout_session(1)  

# Close the connection
conn.close()