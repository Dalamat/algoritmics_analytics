"""Add payments view

Revision ID: 24eb9d8829e7
Revises: 0c8118566968
Create Date: 2023-07-08 13:41:19.196065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24eb9d8829e7'
down_revision = '0c8118566968'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create payments view
    op.execute("""
        CREATE VIEW public.payments_view AS
            SELECT payment_id AS payment_id,
            CASE
                    WHEN payments.payment_created = ''::text THEN NULL::date
                    ELSE to_date(payments.payment_created, 'DD.MM.FXYYYY'::text)
                END AS payment_created,
            CASE
                    WHEN payments.payment_updated = ''::text THEN NULL::date
                    ELSE to_date(payments.payment_updated, 'DD.MM.FXYYYY'::text)
                END AS payment_updated,
            payment_status AS payment_status,
            amount_due AS amount_due,
            student_id AS student_id,
            amount_received AS amount_received,
            student_name AS student_name,
            payment_type AS payment_type,
            account_id AS account_id,
            CASE
                    WHEN payments.account_updated = ''::text THEN NULL::date
                    ELSE to_date(payments.account_updated, 'DD.MM.FXYYYY'::text)
                END AS account_updated,
            updated_by AS updated_by,
            initial_payment AS initial_payment,
            account_type AS account_type,
            account_source AS account_source,
            lessons_paid_for AS lessons_paid_for,
            contract_number AS contract_number,
            FO_comment AS FO_comment,
            office_name AS office_name,
            account_created AS account_created,
            account_responsible_person AS account_responsible_person,
            course_name AS course_name,
            course_type AS course_type
        FROM public.payments;
    """)
    pass


def downgrade() -> None:
    # Drop payments view
    op.execute('''
        DROP VIEW public.payments_view
    ''')
    pass
