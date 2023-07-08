import psycopg2
from algoritmics_analytics import paths
from algoritmics_analytics import envs


def update_db_invocies():

    #Set variables
    database = envs.database
    user = envs.db_user
    password = envs.db_password
    host = envs.db_host
    port = envs.db_port

    csv_path = paths.invoices_filter_csv_path

    # Connect to the database psql -h  -U  -d 
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cur = conn.cursor()

    try:
        # Start the transaction
        cur.execute("BEGIN;")

        # Creating temp_invoices table
        cur.execute('''
            CREATE TABLE public."temp_invoices" (
                id int8 NULL,
                invoice_creation_date text NULL,
                invoice_amount text NULL,
                lessons_to_pay int8 NULL,
                validity_period text NULL,
                student_id int8 NULL,
                student text NULL,
                payment_type text NULL,
                invoice_source text NULL,
                invoice_status text NULL,
                contract_number text NULL,
                invoice_created text NULL,
                responsible text NULL,
                fo_comment text NULL,
                office text NULL,
                payment_id text NULL,
                payment_method text NULL,
                payment_status text NULL,
                payment_received text NULL,
                payment_creation_date text NULL,
                payment_created_by_hour text NULL,
                payment_update_date text NULL,
                payment_updated_by_hour text NULL,
                payment_changed text NULL,
                group_type text NULL,
                group_status text NULL,
                course text NULL,
                course_type text NULL
            );
        ''')
    
        # Import the CSV data into the temporary table
        with open(csv_path, 'r', encoding='utf-8') as f:
            cur.copy_expert("COPY public.\"temp_invoices\" FROM STDIN delimiter ';' encoding 'utf-8' csv header escape '\\' quote '\"'", f)

        v_count = cur.rowcount
        print(f"COPY INVOICES {v_count}")

        # Update existing invoices
        cur.execute("""
            UPDATE public.invoices
            SET
                invoice_creation_date = temp_invoices.invoice_creation_date,
                invoice_amount = temp_invoices.invoice_amount,
                lessons_to_pay = temp_invoices.lessons_to_pay,
                validity_period = temp_invoices.validity_period,
                student_id = temp_invoices.student_id,
                student = temp_invoices.student,
                payment_type = temp_invoices.payment_type,
                invoice_source = temp_invoices.invoice_source,
                invoice_status = temp_invoices.invoice_status,
                contract_number = temp_invoices.contract_number,
                invoice_created = temp_invoices.invoice_created,
                responsible = temp_invoices.responsible,
                fo_comment = temp_invoices.fo_comment,
                office = temp_invoices.office,
                payment_id = temp_invoices.payment_id,
                payment_method = temp_invoices.payment_method,
                payment_status = temp_invoices.payment_status,
                payment_received = temp_invoices.payment_received,
                payment_creation_date = temp_invoices.payment_creation_date,
                payment_created_by_hour = temp_invoices.payment_created_by_hour,
                payment_update_date = temp_invoices.payment_update_date,
                payment_updated_by_hour = temp_invoices.payment_updated_by_hour,
                payment_changed = temp_invoices.payment_changed,
                group_type = temp_invoices.group_type,
                group_status = temp_invoices.group_status,
                course = temp_invoices.course,
                course_type = temp_invoices.course_type
            FROM temp_invoices
            WHERE public.invoices.id = temp_invoices.id AND public.invoices.payment_id = temp_invoices.payment_id;
        """)

        v_count = cur.rowcount
        print(f"UPDATED INVOICES {v_count}")

        # Insert new invoices
        cur.execute("""
            INSERT INTO public.invoices (
                id, invoice_creation_date, invoice_amount, lessons_to_pay, validity_period,
                student_id, student, payment_type, invoice_source, invoice_status,
                contract_number, invoice_created, responsible, fo_comment, office,
                payment_id, payment_method, payment_status, payment_received,
                payment_creation_date, payment_created_by_hour, payment_update_date,
                payment_updated_by_hour, payment_changed, group_type, group_status,
                course, course_type
            )
            SELECT
                temp_invoices.id, temp_invoices.invoice_creation_date, temp_invoices.invoice_amount, temp_invoices.lessons_to_pay, temp_invoices.validity_period,
                temp_invoices.student_id, temp_invoices.student, temp_invoices.payment_type, temp_invoices.invoice_source, temp_invoices.invoice_status,
                temp_invoices.contract_number, temp_invoices.invoice_created, temp_invoices.responsible, temp_invoices.fo_comment, temp_invoices.office,
                temp_invoices.payment_id, temp_invoices.payment_method, temp_invoices.payment_status, temp_invoices.payment_received,
                temp_invoices.payment_creation_date, temp_invoices.payment_created_by_hour, temp_invoices.payment_update_date,
                temp_invoices.payment_updated_by_hour, temp_invoices.payment_changed, temp_invoices.group_type, temp_invoices.group_status,
                temp_invoices.course, temp_invoices.course_type
            FROM temp_invoices
            WHERE NOT EXISTS (
                SELECT 1 FROM public.invoices
                WHERE public.invoices.id = temp_invoices.id AND public.invoices.payment_id = temp_invoices.payment_id
            );
        """)

        v_count = cur.rowcount
        print(f"INSERTED INVOICES {v_count}")

        # Drop temp_invoices table
        cur.execute('DROP TABLE public."temp_invoices";')

        # Commit the transaction
        conn.commit()
        return True

    except Exception as e:
        # If any errors occur, roll back the transaction
        conn.rollback()
        print(f"Error: {e}")
        print("ROLLBACK CHANGES INVOICES")
        return False

    finally:
        # Close the connection
        cur.close()
        conn.close()