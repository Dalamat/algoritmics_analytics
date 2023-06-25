"""Database Initialization

Revision ID: 8ac873230af2
Revises: 
Create Date: 2023-06-18 17:05:39.504081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ac873230af2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    #Migration 1: Create events table
    op.execute("""
        CREATE TABLE public.events (
            next_lesson_time text NULL,
            next_lesson_number text NULL,
            next_lesson text NULL,
            id text NULL,
            "name" text NULL,
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
    """)
    #Migration 2: Create groups table
    op.execute("""
        CREATE TABLE public.groups (
            id text NULL,
            "name" text NULL,
            platform text NULL,
            geography text NULL,
            participants text NULL,
            paid text NULL,
            enrolled int8 NULL,
            dismissed int8 NULL,
            amc_students_paid_after_master int8 NULL,
            dismissed_transferred int8 NULL,
            first_lesson text NULL,
            next_lesson_time text NULL,
            next_lesson_number text NULL,
            next_lesson text NULL,
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
            format text NULL,
            created text NULL,
            created_by text NULL
        );
    """)
    #Migration 3: Create invoices table
    op.execute("""
        CREATE TABLE public.invoices (
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
    """)
    #Migration 4: Create students table
    op.execute("""
        CREATE TABLE public.students (
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
    """)
    #Migration 5: Create events_view view
    op.execute("""
        CREATE OR REPLACE VIEW public.events_view
        AS SELECT events.id,
            events.name AS "название",
            events.venue AS "площадка",
            events.geography AS "география",
            events.lesson_status AS "s статус урока (new)",
            events.participants AS "уч-ки",
            events.attended_students AS " посетившие ученики",
                CASE
                    WHEN events.paid_students = ''::text THEN NULL::numeric
                    ELSE to_number(events.paid_students, '999'::text)
                END AS " оплатившие",
            events.enrolled_students AS " зачисленные",
            events.expelled_students AS " отчисленные",
            events.amc_paid_after_master AS "amc ученики оплатившие после мастер",
            events.expelled_and_transferred AS " отчисленные и переведенные",
                CASE
                    WHEN events.first_lesson = ''::text THEN NULL::date
                    ELSE to_date(events.first_lesson, 'DD.MM.FXYYYY'::text)
                END AS "первый урок",
            events.day AS "день",
                CASE
                    WHEN events.next_lesson_number = ''::text THEN NULL::numeric
                    ELSE to_number(events.next_lesson_number, '999'::text)
                END AS "#след. урок",
            events.next_lesson AS "след. урок",
            events.teacher AS "преподаватель",
            events.curator AS "куратор",
            events.tutor AS "тьютор",
            events.client_manager AS "клиентский менеджер",
            events.priority AS "приоритет",
            events.group_type AS "тип группы",
            events.status AS "статус",
            events.course AS "курс",
            events.course_type AS "тип курса",
            events.availability AS "доступность",
            events.created AS "создан",
            events.created_by AS "кем создан",
            to_timestamp(events.next_lesson_time, 'DD.MM.FXYYYY HH24:MI'::text) AS "время следующего урока"
        FROM events;
    """)
    #Migration 6: Create groups_view view
    op.execute("""
        CREATE OR REPLACE VIEW public.groups_view
        AS SELECT groups.id,
            groups.name AS "название",
            groups.platform AS "площадка",
            groups.geography AS "география",
            groups.participants AS "уч-ки",
                CASE
                    WHEN groups.paid = ''::text THEN NULL::numeric
                    ELSE to_number(groups.paid, '999'::text)
                END AS "кол-во оплативших",
            groups.enrolled AS " зачисленные",
            groups.dismissed AS " отчисленные",
            groups.amc_students_paid_after_master AS "amc ученики оплатившие после мастер",
            groups.dismissed_transferred AS " отчисленные и переведенные",
                CASE
                    WHEN groups.first_lesson = ''::text THEN NULL::date
                    ELSE to_date(groups.first_lesson, 'DD.MM.YYYY'::text)
                END AS "время первого урока",
                CASE
                    WHEN groups.next_lesson_time = ''::text THEN NULL::timestamp with time zone
                    ELSE to_timestamp(groups.next_lesson_time, 'DD.MM.FXYYYY HH24:MI'::text)
                END AS "время следующего урока",
                CASE
                    WHEN groups.next_lesson_number = ''::text THEN NULL::numeric
                    ELSE to_number(groups.next_lesson_number, '999'::text)
                END AS "# следующего урока",
            groups.next_lesson AS "след. урок",
            groups.teacher AS "преподаватель",
            groups.curator AS "куратор",
            groups.tutor AS "тьютор",
            groups.client_manager AS "клиентский менеджер",
            groups.priority AS "приоритет",
            groups.group_type AS "тип группы",
            groups.status AS "статус",
            groups.course AS "курс",
            groups.course_type AS "тип курса",
            groups.availability AS "доступность",
            groups.format AS "формат",
                CASE
                    WHEN groups.created = ''::text THEN NULL::date
                    ELSE to_date(groups.created, 'DD.MM.YYYY'::text)
                END AS "дата создания",
            groups.created_by AS "кем создан"
        FROM groups;
    """)
    #Migration 7: Create invoices_view view
    op.execute("""
        CREATE OR REPLACE VIEW public.invoices_view
        AS SELECT invoices.id,
                CASE
                    WHEN invoices.invoice_creation_date = ''::text THEN NULL::date
                    ELSE to_date(invoices.invoice_creation_date, 'DD.MM.FXYYYY'::text)
                END AS "дата создания счета",
            invoices.invoice_amount AS "выставленная сумма",
            invoices.lessons_to_pay AS "уроков к оплате",
                CASE
                    WHEN invoices.validity_period = ''::text THEN NULL::date
                    ELSE to_date(invoices.validity_period, 'DD.MM.FXYYYY'::text)
                END AS "срок действия",
            invoices.student_id AS "id ученика",
            invoices.student AS "ученик",
            invoices.payment_type AS "тип оплаты",
            invoices.invoice_source AS "источник счета",
            invoices.invoice_status AS "статус счета",
            invoices.contract_number AS "номер договора",
            invoices.invoice_created AS "счет создан",
            invoices.responsible AS "ответственный",
            invoices.fo_comment AS "комментарий фо",
            invoices.office AS "офис",
            invoices.payment_id AS "id платежа",
            invoices.payment_method AS "тип платежа",
            invoices.payment_status AS "статус платежа",
            invoices.payment_received AS "получено по платежу",
                CASE
                    WHEN invoices.payment_creation_date = ''::text THEN NULL::date
                    ELSE to_date(invoices.payment_creation_date, 'DD.MM.FXYYYY'::text)
                END AS "дата создания платежа",
                CASE
                    WHEN invoices.payment_created_by_hour = ''::text THEN NULL::timestamp with time zone
                    ELSE to_timestamp(invoices.payment_created_by_hour, 'DD.MM.FXYYYY HH24:MI'::text)
                END AS "платеж создан по часам",
                CASE
                    WHEN invoices.payment_update_date = ''::text THEN NULL::date
                    ELSE to_date(invoices.payment_update_date, 'DD.MM.FXYYYY'::text)
                END AS "дата изменения платежа",
                CASE
                    WHEN invoices.payment_updated_by_hour = ''::text THEN NULL::timestamp with time zone
                    ELSE to_timestamp(invoices.payment_updated_by_hour, 'DD.MM.FXYYYY HH24:MI'::text)
                END AS "платеж обновлен по часам",
            invoices.payment_changed AS "платеж изменен",
            invoices.group_type AS "тип группы",
            invoices.group_status AS "статус группы",
            invoices.course AS "курс",
            invoices.course_type AS "тип курса",
            students.client_manager AS "клиентский менеджер",
            students.curator AS "куратор",
            groups.platform AS "площадка"
        FROM invoices
            LEFT JOIN students ON students.id = invoices.student_id
            LEFT JOIN groups ON students.group_id = groups.id;
    """)
    #Migration 8: Create students_view view
    op.execute("""
        CREATE OR REPLACE VIEW public.students_view
        AS SELECT students.id,
            students.name AS "имя",
            students.login AS "логин",
            students.password AS "пароль",
                CASE
                    WHEN students.age = ''::text THEN NULL::numeric
                    ELSE to_number(students.age, '999'::text)
                END AS "возраст",
                CASE
                    WHEN students.birthdate = ''::text THEN NULL::date
                    ELSE to_date(students.birthdate, 'DD.MM.FXYYYY'::text)
                END AS "дата рождения",
            students.parent_name AS "имя родителя",
            students.parent_phone AS "тел. родителя",
            students.email AS "e-mail",
                CASE
                    WHEN students.created = ''::text THEN NULL::date
                    ELSE to_date(students.created, 'DD.MM.FXYYYY'::text)
                END AS "создан",
            students.created_by AS "кем создан",
            students.geography AS "география",
            students.sales AS "сейлз",
            students.group_id AS "id группы",
            students.group_name AS "группа",
            students.description AS "описание",
                CASE
                    WHEN students.enrolled_in_group = ''::text THEN NULL::timestamp with time zone
                    ELSE to_timestamp(students.enrolled_in_group, 'DD.MM.FXYYYY HH24:MI'::text)
                END AS "записан в группу",
            students.teacher AS "преподаватель",
                CASE
                    WHEN students.total_group_lessons = ''::text THEN NULL::numeric
                    ELSE to_number(students.total_group_lessons, '999'::text)
                END AS "всего уроков в группе",
            students.curator AS "куратор",
            students.tutor AS "тьютор",
            students.client_manager AS "клиентский менеджер",
                CASE
                    WHEN students.lessons_completed = ''::text THEN NULL::numeric
                    ELSE to_number(students.lessons_completed, '999'::text)
                END AS "прошло уроков в группе",
                CASE
                    WHEN students.group_start = ''::text THEN NULL::date
                    ELSE to_date(students.group_start, 'DD.MM.FXYYYY'::text)
                END AS "старт группы",
            students.group_type AS "тип группы",
            students.group_status AS "статус группы",
            students.student_status AS "статус ученика в группе",
                CASE
                    WHEN students.lessons_attended = ''::text THEN NULL::numeric
                    ELSE to_number(students.lessons_attended, '999'::text)
                END AS " посетил уроков",
                CASE
                    WHEN students.lessons_missed = ''::text THEN NULL::numeric
                    ELSE to_number(students.lessons_missed, '999'::text)
                END AS " пропустил уроков",
            students.lessons_missed_consecutive AS "пропустил уроков подряд",
            students.attendance AS "посещаемость",
            students.total_invoiced AS "всего выставлено",
            students.paid AS "оплачено",
            students.lessons_paid AS "оплачено уроков",
                CASE
                    WHEN students.balance = ''::text THEN NULL::bigint::numeric
                    ELSE to_number(students.balance, '999'::text)
                END AS "баланс",
            students.amo_pipeline AS "amo pipeline",
            students.deal_status AS "статус сделки",
                CASE
                    WHEN students.expelled = ''::text THEN NULL::timestamp without time zone::timestamp with time zone
                    ELSE to_timestamp(students.expelled, 'DD.MM.FXYYYY HH24:MI'::text)
                END AS "отчислен",
            students.expulsion_reasons AS "причины отчисления",
            students.office AS "офис",
            students.course AS "курс",
            students.course_type AS "тип курса",
            students.skype AS "скайп",
            students.remote AS "удалён",
            students.system AS "системный",
            groups.platform AS "площадка",
            concat('https://backoffice.algoritmika.org/student/update/', students.id) AS link,
            groups.name AS "название",
            students.paid / NULLIF(students.lessons_paid::double precision, 0::double precision) AS "стоимость_урока"
        FROM students
            LEFT JOIN groups ON students.group_id = groups.id;
    """)
    #Migration 9: Create events_for_students view
    op.execute("""
        CREATE OR REPLACE VIEW public.events_for_students
        AS SELECT students_view.id,
            students_view."id группы",
            students_view."группа",
            students_view."преподаватель",
            students_view."тип группы",
            students_view."статус группы",
            students_view."статус ученика в группе",
            students_view."оплачено уроков",
            students_view."баланс",
            students_view."курс",
            students_view."тип курса",
            events_view."s статус урока (new)",
            events_view."#след. урок" AS "#след. урок events",
            events_view." посетившие ученики",
            groups_view."# следующего урока" AS "#след. урок groups",
            students_view."отчислен",
            students_view."записан в группу",
            students_view."прошло уроков в группе",
            students_view."куратор",
            students_view."клиентский менеджер",
            events_view."площадка",
                CASE
                    WHEN events_view."#след. урок" <= (students_view."прошло уроков в группе" + students_view."баланс") THEN 1
                    ELSE 0
                END AS "оплачено",
            events_view."время следующего урока"
        FROM students_view
            JOIN groups_view ON students_view."id группы" = groups_view.id
            JOIN events_view ON groups_view.id = events_view.id;
    """)
    #Migration 10: Create payments_by_4 view
    op.execute("""
        CREATE OR REPLACE VIEW public.payments_by_4
        AS SELECT t."название" AS "имя группы",
            t."id группы",
            t."имя",
            t.id,
            t."оплачено",
            min(t."#след. урок events") AS first_event,
            count(*) AS count,
            min(t."время следующего урока") AS min,
            t."площадка",
            t."стоимость_урока"
        FROM ( SELECT events_for_students.id,
                    events_for_students."id группы",
                    events_for_students."группа",
                    events_for_students."преподаватель",
                    events_for_students."тип группы",
                    events_for_students."статус группы",
                    events_for_students."статус ученика в группе",
                    events_for_students."оплачено уроков",
                    events_for_students."баланс",
                    events_for_students."курс",
                    events_for_students."тип курса",
                    events_for_students."s статус урока (new)",
                    events_for_students."время следующего урока",
                    events_for_students."#след. урок events",
                    events_for_students." посетившие ученики",
                    events_for_students."#след. урок groups",
                    events_for_students."отчислен",
                    events_for_students."записан в группу",
                    events_for_students."прошло уроков в группе",
                    events_for_students."куратор",
                    events_for_students."клиентский менеджер",
                    events_for_students."площадка",
                    events_for_students."оплачено",
                    row_number() OVER (PARTITION BY events_for_students."оплачено", events_for_students."id группы", events_for_students.id, students_view."имя", groups_view."название", events_for_students."площадка" ORDER BY events_for_students."id группы", events_for_students.id, events_for_students."оплачено" DESC, events_for_students."#след. урок events") AS r,
                    students_view."имя",
                    students_view."стоимость_урока",
                    groups_view."название"
                FROM events_for_students
                    JOIN students_view ON events_for_students.id = students_view.id
                    JOIN groups_view ON events_for_students."id группы" = groups_view.id
                WHERE events_for_students."оплачено" = 0 AND events_for_students."статус ученика в группе" = 'активен'::text AND (events_for_students."статус группы" = 'Активная'::text OR events_for_students."статус группы" = 'Идет набор'::text)) t
        GROUP BY t."оплачено", ((t.r - 1) / 4), t.id, t."id группы", t."имя", t."название", t."площадка", t."стоимость_урока"
        ORDER BY t."площадка", t."id группы", t.id, (min(t."#след. урок events")), t."оплачено" DESC;
    """)
    pass

def downgrade() -> None:
        # Revert Migration 10
    op.execute("""
        DROP VIEW public.payments_by_4
    """)
        # Revert Migration 9
    op.execute("""
        DROP VIEW public.events_for_students
    """)
        # Revert Migration 8
    op.execute("""
        DROP VIEW public.students_view
    """)
        # Revert Migration 7
    op.execute("""
        DROP VIEW public.invoices_view
    """)
        # Revert Migration 6
    op.execute("""
        DROP VIEW public.groups_view
    """)
        # Revert Migration 5
    op.execute("""
        DROP VIEW public.events_view
    """)
        # Revert Migration 4
    op.execute("""
        DROP TABLE public.students
    """)
        # Revert Migration 3
    op.execute("""
        DROP TABLE public.invoices
    """)
        # Revert Migration 2
    op.execute("""
        DROP TABLE public.groups
    """)
        # Revert Migration 1
    op.execute("""
        DROP TABLE public.events
    """)
    pass
