"""Added price of lesson to events_for_students view

Revision ID: f038b82b543e
Revises: eabc21937d63
Create Date: 2023-10-27 17:07:41.925061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f038b82b543e'
down_revision = 'eabc21937d63'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # # Drop events_for_students view
    # op.execute('''
    #     DROP VIEW public.events_for_students;
    # ''')
    # # Create events_for_students view
    op.execute('''
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
            events_view."время следующего урока",
            students_view."стоимость_урока"
        FROM students_view
            JOIN groups_view ON students_view."id группы" = groups_view.id
            JOIN events_view ON groups_view.id = events_view.id;
    ''')
    pass


def downgrade() -> None:
    # No downgrade flow. Cannot drop columns from existing view. Will requre recreating all dependent views
    pass
