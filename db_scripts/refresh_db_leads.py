import psycopg2
from algoritmics_analytics import paths
from algoritmics_analytics import envs
from log_config import logger
import csv
from collections import Counter


def refresh_db_leads():

    #Set variables
    database = envs.database
    user = envs.db_user
    password = envs.db_password
    host = envs.db_host
    port = envs.db_port

    csv_path = paths.leads_csv_path

    # Prepare structure of CSV
    # Load the structure of the first row of CSV file
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        columns = next(reader)  # gets the first line

    # Create a Counter to keep track of occurrences
    counter = Counter()

    # Prepare a string with column names
    columns_sql = ""
    for col in columns:
        col = col.lower() # convert the column name to lowercase
        counter[col] += 1
        if counter[col] > 1:
            col += f".{str(counter[col])}"
        columns_sql += f'"{col}" text,'
    columns_sql = columns_sql[:-1]

    # Print the number of columns
    num_columns = columns_sql.count(",") + 1
    logger.info(f"The number of columns is {num_columns}")

    # Connect to the database psql -h  -U  -d 
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cur = conn.cursor()

    try:
        # Start the transaction
        cur.execute("BEGIN;")

        # Create a temporary table with a matching CSV structure
        cur.execute(f"CREATE TEMPORARY TABLE temp_leads({columns_sql});")
        logger.info("temp_leads table created")

        # Copy data from the csv file to the temporary table
        with open(csv_path, 'r', encoding='utf-8') as f:
            cur.copy_expert("""COPY temp_leads FROM STDIN WITH (FORMAT CSV, DELIMITER ',', ENCODING 'utf-8', HEADER, ESCAPE '"', QUOTE '"')""", f)
        logger.info("leads.csv imported to temp_leads")

        # Get the number of rows affected
        row_count = cur.rowcount
        logger.info(f"COPY LEADS {row_count}")

        # Truncate the table
        cur.execute('TRUNCATE public."leads";')
        logger.info('TRUNCATE TABLE LEADS')

        # Insert new leads from temp table
        cur.execute("""
            INSERT INTO public.leads (
                id,
                "Название сделки",
                "Бюджет ",
                "Ответственный",
                "Дата создания сделки",
                "Кем создана сделка",
                "Дата редактирования",
                "Кем редактирована",
                "Дата закрытия",
                "Теги",
                "Этап сделки",
                "Воронка",
                "Полное имя контакта",
                "Компания контакта",
                "Ответственный за контакт",
                "Source phone",
                "Район",
                "Сегмент базы",
                "Источник трафика",
                "Cтатус в ЦОП",
                "Причина отказа ОП",
                Телефон,
                "Закреплён за",
                "Возраст ребёнка",
                "Район проживания",
                "Причина отказа",
                "Записался на МК на",
                "Педагог",
                "Дата МК",
                "Мастер-класс_Дата_время",
                "Отказ 2019",
                "Отказ2021",
                "Отказ 2020",
                "Source phone.1",
                "Source phone_new",
                "Источник трафика_new",
                "Источник заявки",
                "Фертильный лид",
                "backoffice_id"
            )
            SELECT
                cast(temp_leads."id" AS integer),
                cast(temp_leads."название сделки" AS varchar(255)),
                cast(temp_leads."бюджет " AS float8),
                cast(temp_leads."ответственный" AS varchar(255)),
                cast(temp_leads."дата создания сделки" AS varchar(255)),
                cast(temp_leads."кем создана сделка" AS varchar(255)),
                cast(temp_leads."дата редактирования" AS varchar(255)),
                cast(temp_leads."кем редактирована" AS varchar(255)),
                cast(temp_leads."дата закрытия" AS varchar(255)),
                cast(temp_leads."теги" AS varchar(255)),
                cast(temp_leads."этап сделки" AS varchar(255)),
                cast(temp_leads."воронка" AS varchar(255)),
                cast(temp_leads."полное имя контакта" AS varchar(255)),
                cast(temp_leads."компания контакта" AS varchar(255)),
                cast(temp_leads."ответственный за контакт" AS varchar(255)),
                cast(temp_leads."source phone" AS varchar(255)),
                cast(temp_leads."район" AS varchar(255)),
                cast(temp_leads."сегмент базы" AS varchar(255)),
                cast(temp_leads."источник трафика" AS varchar(255)),
                cast(temp_leads."cтатус в цоп" AS varchar(255)),
                cast(temp_leads."причина отказа оп" AS varchar(255)),
                cast(temp_leads."телефон" AS varchar(255)),
                cast(temp_leads."закреплён за" AS varchar(255)),
                cast(temp_leads."возраст ребёнка" AS varchar(255)),
                cast(temp_leads."район проживания" AS varchar(255)),
                cast(temp_leads."причина отказа" AS varchar(255)),
                cast(temp_leads."записался на мк на" AS varchar(255)),
                cast(temp_leads."педагог" AS varchar(255)),
                cast(temp_leads."дата мк" AS varchar(255)),
                cast(temp_leads."мастер-класс_дата_время" AS varchar(255)),
                cast(temp_leads."отказ 2019" AS varchar(255)),
                cast(temp_leads."отказ2021/2022" AS varchar(255)),
                cast(temp_leads."отказ 2020" AS varchar(255)),
                cast(temp_leads."source phone.2" AS varchar(255)),
                cast(temp_leads."source phone_new" AS varchar(255)),
                cast(temp_leads."источник трафика_new" AS varchar(255)),
                cast(temp_leads."источник заявки" AS varchar(255)),
                cast(temp_leads."фертильный лид" AS varchar(255)),
                cast(temp_leads."backoffice_id" AS varchar(255))
            FROM temp_leads;
        """)

        v_count = cur.rowcount
        logger.info(f"INSERTED LEADS {v_count}")

        # Delete the temporary table
        cur.execute("DROP TABLE temp_leads")
        logger.info("temp_leads table deleted")

        # Commit the changes
        conn.commit()
        return True

    except Exception as e:
        # If any errors occur, roll back the transaction
        conn.rollback()
        logger.error(f"Error during LEADS REFRESH: {e}")
        logger.warning("ROLLBACK CHANGES LEADS")
        return False

    finally:
        # Close the connection
        cur.close()
        conn.close()