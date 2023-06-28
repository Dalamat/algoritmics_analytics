"""Budget table and view

Revision ID: ecafe76a3d41
Revises: 2c7eb7ba98bd
Create Date: 2023-06-28 19:43:04.355401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecafe76a3d41'
down_revision = '2c7eb7ba98bd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create budget table
    op.execute('''
        CREATE TABLE public.budget(
            date date,
            sum float
        );
    ''')
    # Create budget_view view
    op.execute('''
        CREATE VIEW public.budget_view AS
        SELECT date as "Дата",
        sum as "Сумма"
        from public.budget;
    ''')
    pass


def downgrade() -> None:
    # Drop budget_view view
    op.execute('''
        DROP VIEW public.budget_view
    ''')
    # Drop budget table
    op.execute('''
    DROP TABLE public.budget
    ''')
    pass
