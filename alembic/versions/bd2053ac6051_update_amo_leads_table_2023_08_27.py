"""Update AMO Leads table. 2023.08.27

Revision ID: bd2053ac6051
Revises: 455058e0fe8b
Create Date: 2023-08-27 21:59:55.686612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd2053ac6051'
down_revision = '455058e0fe8b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Drop leads table and dependent leads_view view
    op.execute("""
        DROP VIEW public.leads_view;
        DROP TABLE public.leads;
    """)
    # Create new leads table
    op.execute("""
        CREATE TABLE public.leads (
            id serial4 NOT NULL,
            "Название сделки" varchar(255) NULL,
            "Бюджет " float8 NULL,
            "Ответственный" varchar(255) NULL,
            "Дата создания сделки" varchar(255) NULL,
            "Кем создана сделка" varchar(255) NULL,
            "Дата редактирования" varchar(255) NULL,
            "Кем редактирована" varchar(255) NULL,
            "Дата закрытия" varchar(255) NULL,
            "Теги" varchar(255) NULL,
            "Примечание" text NULL,
            "Примечание 2" text NULL,
            "Примечание 3" text NULL,
            "Примечание 4" text NULL,
            "Примечание 5" text NULL,
            "Этап сделки" varchar(255) NULL,
            "Воронка" varchar(255) NULL,
            "Полное имя контакта" varchar(255) NULL,
            "Компания контакта" varchar(255) NULL,
            "Ответственный за контакт" varchar(255) NULL,
            "Компания" varchar(255) NULL,
            "Рабочий телефон" text NULL,
            "Рабочий прямой телефон" varchar(255) NULL,
            "Мобильный телефон" varchar(255) NULL,
            "Факс" varchar(255) NULL,
            "Домашний телефон" varchar(255) NULL,
            "Другой телефон" varchar(255) NULL,
            "Рабочий email" text NULL,
            "Личный email" varchar(255) NULL,
            "Другой email" varchar(255) NULL,
            "Source phone" varchar(255) NULL,
            "text" text NULL,
            "Ваше имя" varchar(255) NULL,
            "Телефон (NEW)" varchar(255) NULL,
            "Имя.2" varchar(255) NULL,
            "instagram" varchar(255) NULL,
            "День рождения" varchar(255) NULL,
            "Должность" varchar(255) NULL,
            "Район" varchar(255) NULL,
            "Сегмент базы" varchar(255) NULL,
            "Имена детей" varchar(255) NULL,
            "Возраст детей" varchar(255) NULL,
            "Школы детей" varchar(255) NULL,
            "Уникальный ID" varchar(255) NULL,
            "Реферал" varchar(255) NULL,
            "NPC Погашеные" float8 NULL,
            "NPC Всего" float8 NULL,
            "Источник трафика" varchar(255) NULL,
            "Трекинг" varchar(255) NULL,
            "mailchimp" varchar(255) NULL,
            "Пользовательское соглашение" varchar(255) NULL,
            "Стал клиентом" varchar(255) NULL,
            "skype" varchar(255) NULL,ICQ varchar(255) NULL,
            "jabber" varchar(255) NULL,
            "Google Talk" varchar(255) NULL,
            "msn" varchar(255) NULL,
            "Другой IM" varchar(255) NULL,
            "Cтатус в ЦОП" varchar(255) NULL,
            "Комментарий ОП" varchar(255) NULL,
            "Примечание партнера" text NULL,
            "Выбор" varchar(255) NULL,Телефон varchar(255) NULL,
            "Занимался ли ваш ребенок программированием ранее?" varchar(255) NULL,
            "Занимались ранее программированием?" varchar(255) NULL,
            "Филиал" varchar(255) NULL,
            "Куда вам отправить приглашение?" varchar(255) NULL,
            "Возраст" varchar(255) NULL,
            "Имя" varchar(255) NULL,
            "Закреплён за" varchar(255) NULL,
            "Возраст ребёнка" varchar(255) NULL,
            "Район проживания" varchar(255) NULL,
            "Школа" varchar(255) NULL,
            "Комментарий" varchar(255) NULL,
            "Причина отказа" varchar(255) NULL,
            "Записался на МК на" varchar(255) NULL,
            "utm_source" varchar(255) NULL,
            "url (NEW)" text NULL,
            "Педагог" varchar(255) NULL,
            "Дата МК" varchar(255) NULL,
            "День рождения_new" varchar(255) NULL,
            "Номер договора" varchar(255) NULL,
            "Логин" varchar(255) NULL,
            "Пароль" varchar(255) NULL,
            "Название МК (маркет)" varchar(255) NULL,
            "Мастер-класс_Дата_время" varchar(255) NULL,
            "Имя ребенка из LMS" varchar(255) NULL,
            "Фамилия ребенка из LMS" varchar(255) NULL,
            "Название курса из LMS" varchar(255) NULL,
            "Маркетинговый тип курса" varchar(255) NULL,
            "название площадки" varchar(255) NULL,
            "Адрес площадки LMS" varchar(255) NULL,
            "Преподаватель" varchar(255) NULL,
            "Название группы LMS" varchar(255) NULL,
            "дата+время группы" varchar(255) NULL,
            "Ученик в БО связан" varchar(255) NULL,
            "Переведён в группу" varchar(255) NULL,
            "Счёт в БО выставлен" varchar(255) NULL,
            "Счёт в БО оплачен" varchar(255) NULL,
            "Адрес страницы" varchar(255) NULL,
            "Отказ 2019" varchar(255) NULL,
            "Отказ2021" varchar(255) NULL,
            "Отказ 2020" varchar(255) NULL,
            "Source phone.1" varchar(255) NULL,
            "da_id" varchar(255) NULL,
            "ip" varchar(255) NULL,
            "utm_term" varchar(255) NULL,
            "utm_content" varchar(255) NULL,
            "utm_medium" varchar(255) NULL,
            utm_campaign varchar(255) NULL,
            "formid" varchar(255) NULL,
            "referer" text NULL,
            "tranid" varchar(255) NULL,
            "Форма" varchar(255) NULL,
            "ym_client_id" varchar(255) NULL,
            "url" text NULL,
            "Группа в АМО" varchar(255) NULL,
            "Страница" varchar(255) NULL,
            "Скидка" varchar(255) NULL,
            "Курс интересует" varchar(255) NULL,
            "Курс окончил" varchar(255) NULL,
            "Площадка" varchar(255) NULL,
            "Куратор" varchar(255) NULL,
            "Курс" varchar(255) NULL,
            "Дата выбывания" varchar(255) NULL,
            "Номер урока отсева" varchar(255) NULL,
            "Причина отсева" varchar(255) NULL,
            "Source phone_new" varchar(255) NULL,
            "Источник трафика_new" varchar(255) NULL,
            "utm_source.1" varchar(255) NULL,
            "utm_campaign.1" varchar(255) NULL,
            "Ссылка для формы" varchar(255) NULL,
            "Причина отказа.1" varchar(255) NULL,
            "Источник заявки" varchar(255) NULL,
            "Фертильный лид" varchar(255) NULL,
            "ITBOT" varchar(255) NULL,
            "Реферальная прогр" varchar(255) NULL,
            "ЦОП - Адрес площадки" varchar(255) NULL,
            "openstat_campaign" varchar(255) NULL,
            "yclid" varchar(255) NULL,
            "gclid" varchar(255) NULL,
            "gclientid" varchar(255) NULL,
            "from" varchar(255) NULL,
            "openstat_source" varchar(255) NULL,
            "openstat_ad" varchar(255) NULL,
            "fbclid" varchar(255) NULL,
            "openstat_service" varchar(255) NULL,
            "referrer" varchar(255) NULL,
            "roistat" varchar(255) NULL,
            "_ym_counter" varchar(255) NULL,
            "_ym_uid" varchar(255) NULL,
            "utm_referrer" text NULL,
            "utm_content.1" varchar(255) NULL,
            "utm_term.1" varchar(255) NULL,
            "utm_campaign.2" varchar(255) NULL,
            "utm_medium.1" varchar(255) NULL,
            "utm_source.2" varchar(255) NULL
        );
    """)

    op.execute('''
    CREATE VIEW public.leads_view AS
        SELECT id AS "id",
        "Название сделки" AS "Название сделки",
        "Бюджет " AS "Бюджет ",
        Ответственный AS "Ответственный",
        COALESCE(TO_DATE("Дата создания сделки", 'DD.MM.YYYY'), NULL) AS "Дата создания",
        "Кем создана сделка" AS "Кем создана сделка",
        COALESCE(TO_DATE("Дата редактирования", 'DD.MM.YYYY'), NULL) AS "Дата редактирования",
        "Кем редактирована" AS "Кем редактирована",
        CASE
            WHEN "Дата закрытия" = 'не закрыта' THEN NULL
            ELSE COALESCE(TO_DATE("Дата закрытия", 'DD.MM.YYYY'), NULL)
        END AS "Дата закрытия",
        Теги AS "Теги сделки",
        Примечание AS "Примечание",
        "Примечание 2" AS "Примечание 2",
        "Примечание 3" AS "Примечание 3",
        "Примечание 4" AS "Примечание 4",
        "Примечание 5" AS "Примечание 5",
        "Этап сделки" AS "Этап сделки",
        Воронка AS "Воронка",
        "Полное имя контакта" AS "Полное имя контакта",
        "Компания контакта" AS "Компания контакта",
        "Ответственный за контакт" AS "Ответственный за контакт",
        Компания AS "Компания",
        "Рабочий телефон" AS "Рабочий телефон",
        "Рабочий прямой телефон" AS "Рабочий прямой телефон",
        "Мобильный телефон" AS "Мобильный телефон",
        Факс AS "Факс",
        "Домашний телефон" AS "Домашний телефон",
        "Другой телефон" AS "Другой телефон",
        "Рабочий email" AS "Рабочий email",
        "Личный email" AS "Личный email",
        "Другой email" AS "Другой email",
        "Source phone" AS "Source phone",
        text AS "text",
        "Ваше имя" AS "Ваше имя",
        "Телефон (NEW)" AS "Телефон (NEW)",
        Instagram AS "Instagram",
        "День рождения" AS "День рождения",
        Должность AS "Должность",
        Район AS "Район",
        "Сегмент базы" AS "Сегмент базы",
        "Имена детей" AS "Имена детей",
        "Возраст детей" AS "Возраст детей",
        "Школы детей" AS "Школы детей",
        "Уникальный ID" AS "Уникальный ID",
        Реферал AS "Реферал",
        "NPC Погашеные" AS "NPC Погашеные",
        "NPC Всего" AS "NPC Всего",
        "Источник трафика" AS "Источник трафика",
        Трекинг AS "Трекинг",
        MailChimp AS "MailChimp",
        "Пользовательское соглашение" AS "Пользовательское соглашение",
        "Стал клиентом" AS "Стал клиентом",
        Skype AS "Skype",
        ICQ AS "ICQ",
        Jabber AS "Jabber",
        "Google Talk" AS "Google Talk",
        MSN AS "MSN",
        "Другой IM" AS "Другой IM",
        "Куда вам отправить приглашение?" AS "Куда вам отправить приглашение?",
        Выбор AS "Выбор",
        "Занимался ли ваш ребенок программированием ранее?" AS "Занимался ли ваш ребенок программированием ранее?",
        Возраст AS "Возраст",
        Телефон AS "Телефон",
        Имя AS "Имя",
        "Закреплён за" AS "Закреплён за",
        "Возраст ребёнка" AS "Возраст ребёнка",
        "Район проживания" AS "Район проживания",
        Школа AS "Школа",
        Комментарий AS "Комментарий",
        "Причина отказа" AS "Причина отказа",
        "Записался на МК на" AS "Записался на МК на",
        UTM_SOURCE AS "utm_source",
        "url (NEW)" AS "url (NEW)",
        Педагог AS "Педагог",
        "Дата МК" AS "Дата МК",
        "День рождения_new" AS "День рождения_new",
        "Номер договора" AS "Номер договора",
        "Ученик в БО связан" AS "Ученик в БО связан",
        "Переведён в группу" AS "Переведён в группу",
        "Счёт в БО выставлен" AS "Счёт в БО выставлен",
        "Счёт в БО оплачен" AS "Счёт в БО оплачен",
        "Отказ 2019" AS "Отказ 2019",
        Отказ2021 AS "Отказ2021",
        "Отказ 2020" AS "Отказ 2020",
        "Source phone.1" AS "Source phone.1",
        da_id AS "da_id",
        ip AS "ip",
        UTM_TERM AS "utm_term",
        UTM_CONTENT AS "utm_content",
        UTM_MEDIUM AS "utm_medium",
        UTM_CAMPAIGN AS "utm_campaign",
        FORMID AS "FORMID",
        REFERER AS "REFERER",
        TRANID AS "TRANID",
        "Адрес страницы" AS "Адрес страницы",
        Форма AS "Форма",
        ym_client_id AS "ym_client_id",
        url AS "url",
        "Группа в АМО" AS "Группа в АМО",
        Страница AS "Страница",
        Скидка AS "Скидка",
        "Курс интересует" AS "Курс интересует",
        "Курс окончил" AS "Курс окончил",
        Площадка AS "Площадка",
        Куратор AS "Куратор",
        Курс AS "Курс",
        "Дата выбывания" AS "Дата выбывания",
        "Номер урока отсева" AS "Номер урока отсева",
        "Причина отсева" AS "Причина отсева",
        "Source phone_new" AS "Source phone (контакт)",
        "Источник трафика_new" AS "Источник трафика_new",
        "utm_source.1" AS "utm_source.1",
        "utm_campaign.1" AS "utm_campaign.1",
        "Ссылка для формы" AS "Ссылка для формы",
        "Причина отказа.1" AS "Причина отказа.1",
        "Источник заявки" AS "Источник заявки",
        "Фертильный лид" AS "Фертильный лид",
        "Реферальная прогр" AS "Реферальная прогр",
        openstat_campaign AS "openstat_campaign",
        yclid AS "yclid",
        gclid AS "gclid",
        gclientid AS "gclientid",
        "from" AS "from",
        openstat_source AS "openstat_source",
        openstat_ad AS "openstat_ad",
        fbclid AS "fbclid",
        openstat_service AS "openstat_service",
        referrer AS "referrer",
        roistat AS "roistat",
        _ym_counter AS "_ym_counter",
        _ym_uid AS "_ym_uid",
        utm_referrer AS "utm_referrer",
        "utm_content.1" AS "utm_content.1",
        "utm_term.1" AS "utm_term.1",
        "utm_campaign.2" AS "utm_campaign.2",
        "utm_medium.1" AS "utm_medium.1",
        "utm_source.2" AS "utm_source.2"
        FROM public.leads;
    ''')
    pass

def downgrade() -> None:
    # Drop leads table and dependent leads_view view
    op.execute("""
        DROP VIEW public.leads_view;
        DROP TABLE public.leads;
    """)
    # Create new leads table
    op.execute("""
        CREATE TABLE public.leads (
            id serial4 NOT NULL,
            "Название сделки" varchar(255) NULL,
            "Бюджет " float8 NULL,
            "Ответственный" varchar(255) NULL,
            "Дата создания сделки" varchar(255) NULL,
            "Кем создана сделка" varchar(255) NULL,
            "Дата редактирования" varchar(255) NULL,
            "Кем редактирована" varchar(255) NULL,
            "Дата закрытия" varchar(255) NULL,
            "Теги" varchar(255) NULL,
            "Примечание" text NULL,
            "Примечание 2" text NULL,
            "Примечание 3" text NULL,
            "Примечание 4" text NULL,
            "Примечание 5" text NULL,
            "Этап сделки" varchar(255) NULL,
            "Воронка" varchar(255) NULL,
            "Полное имя контакта" varchar(255) NULL,
            "Компания контакта" varchar(255) NULL,
            "Ответственный за контакт" varchar(255) NULL,
            "Компания" varchar(255) NULL,
            "Рабочий телефон" text NULL,
            "Рабочий прямой телефон" varchar(255) NULL,
            "Мобильный телефон" varchar(255) NULL,
            "Факс" varchar(255) NULL,
            "Домашний телефон" varchar(255) NULL,
            "Другой телефон" varchar(255) NULL,
            "Рабочий email" text NULL,
            "Личный email" varchar(255) NULL,
            "Другой email" varchar(255) NULL,
            "Source phone" varchar(255) NULL,
            "text" text NULL,
            "Ваше имя" varchar(255) NULL,
            "Телефон (NEW)" varchar(255) NULL,
            "Имя.2" varchar(255) NULL,
            "instagram" varchar(255) NULL,
            "День рождения" varchar(255) NULL,
            "Должность" varchar(255) NULL,
            "Район" varchar(255) NULL,
            "Сегмент базы" varchar(255) NULL,
            "Имена детей" varchar(255) NULL,
            "Возраст детей" varchar(255) NULL,
            "Школы детей" varchar(255) NULL,
            "Уникальный ID" varchar(255) NULL,
            "Реферал" varchar(255) NULL,
            "NPC Погашеные" float8 NULL,
            "NPC Всего" float8 NULL,
            "Источник трафика" varchar(255) NULL,
            "Трекинг" varchar(255) NULL,
            "mailchimp" varchar(255) NULL,
            "Пользовательское соглашение" varchar(255) NULL,
            "Стал клиентом" varchar(255) NULL,
            "skype" varchar(255) NULL,ICQ varchar(255) NULL,
            "jabber" varchar(255) NULL,
            "Google Talk" varchar(255) NULL,
            "msn" varchar(255) NULL,
            "Другой IM" varchar(255) NULL,
            "Cтатус в ЦОП" varchar(255) NULL,
            "Комментарий ОП" varchar(255) NULL,
            "Выбор" varchar(255) NULL,Телефон varchar(255) NULL,
            "Занимался ли ваш ребенок программированием ранее?" varchar(255) NULL,
            "Занимались ранее программированием?" varchar(255) NULL,
            "Филиал" varchar(255) NULL,
            "Куда вам отправить приглашение?" varchar(255) NULL,
            "Возраст" varchar(255) NULL,
            "Имя" varchar(255) NULL,
            "Закреплён за" varchar(255) NULL,
            "Возраст ребёнка" varchar(255) NULL,
            "Район проживания" varchar(255) NULL,
            "Школа" varchar(255) NULL,
            "Комментарий" varchar(255) NULL,
            "Причина отказа" varchar(255) NULL,
            "Записался на МК на" varchar(255) NULL,
            "utm_source" varchar(255) NULL,
            "url (NEW)" text NULL,
            "Педагог" varchar(255) NULL,
            "Дата МК" varchar(255) NULL,
            "День рождения_new" varchar(255) NULL,
            "Номер договора" varchar(255) NULL,
            "Логин" varchar(255) NULL,
            "Пароль" varchar(255) NULL,
            "Название МК (маркет)" varchar(255) NULL,
            "Мастер-класс_Дата_время" varchar(255) NULL,
            "Имя ребенка из LMS" varchar(255) NULL,
            "Фамилия ребенка из LMS" varchar(255) NULL,
            "Название курса из LMS" varchar(255) NULL,
            "Маркетинговый тип курса" varchar(255) NULL,
            "название площадки" varchar(255) NULL,
            "Адрес площадки LMS" varchar(255) NULL,
            "Преподаватель" varchar(255) NULL,
            "Название группы LMS" varchar(255) NULL,
            "дата+время группы" varchar(255) NULL,
            "Ученик в БО связан" varchar(255) NULL,
            "Переведён в группу" varchar(255) NULL,
            "Счёт в БО выставлен" varchar(255) NULL,
            "Счёт в БО оплачен" varchar(255) NULL,
            "Адрес страницы" varchar(255) NULL,
            "Отказ 2019" varchar(255) NULL,
            "Отказ2021" varchar(255) NULL,
            "Отказ 2020" varchar(255) NULL,
            "Source phone.1" varchar(255) NULL,
            "da_id" varchar(255) NULL,
            "ip" varchar(255) NULL,
            "utm_term" varchar(255) NULL,
            "utm_content" varchar(255) NULL,
            "utm_medium" varchar(255) NULL,
            utm_campaign varchar(255) NULL,
            "formid" varchar(255) NULL,
            "referer" text NULL,
            "tranid" varchar(255) NULL,
            "Форма" varchar(255) NULL,
            "ym_client_id" varchar(255) NULL,
            "url" text NULL,
            "Группа в АМО" varchar(255) NULL,
            "Страница" varchar(255) NULL,
            "Скидка" varchar(255) NULL,
            "Курс интересует" varchar(255) NULL,
            "Курс окончил" varchar(255) NULL,
            "Площадка" varchar(255) NULL,
            "Куратор" varchar(255) NULL,
            "Курс" varchar(255) NULL,
            "Дата выбывания" varchar(255) NULL,
            "Номер урока отсева" varchar(255) NULL,
            "Причина отсева" varchar(255) NULL,
            "Source phone_new" varchar(255) NULL,
            "Источник трафика_new" varchar(255) NULL,
            "utm_source.1" varchar(255) NULL,
            "utm_campaign.1" varchar(255) NULL,
            "Ссылка для формы" varchar(255) NULL,
            "Причина отказа.1" varchar(255) NULL,
            "Источник заявки" varchar(255) NULL,
            "Фертильный лид" varchar(255) NULL,
            "ITBOT" varchar(255) NULL,
            "Реферальная прогр" varchar(255) NULL,
            "openstat_campaign" varchar(255) NULL,
            "yclid" varchar(255) NULL,
            "gclid" varchar(255) NULL,
            "gclientid" varchar(255) NULL,
            "from" varchar(255) NULL,
            "openstat_source" varchar(255) NULL,
            "openstat_ad" varchar(255) NULL,
            "fbclid" varchar(255) NULL,
            "openstat_service" varchar(255) NULL,
            "referrer" varchar(255) NULL,
            "roistat" varchar(255) NULL,
            "_ym_counter" varchar(255) NULL,
            "_ym_uid" varchar(255) NULL,
            "utm_referrer" text NULL,
            "utm_content.1" varchar(255) NULL,
            "utm_term.1" varchar(255) NULL,
            "utm_campaign.2" varchar(255) NULL,
            "utm_medium.1" varchar(255) NULL,
            "utm_source.2" varchar(255) NULL
        );
    """)

    op.execute('''
    CREATE VIEW public.leads_view AS
        SELECT id AS "id",
        "Название сделки" AS "Название сделки",
        "Бюджет " AS "Бюджет ",
        Ответственный AS "Ответственный",
        COALESCE(TO_DATE("Дата создания сделки", 'DD.MM.YYYY'), NULL) AS "Дата создания",
        "Кем создана сделка" AS "Кем создана сделка",
        COALESCE(TO_DATE("Дата редактирования", 'DD.MM.YYYY'), NULL) AS "Дата редактирования",
        "Кем редактирована" AS "Кем редактирована",
        CASE
            WHEN "Дата закрытия" = 'не закрыта' THEN NULL
            ELSE COALESCE(TO_DATE("Дата закрытия", 'DD.MM.YYYY'), NULL)
        END AS "Дата закрытия",
        Теги AS "Теги сделки",
        Примечание AS "Примечание",
        "Примечание 2" AS "Примечание 2",
        "Примечание 3" AS "Примечание 3",
        "Примечание 4" AS "Примечание 4",
        "Примечание 5" AS "Примечание 5",
        "Этап сделки" AS "Этап сделки",
        Воронка AS "Воронка",
        "Полное имя контакта" AS "Полное имя контакта",
        "Компания контакта" AS "Компания контакта",
        "Ответственный за контакт" AS "Ответственный за контакт",
        Компания AS "Компания",
        "Рабочий телефон" AS "Рабочий телефон",
        "Рабочий прямой телефон" AS "Рабочий прямой телефон",
        "Мобильный телефон" AS "Мобильный телефон",
        Факс AS "Факс",
        "Домашний телефон" AS "Домашний телефон",
        "Другой телефон" AS "Другой телефон",
        "Рабочий email" AS "Рабочий email",
        "Личный email" AS "Личный email",
        "Другой email" AS "Другой email",
        "Source phone" AS "Source phone",
        text AS "text",
        "Ваше имя" AS "Ваше имя",
        "Телефон (NEW)" AS "Телефон (NEW)",
        Instagram AS "Instagram",
        "День рождения" AS "День рождения",
        Должность AS "Должность",
        Район AS "Район",
        "Сегмент базы" AS "Сегмент базы",
        "Имена детей" AS "Имена детей",
        "Возраст детей" AS "Возраст детей",
        "Школы детей" AS "Школы детей",
        "Уникальный ID" AS "Уникальный ID",
        Реферал AS "Реферал",
        "NPC Погашеные" AS "NPC Погашеные",
        "NPC Всего" AS "NPC Всего",
        "Источник трафика" AS "Источник трафика",
        Трекинг AS "Трекинг",
        MailChimp AS "MailChimp",
        "Пользовательское соглашение" AS "Пользовательское соглашение",
        "Стал клиентом" AS "Стал клиентом",
        Skype AS "Skype",
        ICQ AS "ICQ",
        Jabber AS "Jabber",
        "Google Talk" AS "Google Talk",
        MSN AS "MSN",
        "Другой IM" AS "Другой IM",
        "Куда вам отправить приглашение?" AS "Куда вам отправить приглашение?",
        Выбор AS "Выбор",
        "Занимался ли ваш ребенок программированием ранее?" AS "Занимался ли ваш ребенок программированием ранее?",
        Возраст AS "Возраст",
        Телефон AS "Телефон",
        Имя AS "Имя",
        "Закреплён за" AS "Закреплён за",
        "Возраст ребёнка" AS "Возраст ребёнка",
        "Район проживания" AS "Район проживания",
        Школа AS "Школа",
        Комментарий AS "Комментарий",
        "Причина отказа" AS "Причина отказа",
        "Записался на МК на" AS "Записался на МК на",
        UTM_SOURCE AS "utm_source",
        "url (NEW)" AS "url (NEW)",
        Педагог AS "Педагог",
        "Дата МК" AS "Дата МК",
        "День рождения_new" AS "День рождения_new",
        "Номер договора" AS "Номер договора",
        "Ученик в БО связан" AS "Ученик в БО связан",
        "Переведён в группу" AS "Переведён в группу",
        "Счёт в БО выставлен" AS "Счёт в БО выставлен",
        "Счёт в БО оплачен" AS "Счёт в БО оплачен",
        "Отказ 2019" AS "Отказ 2019",
        Отказ2021 AS "Отказ2021",
        "Отказ 2020" AS "Отказ 2020",
        "Source phone.1" AS "Source phone.1",
        da_id AS "da_id",
        ip AS "ip",
        UTM_TERM AS "utm_term",
        UTM_CONTENT AS "utm_content",
        UTM_MEDIUM AS "utm_medium",
        UTM_CAMPAIGN AS "utm_campaign",
        FORMID AS "FORMID",
        REFERER AS "REFERER",
        TRANID AS "TRANID",
        "Адрес страницы" AS "Адрес страницы",
        Форма AS "Форма",
        ym_client_id AS "ym_client_id",
        url AS "url",
        "Группа в АМО" AS "Группа в АМО",
        Страница AS "Страница",
        Скидка AS "Скидка",
        "Курс интересует" AS "Курс интересует",
        "Курс окончил" AS "Курс окончил",
        Площадка AS "Площадка",
        Куратор AS "Куратор",
        Курс AS "Курс",
        "Дата выбывания" AS "Дата выбывания",
        "Номер урока отсева" AS "Номер урока отсева",
        "Причина отсева" AS "Причина отсева",
        "Source phone_new" AS "Source phone (контакт)",
        "Источник трафика_new" AS "Источник трафика_new",
        "utm_source.1" AS "utm_source.1",
        "utm_campaign.1" AS "utm_campaign.1",
        "Ссылка для формы" AS "Ссылка для формы",
        "Причина отказа.1" AS "Причина отказа.1",
        "Источник заявки" AS "Источник заявки",
        "Фертильный лид" AS "Фертильный лид",
        "Реферальная прогр" AS "Реферальная прогр",
        openstat_campaign AS "openstat_campaign",
        yclid AS "yclid",
        gclid AS "gclid",
        gclientid AS "gclientid",
        "from" AS "from",
        openstat_source AS "openstat_source",
        openstat_ad AS "openstat_ad",
        fbclid AS "fbclid",
        openstat_service AS "openstat_service",
        referrer AS "referrer",
        roistat AS "roistat",
        _ym_counter AS "_ym_counter",
        _ym_uid AS "_ym_uid",
        utm_referrer AS "utm_referrer",
        "utm_content.1" AS "utm_content.1",
        "utm_term.1" AS "utm_term.1",
        "utm_campaign.2" AS "utm_campaign.2",
        "utm_medium.1" AS "utm_medium.1",
        "utm_source.2" AS "utm_source.2"
        FROM public.leads;
    ''')
    pass