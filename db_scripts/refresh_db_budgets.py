import psycopg2
from algoritmics_analytics import paths
from algoritmics_analytics import envs
from log_config import logger


def refresh_db_budgets():

    #Set variables
    database = envs.database
    user = envs.db_user
    password = envs.db_password
    host = envs.db_host
    port = envs.db_port

    csv_path = paths.budgets_csv_path

    # Connect to the database psql -h  -U  -d 
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cur = conn.cursor()

    try:
        # Start the transaction
        cur.execute("BEGIN;")

        # Truncate the table
        cur.execute('TRUNCATE public."budget";')
        logger.info('TRUNCATE TABLE BUDGETS')

        # Copy data from the csv file
        with open(csv_path, 'r', encoding='utf-8') as f:
            cur.copy_expert('COPY public."budget" FROM STDIN delimiter \',\' encoding \'utf-8\' csv header escape \'\\\' quote \'"\';', f)

        # Get the number of rows affected
        row_count = cur.rowcount
        logger.info(f"COPY BUDGETS {row_count}")

        # Commit the changes
        conn.commit()
        return True

    except Exception as e:
        # If any errors occur, roll back the transaction
        conn.rollback()
        logger.error(f"Error during BUDGETS REFRESH: {e}")
        logger.warning("ROLLBACK CHANGES BUDGETS")
        return False

    finally:
        # Close the connection
        cur.close()
        conn.close()