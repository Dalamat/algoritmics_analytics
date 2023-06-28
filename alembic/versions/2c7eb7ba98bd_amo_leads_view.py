"""AMO Leads View

Revision ID: 2c7eb7ba98bd
Revises: daa581934307
Create Date: 2023-06-28 18:35:25.216052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c7eb7ba98bd'
down_revision = 'daa581934307'
branch_labels = None
depends_on = None


def upgrade() -> None:
    #Create leads_view
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
    op.execute('''
        DROP VIEW public.leads_view
    ''')
    pass
