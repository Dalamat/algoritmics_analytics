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
                "Примечание",
                "Примечание 2",
                "Примечание 3",
                "Примечание 4",
                "Примечание 5",
                "Этап сделки",
                "Воронка",
                "Полное имя контакта",
                "Компания контакта",
                "Ответственный за контакт",
                "Компания",
                "Рабочий телефон",
                "Рабочий прямой телефон",
                "Мобильный телефон",
                "Факс",
                "Домашний телефон",
                "Другой телефон",
                "Рабочий email",
                "Личный email",
                "Другой email",
                "Source phone",
                "text",
                "Ваше имя",
                "Телефон (NEW)",
                "Имя.2",
                "instagram",
                "День рождения",
                "Должность",
                "Район",
                "Сегмент базы",
                "Имена детей",
                "Возраст детей",
                "Школы детей",
                "Уникальный ID",
                "Реферал",
                "NPC Погашеные",
                "NPC Всего",
                "Источник трафика",
                "Трекинг",
                "mailchimp",
                "Пользовательское соглашение",
                "Стал клиентом",
                "skype",
                ICQ,
                "jabber",
                "Google Talk",
                "msn",
                "Другой IM",
                "Cтатус в ЦОП",
                "Комментарий ОП",
                "Примечание партнера",
                "Выбор",
                Телефон,
                "Занимался ли ваш ребенок программированием ранее?",
                "Занимались ранее программированием?",
                "Филиал",
                "Куда вам отправить приглашение?",
                "Возраст",
                "Имя",
                "Закреплён за",
                "Возраст ребёнка",
                "Район проживания",
                "Школа",
                "Комментарий",
                "Причина отказа",
                "Записался на МК на",
                "utm_source",
                "url (NEW)",
                "Педагог",
                "Дата МК",
                "День рождения_new",
                "Номер договора",
                "Логин",
                "Пароль",
                "Название МК (маркет)",
                "Мастер-класс_Дата_время",
                "Имя ребенка из LMS",
                "Фамилия ребенка из LMS",
                "Название курса из LMS",
                "Маркетинговый тип курса",
                "название площадки",
                "Адрес площадки LMS",
                "Преподаватель",
                "Название группы LMS",
                "дата+время группы",
                "Ученик в БО связан",
                "Переведён в группу",
                "Счёт в БО выставлен",
                "Счёт в БО оплачен",
                "Адрес страницы",
                "Отказ 2019",
                "Отказ2021",
                "Отказ 2020",
                "Source phone.1",
                "da_id",
                "ip",
                "utm_term",
                "utm_content",
                "utm_medium",
                utm_campaign,
                "formid",
                "referer",
                "tranid",
                "Форма",
                "ym_client_id",
                "url",
                "Группа в АМО",
                "Страница",
                "Комментарий ОП(old)",
                "Скидка",
                "Курс интересует",
                "Курс окончил",
                "Площадка",
                "Куратор",
                "Курс",
                "Дата выбывания",
                "Номер урока отсева",
                "Причина отсева",
                "Source phone_new",
                "Источник трафика_new",
                "utm_source.1",
                "utm_campaign.1",
                "Ссылка для формы",
                "Причина отказа.1",
                "Источник заявки",
                "Фертильный лид",
                "ITBOT",
                "backoffice_id",
                "лид из телефонии?",
                "Реферальная прогр",
                "ЦОП - Адрес площадки",
                "openstat_campaign",
                "yclid",
                "gclid",
                "gclientid",
                "from",
                "openstat_source",
                "openstat_ad",
                "fbclid",
                "openstat_service",
                "referrer",
                "roistat",
                "_ym_counter",
                "_ym_uid",
                "utm_referrer",
                "utm_content.1",
                "utm_term.1",
                "utm_campaign.2",
                "utm_medium.1",
                "utm_source.2"
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
                cast(temp_leads."примечание" AS text),
                cast(temp_leads."примечание 2" AS text),
                cast(temp_leads."примечание 3" AS text),
                cast(temp_leads."примечание 4" AS text),
                cast(temp_leads."примечание 5" AS text),
                cast(temp_leads."этап сделки" AS varchar(255)),
                cast(temp_leads."воронка" AS varchar(255)),
                cast(temp_leads."полное имя контакта" AS varchar(255)),
                cast(temp_leads."компания контакта" AS varchar(255)),
                cast(temp_leads."ответственный за контакт" AS varchar(255)),
                cast(temp_leads."компания" AS varchar(255)),
                cast(temp_leads."рабочий телефон" AS text),
                cast(temp_leads."рабочий прямой телефон" AS varchar(255)),
                cast(temp_leads."мобильный телефон" AS varchar(255)),
                cast(temp_leads."факс" AS varchar(255)),
                cast(temp_leads."домашний телефон" AS varchar(255)),
                cast(temp_leads."другой телефон" AS varchar(255)),
                cast(temp_leads."рабочий email" AS text),
                cast(temp_leads."личный email" AS varchar(255)),
                cast(temp_leads."другой email" AS varchar(255)),
                cast(temp_leads."source phone" AS varchar(255)),
                cast(temp_leads."text" AS text),
                cast(temp_leads."ваше имя" AS varchar(255)),
                cast(temp_leads."телефон (new)" AS varchar(255)),
                cast(temp_leads."имя" AS varchar(255)),
                cast(temp_leads."instagram" AS varchar(255)),
                cast(temp_leads."день рождения" AS varchar(255)),
                cast(temp_leads."должность" AS varchar(255)),
                cast(temp_leads."район" AS varchar(255)),
                cast(temp_leads."сегмент базы" AS varchar(255)),
                cast(temp_leads."имена детей" AS varchar(255)),
                cast(temp_leads."возраст детей" AS varchar(255)),
                cast(temp_leads."школы детей" AS varchar(255)),
                cast(temp_leads."уникальный id" AS varchar(255)),
                cast(temp_leads."реферал" AS varchar(255)),
                cast(temp_leads."npc погашеные" AS float8),
                cast(temp_leads."npc всего" AS float8),
                cast(temp_leads."источник трафика" AS varchar(255)),
                cast(temp_leads."трекинг" AS varchar(255)),
                cast(temp_leads."mailchimp" AS varchar(255)),
                cast(temp_leads."пользовательское соглашение" AS varchar(255)),
                cast(temp_leads."стал клиентом" AS varchar(255)),
                cast(temp_leads."skype" AS varchar(255)),
                cast(temp_leads."icq" AS varchar(255)),
                cast(temp_leads."jabber" AS varchar(255)),
                cast(temp_leads."google talk" AS varchar(255)),
                cast(temp_leads."msn" AS varchar(255)),
                cast(temp_leads."другой im" AS varchar(255)),
                cast(temp_leads."cтатус в цоп" AS varchar(255)),
                cast(temp_leads."комментарий оп" AS text),
                cast(temp_leads."примечание партнера" AS text),
                cast(temp_leads."выбор" AS varchar(255)),
                cast(temp_leads."телефон" AS varchar(255)),
                cast(temp_leads."занимался ли ваш ребенок программированием ранее?" AS varchar(255)),
                cast(temp_leads."занимались ранее программированием?" AS varchar(255)),
                cast(temp_leads."филиал" AS varchar(255)),
                cast(temp_leads."куда вам отправить приглашение?" AS varchar(255)),
                cast(temp_leads."возраст" AS varchar(255)),
                cast(temp_leads."имя.2" AS varchar(255)),
                cast(temp_leads."закреплён за" AS varchar(255)),
                cast(temp_leads."возраст ребёнка" AS varchar(255)),
                cast(temp_leads."район проживания" AS varchar(255)),
                cast(temp_leads."школа" AS varchar(255)),
                cast(temp_leads."комментарий" AS varchar(255)),
                cast(temp_leads."причина отказа" AS varchar(255)),
                cast(temp_leads."записался на мк на" AS varchar(255)),
                cast(temp_leads."utm_source" AS varchar(255)),
                cast(temp_leads."url (new)" AS text),
                cast(temp_leads."педагог" AS varchar(255)),
                cast(temp_leads."дата мк" AS varchar(255)),
                cast(temp_leads."день рождения_new" AS varchar(255)),
                cast(temp_leads."номер договора" AS varchar(255)),
                cast(temp_leads."логин" AS varchar(255)),
                cast(temp_leads."пароль" AS varchar(255)),
                cast(temp_leads."название мк (маркет)" AS varchar(255)),
                cast(temp_leads."мастер-класс_дата_время" AS varchar(255)),
                cast(temp_leads."имя ребенка из lms" AS varchar(255)),
                cast(temp_leads."фамилия ребенка из lms" AS varchar(255)),
                cast(temp_leads."название курса из lms" AS varchar(255)),
                cast(temp_leads."маркетинговый тип курса" AS varchar(255)),
                cast(temp_leads."название площадки" AS varchar(255)),
                cast(temp_leads."адрес площадки lms" AS varchar(255)),
                cast(temp_leads."преподаватель" AS varchar(255)),
                cast(temp_leads."название группы lms" AS varchar(255)),
                cast(temp_leads."дата+время группы" AS varchar(255)),
                cast(temp_leads."ученик в бо связан" AS varchar(255)),
                cast(temp_leads."переведён в группу" AS varchar(255)),
                cast(temp_leads."счёт в бо выставлен" AS varchar(255)),
                cast(temp_leads."счёт в бо оплачен" AS varchar(255)),
                cast(temp_leads."адрес страницы" AS varchar(255)),
                cast(temp_leads."отказ 2019" AS varchar(255)),
                cast(temp_leads."отказ2021/2022" AS varchar(255)),
                cast(temp_leads."отказ 2020" AS varchar(255)),
                cast(temp_leads."source phone.2" AS varchar(255)),
                cast(temp_leads."da_id" AS varchar(255)),
                cast(temp_leads."ip" AS varchar(255)),
                cast(temp_leads."utm_term" AS varchar(255)),
                cast(temp_leads."utm_content" AS varchar(255)),
                cast(temp_leads."utm_medium" AS varchar(255)),
                cast(temp_leads."utm_campaign" AS varchar(255)),
                cast(temp_leads."formid" AS varchar(255)),
                cast(temp_leads."referer" AS text),
                cast(temp_leads."tranid" AS varchar(255)),
                cast(temp_leads."форма" AS varchar(255)),
                cast(temp_leads."ym_client_id" AS varchar(255)),
                cast(temp_leads."url" AS text),
                cast(temp_leads."группа в амо" AS varchar(255)),
                cast(temp_leads."страница" AS varchar(255)),
                cast(temp_leads."комментарий оп(old)" AS text),
                cast(temp_leads."скидка" AS varchar(255)),
                cast(temp_leads."курс интересует" AS varchar(255)),
                cast(temp_leads."курс окончил" AS varchar(255)),
                cast(temp_leads."площадка" AS varchar(255)),
                cast(temp_leads."куратор" AS varchar(255)),
                cast(temp_leads."курс" AS varchar(255)),
                cast(temp_leads."дата выбывания" AS varchar(255)),
                cast(temp_leads."номер урока отсева" AS varchar(255)),
                cast(temp_leads."причина отсева" AS varchar(255)),
                cast(temp_leads."source phone_new" AS varchar(255)),
                cast(temp_leads."источник трафика_new" AS varchar(255)),
                cast(temp_leads."utm_source.2" AS varchar(255)),
                cast(temp_leads."utm_campaign.2" AS varchar(255)),
                cast(temp_leads."ссылка для формы" AS varchar(255)),
                cast(temp_leads."причина отказа.2" AS varchar(255)),
                cast(temp_leads."источник заявки" AS varchar(255)),
                cast(temp_leads."фертильный лид" AS varchar(255)),
                cast(temp_leads."itbot" AS varchar(255)),
                cast(temp_leads."backoffice_id" AS varchar(255)),
                cast(temp_leads."лид из телефонии?" AS varchar(255)),
                cast(temp_leads."реферальная прогр" AS varchar(255)),
                cast(temp_leads."цоп - адрес площадки" AS varchar(255)),
                cast(temp_leads."openstat_campaign" AS varchar(255)),
                cast(temp_leads."yclid" AS varchar(255)),
                cast(temp_leads."gclid" AS varchar(255)),
                cast(temp_leads."gclientid" AS varchar(255)),
                cast(temp_leads."from" AS varchar(255)),
                cast(temp_leads."openstat_source" AS varchar(255)),
                cast(temp_leads."openstat_ad" AS varchar(255)),
                cast(temp_leads."fbclid" AS varchar(255)),
                cast(temp_leads."openstat_service" AS varchar(255)),
                cast(temp_leads."referrer" AS varchar(255)),
                cast(temp_leads."roistat" AS varchar(255)),
                cast(temp_leads."_ym_counter" AS varchar(255)),
                cast(temp_leads."_ym_uid" AS varchar(255)),
                cast(temp_leads."utm_referrer" AS text),
                cast(temp_leads."utm_content.2" AS varchar(255)),
                cast(temp_leads."utm_term.2" AS varchar(255)),
                cast(temp_leads."utm_campaign.3" AS varchar(255)),
                cast(temp_leads."utm_medium.2" AS varchar(255)),
                cast(temp_leads."utm_source.3" AS varchar(255))
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