"""Add payments table

Revision ID: 0c8118566968
Revises: ecafe76a3d41
Create Date: 2023-07-07 20:55:42.552723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c8118566968'
down_revision = 'ecafe76a3d41'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create payments table
    op.execute("""
        CREATE TABLE public.payments (
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
    """)
    pass


def downgrade() -> None:

    # Drop payments table
    op.execute('''
        DROP TABLE public.payments
    ''')
    pass
