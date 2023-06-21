import psycopg2
import paths
import envs
import sys

#Set variables
database = envs.database
user = envs.db_user
password = envs.db_password
host = envs.db_host
port = envs.db_port

csv_path = paths.students_csv_path

# Connect to the database psql -h  -U  -d 
conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
cur = conn.cursor()

try:
    # Start the transaction
    cur.execute("BEGIN;")

    # Truncate the table
    cur.execute('TRUNCATE public."students";')
    print('TRUNCATE TABLE STUDENTS')

    # Copy data from the csv file to the students table
    with open(csv_path, 'r', encoding='utf-8') as f:
        cur.copy_expert('COPY public."students" FROM STDIN delimiter \';\' encoding \'utf-8\' csv header escape \'\\\' quote \'"\';', f)

    # Get the number of rows affected
    row_count = cur.rowcount
    print(f"COPY STUDENTS {row_count}")

    # Commit the changes
    conn.commit()
    sys.exit(0)  # Exit with code 0 for a successful commit

except Exception as e:
    # If any errors occur, roll back the transaction
    conn.rollback()
    print(f"Error: {e}")
    print("ROLLBACK CHANGES STUDENTS")
    sys.exit(1)  # Exit with code 1 for a rollback

finally:
    # Close the connection
    cur.close()
    conn.close()