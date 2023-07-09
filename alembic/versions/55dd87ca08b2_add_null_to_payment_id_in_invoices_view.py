"""Add NULL to payment_id in invoices_view

Revision ID: 55dd87ca08b2
Revises: 24eb9d8829e7
Create Date: 2023-07-08 14:47:30.354478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55dd87ca08b2'
down_revision = '24eb9d8829e7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Update invoices_view
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
            CASE 
                    WHEN invoices.payment_id = '' THEN NULL
                    ELSE invoices.payment_id
                END AS "id платежа",
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
    pass


def downgrade() -> None:
    # Revert invoices_view
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
    pass
