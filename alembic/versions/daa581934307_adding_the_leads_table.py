"""Adding the Leads table

Revision ID: daa581934307
Revises: 8ac873230af2
Create Date: 2023-06-25 13:43:08.442927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daa581934307'
down_revision = '8ac873230af2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create Leads table
    # Several columns were renamed to xxx.1/2 because of the duplicates
    op.execute("""
        CREATE TABLE public.leads (
            ID SERIAL,
            "Название сделки" VARCHAR(255),
            "Бюджет " FLOAT,
            Ответственный VARCHAR(255),
            "Дата создания сделки" VARCHAR(255),
            "Кем создана сделка" VARCHAR(255),
            "Дата редактирования" VARCHAR(255),
            "Кем редактирована" VARCHAR(255),
            "Дата закрытия" VARCHAR(255),
            Теги VARCHAR(255),
            Примечание TEXT,
            "Примечание 2" TEXT,
            "Примечание 3" TEXT,
            "Примечание 4" TEXT,
            "Примечание 5" TEXT,
            "Этап сделки" VARCHAR(255),
            Воронка VARCHAR(255),
            "Полное имя контакта" VARCHAR(255),
            "Компания контакта" VARCHAR(255),
            "Ответственный за контакт" VARCHAR(255),
            Компания VARCHAR(255),
            "Рабочий телефон" TEXT,
            "Рабочий прямой телефон" VARCHAR(255),
            "Мобильный телефон" VARCHAR(255),
            Факс VARCHAR(255),
            "Домашний телефон" VARCHAR(255),
            "Другой телефон" VARCHAR(255),
            "Рабочий email" TEXT,
            "Личный email" TEXT,
            "Другой email" TEXT,
            "Source phone" VARCHAR(255),
            text TEXT,
            "Ваше имя" VARCHAR(255),
            "Телефон (NEW)" VARCHAR(255),
            Instagram VARCHAR(255),
            "День рождения" VARCHAR(255),
            Должность VARCHAR(255),
            Район VARCHAR(255),
            "Сегмент базы" VARCHAR(255),
            "Имена детей" TEXT,
            "Возраст детей" TEXT,
            "Школы детей" TEXT,
            "Уникальный ID" VARCHAR(255),
            Реферал VARCHAR(255),
            "NPC Погашеные" FLOAT,
            "NPC Всего" FLOAT,
            "Источник трафика" VARCHAR(255),
            Трекинг VARCHAR(255),
            MailChimp VARCHAR(255),
            "Пользовательское соглашение" VARCHAR(255),
            "Стал клиентом" VARCHAR(255),
            Skype VARCHAR(255),
            ICQ VARCHAR(255),
            Jabber VARCHAR(255),
            "Google Talk" VARCHAR(255),
            MSN VARCHAR(255),
            "Другой IM" VARCHAR(255),
            "Куда вам отправить приглашение?" VARCHAR(255),
            Выбор VARCHAR(255),
            "Занимался ли ваш ребенок программированием ранее?" VARCHAR(255),
            Возраст VARCHAR(255),
            Телефон VARCHAR(255),
            Имя VARCHAR(255),
            "Закреплён за" VARCHAR(255),
            "Возраст ребёнка" VARCHAR(255),
            "Район проживания" VARCHAR(255),
            Школа VARCHAR(255),
            Комментарий TEXT,
            "Причина отказа" TEXT,
            "Записался на МК на" VARCHAR(255),
            UTM_SOURCE VARCHAR(255),
            "url (NEW)" TEXT,
            Педагог VARCHAR(255),
            "Дата МК" VARCHAR(255),
            "День рождения_new" VARCHAR(255),
            "Номер договора" VARCHAR(255),
            "Ученик в БО связан" VARCHAR(255),
            "Переведён в группу" VARCHAR(255),
            "Счёт в БО выставлен" VARCHAR(255),
            "Счёт в БО оплачен" VARCHAR(255),
            "Отказ 2019" VARCHAR(255),
            Отказ2021 VARCHAR(255),
            "Отказ 2020" VARCHAR(255),
            "Source phone.1" VARCHAR(255),
            da_id VARCHAR(255),
            ip VARCHAR(255),
            UTM_TERM VARCHAR(255),
            UTM_CONTENT VARCHAR(255),
            UTM_MEDIUM VARCHAR(255),
            UTM_CAMPAIGN VARCHAR(255),
            FORMID VARCHAR(255),
            REFERER TEXT,
            TRANID VARCHAR(255),
            "Адрес страницы" VARCHAR(255),
            Форма VARCHAR(255),
            ym_client_id VARCHAR(255),
            url TEXT,
            "Группа в АМО" VARCHAR(255),
            Страница VARCHAR(255),
            Скидка VARCHAR(255),
            "Курс интересует" VARCHAR(255),
            "Курс окончил" VARCHAR(255),
            Площадка VARCHAR(255),
            Куратор VARCHAR(255),
            Курс VARCHAR(255),
            "Дата выбывания" VARCHAR(255),
            "Номер урока отсева" VARCHAR(255),
            "Причина отсева" TEXT,
            "Source phone_new" VARCHAR(255),
            "Источник трафика_new" VARCHAR(255),
            "utm_source.1" VARCHAR(255),
            "utm_campaign.1" VARCHAR(255),
            "Ссылка для формы" VARCHAR(255),
            "Причина отказа.1" TEXT,
            "Источник заявки" VARCHAR(255),
            "Фертильный лид" VARCHAR(255),
            "Реферальная прогр" VARCHAR(255),
            openstat_campaign VARCHAR(255),
            yclid VARCHAR(255),
            gclid VARCHAR(255),
            gclientid VARCHAR(255),
            "from" VARCHAR(255),
            openstat_source VARCHAR(255),
            openstat_ad VARCHAR(255),
            fbclid VARCHAR(255),
            openstat_service VARCHAR(255),
            referrer VARCHAR(255),
            roistat VARCHAR(255),
            _ym_counter VARCHAR(255),
            _ym_uid VARCHAR(255),
            utm_referrer TEXT,
            "utm_content.1" VARCHAR(255),
            "utm_term.1" VARCHAR(255),
            "utm_campaign.2" VARCHAR(255),
            "utm_medium.1" VARCHAR(255),
            "utm_source.2" VARCHAR(255)
            );
    """)
    pass


def downgrade() -> None:
    op.execute("""
        DROP TABLE public.leads
    """)
    pass
