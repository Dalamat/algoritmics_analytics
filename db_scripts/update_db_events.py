import psycopg2
from algoritmics_analytics import paths
from algoritmics_analytics import envs
from log_config import logger


def update_db_events():

    #Set variables
    database = envs.database
    user = envs.db_user
    password = envs.db_password
    host = envs.db_host
    port = envs.db_port

    csv_path = paths.events_filter_csv_path

    # Connect to the database psql -h  -U  -d 
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cur = conn.cursor()
    try:
        # Start the transaction
        cur.execute("BEGIN;")

        # Step 1: Create a temporary table with the same structure as the main table
        cur.execute('''
            CREATE TABLE public."temp_events" (
            next_lesson_time text NULL,
            next_lesson_number text NULL,
            next_lesson text NULL,
            id text NULL,
            name text NULL,
            venue text NULL,
            geography text NULL,
            lesson_status text NULL,
            participants text NULL,
            attended_students int8 NULL,
            paid_students text NULL,
            enrolled_students int8 NULL,
            expelled_students int8 NULL,
            amc_paid_after_master int8 NULL,
            expelled_and_transferred int8 NULL,
            first_lesson text NULL,
            "day" text NULL,
            teacher text NULL,
            curator text NULL,
            tutor text NULL,
            client_manager text NULL,
            priority text NULL,
            group_type text NULL,
            status text NULL,
            course text NULL,
            course_type text NULL,
            availability text NULL,
            created text NULL,
            created_by text NULL
            );
        ''')

        # Step 2: Import the CSV data into the temporary table
        with open(csv_path, 'r', encoding='utf-8') as f:
            cur.copy_expert("COPY public.\"temp_events\" FROM STDIN delimiter ';' encoding 'utf-8' csv header escape '\\' quote '\"'", f)

        v_count = cur.rowcount
        logger.info(f"COPY EVENTS {v_count}")

        # Step 3: Delete the rows in the main table that have matching IDs with the temporary table
        cur.execute('''
            DELETE FROM public.events
            WHERE id IN (SELECT id FROM public."temp_events");
        ''')

        v_count = cur.rowcount
        logger.info(f"DELETE EVENTS {v_count}")

        # Step 4: Insert the data from the temporary table into the main table
        cur.execute('''
            INSERT INTO public.events (
                next_lesson_time, next_lesson_number, next_lesson, id, name, venue, geography, lesson_status, participants,
                attended_students, paid_students, enrolled_students, expelled_students, amc_paid_after_master, expelled_and_transferred,
                first_lesson, "day", teacher, curator, tutor, client_manager, priority, group_type, status, course, course_type,
                availability, created, created_by
            )
            SELECT
                next_lesson_time, next_lesson_number, next_lesson, id, name, venue, geography, lesson_status, participants,
                attended_students, paid_students, enrolled_students, expelled_students, amc_paid_after_master, expelled_and_transferred,
                first_lesson, "day", teacher, curator, tutor, client_manager, priority, group_type, status, course, course_type,
                availability, created, created_by
            FROM public."temp_events";
        ''')

        v_count = cur.rowcount
        logger.info(f"INSERT EVENTS {v_count}")

        # Step 5: Drop the temporary table
        cur.execute('''
            DROP TABLE public."temp_events";
        ''')

        # Commit the transaction
        conn.commit()
        return True

    except Exception as e:
        # If any errors occur, roll back the transaction
        conn.rollback()
        logger.error(f"Error during EVENTS UPDATE: {e}")
        logger.warning("ROLLBACK CHANGES EVENTS")
        return False

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()