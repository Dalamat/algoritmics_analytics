import psycopg2
import paths
import envs

#Set variables
database = envs.database
user = envs.db_user
password = envs.db_password
host = envs.db_host
port = envs.db_port

invoices_csv_path = paths.invoices_csv_path

# Connect to the database psql -h  -U  -d 
conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

# Create a cursor object
cur = conn.cursor()

try:
    # Start the transaction
    cur.execute("BEGIN;")

    # Truncate the table
    cur.execute('TRUNCATE public."invoices";')
    print('TRUNCATE TABLE INVOICES')

    # Copy data from the csv file to the invoices table
    with open(invoices_csv_path, 'r', encoding='utf-8') as f:
        cur.copy_expert('COPY public."invoices" FROM STDIN delimiter \';\' encoding \'utf-8\' csv header escape \'\\\' quote \'"\';', f)

    # Get the number of rows affected
    row_count = cur.rowcount
    print(f"COPY INVOICES {row_count}")

    # Commit the changes
    conn.commit()

except Exception as e:
    # If any errors occur, roll back the transaction
    conn.rollback()
    print(f"Error: {e}")
    print("ROLLBACK CHANGES INVOICES")

finally:
    # Close the connection
    cur.close()
    conn.close()