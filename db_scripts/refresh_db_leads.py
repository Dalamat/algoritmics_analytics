import psycopg2
from algoritmics_analytics import paths
from algoritmics_analytics import envs


def refresh_db_leads():

    #Set variables
    database = envs.database
    user = envs.db_user
    password = envs.db_password
    host = envs.db_host
    port = envs.db_port

    csv_path = paths.leads_csv_path

    # Connect to the database psql -h  -U  -d 
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cur = conn.cursor()

    try:
        # Start the transaction
        cur.execute("BEGIN;")

        # Truncate the table
        cur.execute('TRUNCATE public."leads";')
        print('TRUNCATE TABLE LEADS')

        # Copy data from the csv file to the table
        with open(csv_path, 'r', encoding='utf-8') as f:
            # cur.copy_expert('COPY public."leads" FROM STDIN delimiter \',\' encoding \'utf-8\' csv header escape \'\\\' quote \'"\';', f)
            cur.copy_expert("""COPY public."leads" FROM STDIN WITH (FORMAT CSV, DELIMITER ',', ENCODING 'utf-8', HEADER, ESCAPE '"', QUOTE '"')""", f)

        # Get the number of rows affected
        row_count = cur.rowcount
        print(f"COPY LEADS {row_count}")

        # Commit the changes
        conn.commit()
        return True

    except Exception as e:
        # If any errors occur, roll back the transaction
        conn.rollback()
        print(f"Error: {e}")
        print("ROLLBACK CHANGES LEADS")
        return False

    finally:
        # Close the connection
        cur.close()
        conn.close()