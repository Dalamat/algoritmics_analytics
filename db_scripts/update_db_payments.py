import psycopg2
from algoritmics_analytics import paths
from algoritmics_analytics import envs
from log_config import logger


def update_db_payments():

    #Set variables
    database = envs.database
    user = envs.db_user
    password = envs.db_password
    host = envs.db_host
    port = envs.db_port

    csv_path = paths.payments_filter_csv_path

    # Connect to the database psql -h  -U  -d 
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cur = conn.cursor()

    try:
        # Start the transaction
        cur.execute("BEGIN;")

        # Creating temp_payments table
        cur.execute('''
            CREATE TABLE public.temp_payments (
            payment_id INT8,
            payment_created VARCHAR(255),
            payment_updated VARCHAR(255),
            payment_status VARCHAR(255),
            amount_due FLOAT,
            student_id INT8,
            amount_received FLOAT,
            student_name VARCHAR(255),
            payment_type VARCHAR(255),
            account_id INT8,
            account_updated VARCHAR(255),
            updated_by VARCHAR(255),
            initial_payment VARCHAR(255),
            account_type VARCHAR(255),
            account_source VARCHAR(255),
            lessons_paid_for INT8,
            contract_number VARCHAR(255),
            FO_comment TEXT,
            office_name VARCHAR(255),
            account_created VARCHAR(255),
            account_responsible_person VARCHAR(255),
            course_name VARCHAR(255),
            course_type VARCHAR(255)
        );
        ''')
    
        # Import the CSV data into the temporary table
        with open(csv_path, 'r', encoding='utf-8') as f:
            cur.copy_expert("COPY public.\"temp_payments\" FROM STDIN delimiter ';' encoding 'utf-8' csv header escape '\\' quote '\"'", f)

        v_count = cur.rowcount
        logger.info(f"COPY PAYMENTS {v_count}")

        # Update existing payments
        cur.execute("""
            UPDATE public.payments
            SET
                payment_created = temp_payments.payment_created,
                payment_updated = temp_payments.payment_updated,
                payment_status = temp_payments.payment_status,
                amount_due = temp_payments.amount_due,
                student_id = temp_payments.student_id,
                amount_received = temp_payments.amount_received,
                student_name = temp_payments.student_name,
                payment_type = temp_payments.payment_type,
                account_id = temp_payments.account_id,
                account_updated = temp_payments.account_updated,
                updated_by = temp_payments.updated_by,
                initial_payment = temp_payments.initial_payment,
                account_type = temp_payments.account_type,
                account_source = temp_payments.account_source,
                lessons_paid_for = temp_payments.lessons_paid_for,
                contract_number = temp_payments.contract_number,
                FO_comment = temp_payments.FO_comment,
                office_name = temp_payments.office_name,
                account_created = temp_payments.account_created,
                account_responsible_person = temp_payments.account_responsible_person,
                course_name = temp_payments.course_name,
                course_type = temp_payments.course_type
            FROM temp_payments
            WHERE public.payments.payment_id = temp_payments.payment_id;
        """)

        v_count = cur.rowcount
        logger.info(f"UPDATED PAYMENTS {v_count}")

        # Insert new payments
        cur.execute("""
            INSERT INTO public.payments (
                payment_id, payment_created, payment_updated, payment_status, amount_due,
                student_id, amount_received, student_name, payment_type, account_id,
                account_updated, updated_by, initial_payment, account_type,
                account_source, lessons_paid_for, contract_number, FO_comment, office_name,
                account_created, account_responsible_person, course_name, course_type
            )
            SELECT
                temp_payments.payment_id, temp_payments.payment_created, temp_payments.payment_updated, temp_payments.payment_status, temp_payments.amount_due,
                temp_payments.student_id, temp_payments.amount_received, temp_payments.student_name, temp_payments.payment_type, temp_payments.account_id,
                temp_payments.account_updated, temp_payments.updated_by, temp_payments.initial_payment, temp_payments.account_type,
                temp_payments.account_source, temp_payments.lessons_paid_for, temp_payments.contract_number, temp_payments.FO_comment, temp_payments.office_name,
                temp_payments.account_created, temp_payments.account_responsible_person, temp_payments.course_name, temp_payments.course_type
            FROM temp_payments
            WHERE NOT EXISTS (
                SELECT 1 FROM public.payments
                WHERE public.payments.payment_id = temp_payments.payment_id
            );
        """)

        v_count = cur.rowcount
        logger.info(f"INSERTED PAYMENTS {v_count}")

        # Drop temp_payments table
        cur.execute('DROP TABLE public."temp_payments";')

        # Commit the transaction
        conn.commit()
        return True

    except Exception as e:
        # If any errors occur, roll back the transaction
        conn.rollback()
        logger.error(f"Error during PAYMENTS UPDATE: {e}")
        logger.warning("ROLLBACK CHANGES PAYMENTS")
        return False

    finally:
        # Close the connection
        cur.close()
        conn.close()