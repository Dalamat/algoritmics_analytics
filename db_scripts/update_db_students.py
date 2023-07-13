import psycopg2
from algoritmics_analytics import paths
from algoritmics_analytics import envs
from log_config import logger


def update_db_students():

    #Set variables
    database = envs.database
    user = envs.db_user
    password = envs.db_password
    host = envs.db_host
    port = envs.db_port

    csv_path = paths.students_filter_csv_path

    # Connect to the database psql -h  -U  -d 
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cur = conn.cursor()

    try:
        # Start the transaction
        cur.execute("BEGIN;")

        # Creating temp_students table
        cur.execute('''
            CREATE TABLE public."temp_students" (
                id int8 NULL,
                "name" text NULL,
                login text NULL,
                "password" text NULL,
                age text NULL,
                birthdate text NULL,
                parent_name text NULL,
                parent_phone text NULL,
                email text NULL,
                created text NULL,
                created_by text NULL,
                updated text NULL,
                geography text NULL,
                sales text NULL,
                group_id text NULL,
                group_name text NULL,
                description text NULL,
                enrolled_in_group text NULL,
                teacher text NULL,
                total_group_lessons text NULL,
                curator text NULL,
                tutor text NULL,
                client_manager text NULL,
                lessons_completed text NULL,
                group_start text NULL,
                group_type text NULL,
                group_status text NULL,
                student_status text NULL,
                lessons_attended text NULL DEFAULT 0,
                lessons_missed text NULL,
                lessons_missed_consecutive text NULL,
                attendance text NULL,
                total_invoiced float8 NULL,
                paid float8 NULL,
                lessons_paid int8 NULL,
                balance text NULL,
                amo_pipeline text NULL,
                deal_status text NULL,
                expelled text NULL,
                expulsion_reasons text NULL,
                office text NULL,
                course text NULL,
                course_type text NULL,
                skype text NULL,
                remote text NULL,
                "system" text NULL
            );
        ''')
    
        # Import the CSV data into the temporary table
        with open(csv_path, 'r', encoding='utf-8') as f:
            cur.copy_expert("COPY public.\"temp_students\" FROM STDIN delimiter ';' encoding 'utf-8' csv header escape '\\' quote '\"'", f)

        v_count = cur.rowcount
        logger.info(f"COPY STUDENTS {v_count}")

        # Update existing students
        cur.execute("""
            UPDATE public.students
            SET
                "name" = temp_students."name",
                login = temp_students.login,
                "password" = temp_students."password",
                age = temp_students.age,
                birthdate = temp_students.birthdate,
                parent_name = temp_students.parent_name,
                parent_phone = temp_students.parent_phone,
                email = temp_students.email,
                created = temp_students.created,
                created_by = temp_students.created_by,
                updated = temp_students.updated,
                geography = temp_students.geography,
                sales = temp_students.sales,
                group_id = temp_students.group_id,
                group_name = temp_students.group_name,
                description = temp_students.description,
                enrolled_in_group = temp_students.enrolled_in_group,
                teacher = temp_students.teacher,
                total_group_lessons = temp_students.total_group_lessons,
                curator = temp_students.curator,
                tutor = temp_students.tutor,
                client_manager = temp_students.client_manager,
                lessons_completed = temp_students.lessons_completed,
                group_start = temp_students.group_start,
                group_type = temp_students.group_type,
                group_status = temp_students.group_status,
                student_status = temp_students.student_status,
                lessons_attended = temp_students.lessons_attended,
                lessons_missed = temp_students.lessons_missed,
                lessons_missed_consecutive = temp_students.lessons_missed_consecutive,
                attendance = temp_students.attendance,
                total_invoiced = temp_students.total_invoiced,
                paid = temp_students.paid,
                lessons_paid = temp_students.lessons_paid,
                balance = temp_students.balance,
                amo_pipeline = temp_students.amo_pipeline,
                deal_status = temp_students.deal_status,
                expelled = temp_students.expelled,
                expulsion_reasons = temp_students.expulsion_reasons,
                office = temp_students.office,
                course = temp_students.course,
                course_type = temp_students.course_type,
                skype = temp_students.skype,
                remote = temp_students.remote,
                "system" = temp_students."system"
            FROM temp_students
            WHERE public.students.id = temp_students.id;
        """)

        v_count = cur.rowcount
        logger.info(f"UPDATED STUDENTS {v_count}")

        # Insert new students
        cur.execute("""
            INSERT INTO public.students (
                id, "name", login, "password", age, birthdate, parent_name, parent_phone,
                email, created, created_by, updated, geography, sales, group_id, group_name,
                description, enrolled_in_group, teacher, total_group_lessons, curator, tutor,
                client_manager, lessons_completed, group_start, group_type, group_status, student_status,
                lessons_attended, lessons_missed, lessons_missed_consecutive, attendance, total_invoiced,
                paid, lessons_paid, balance, amo_pipeline, deal_status, expelled, expulsion_reasons, office,
                course, course_type, skype, remote, "system"
            )
            SELECT
                temp_students.id, temp_students."name", temp_students.login, temp_students."password", temp_students.age, temp_students.birthdate, temp_students.parent_name, temp_students.parent_phone,
                temp_students.email, temp_students.created, temp_students.created_by, temp_students.updated, temp_students.geography, temp_students.sales, temp_students.group_id, temp_students.group_name,
                temp_students.description, temp_students.enrolled_in_group, temp_students.teacher, temp_students.total_group_lessons, temp_students.curator, temp_students.tutor,
                temp_students.client_manager, temp_students.lessons_completed, temp_students.group_start, temp_students.group_type, temp_students.group_status, temp_students.student_status,
                temp_students.lessons_attended, temp_students.lessons_missed, temp_students.lessons_missed_consecutive, temp_students.attendance, temp_students.total_invoiced,
                temp_students.paid, temp_students.lessons_paid, temp_students.balance, temp_students.amo_pipeline, temp_students.deal_status, temp_students.expelled, temp_students.expulsion_reasons, temp_students.office,
                temp_students.course, temp_students.course_type, temp_students.skype, temp_students.remote, temp_students."system"
            FROM temp_students
            WHERE NOT EXISTS (
                SELECT 1 FROM public.students
                WHERE public.students.id = temp_students.id
            );
        """)

        v_count = cur.rowcount
        logger.info(f"INSERTED STUDENTS {v_count}")

        # Drop temp_students table
        cur.execute('DROP TABLE public."temp_students";')

        # Commit the transaction
        conn.commit()
        return True
    
    except Exception as e:
        # If any errors occur, roll back the transaction
        conn.rollback()
        logger.error(f"Error during STUDENTS UPDATE: {e}")
        logger.warning("ROLLBACK CHANGES STUDENTS")
        return False
    
    finally:
        # Close the connection
        cur.close()
        conn.close()