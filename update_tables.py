import sys
import envs
import paths
import asyncio
from download import download_file
from db_scripts_controller import db_scripts
from telegram_client import send_group_message
from log_config import logger
from url_generator import get_urls


PARAMETER_SETS = {
    "events_full": {"output_path":paths.events_csv_path,"table_name":"EVENTS FULL","db_script_function":"refresh_db_events"},
    "groups_full":{"output_path":paths.groups_csv_path,"table_name":"GROUPS FULL","db_script_function":"refresh_db_groups"},
    "invoices_full":{"output_path":paths.invoices_csv_path,"table_name":"INVOICES FULL","db_script_function":"refresh_db_invoices"},
    "students_full":{"output_path":paths.students_csv_path,"table_name":"STUDENTS FULL","db_script_function":"refresh_db_students"},
    "payments_full":{"output_path":paths.payments_csv_path,"table_name":"PAYMENTS FULL","db_script_function":"refresh_db_payments"},
    "events_filter":{"output_path":paths.events_filter_csv_path,"table_name":"EVENTS UPDATES","db_script_function":"update_db_events"},
    "invoices_filter":{"output_path":paths.invoices_filter_csv_path,"table_name":"INVOICES UPDATES","db_script_function":"update_db_invocies"},
    "invoices_filter_2":{"output_path":paths.invoices_filter_2_csv_path,"table_name":"INVOICES UPDATES_2","db_script_function":"update_db_invocies_2"},
    "students_filter":{"output_path":paths.students_filter_csv_path,"table_name":"STUDENTS UPDATES","db_script_function":"update_db_students"},
    "payments_filter":{"output_path":paths.payments_filter_csv_path,"table_name":"PAYMENTS UPDATES","db_script_function":"update_db_payments"},
    "leads_full":{"output_path":paths.leads_csv_path,"table_name":"LEADS FULL","db_script_function":"refresh_db_leads","source":"AMO"},
    "budgets_full":{"output_path":paths.budgets_csv_path,"table_name":"BUDGETS FULL","db_script_function":"refresh_db_budgets","source":"GCP"}
}

def run_coroutine(coroutine):
    loop = asyncio.get_event_loop()
    if loop.is_running():
        loop.create_task(coroutine)
    else:
        loop.run_until_complete(coroutine)

def update_table(output_path, table_name, db_script_function, source="BO", send_messages=True):
    # run_coroutine(send_group_message(f"{table_name} Started"))
    csv_url = get_urls(table_name)
    logger.info(f"Download started. Table: {table_name} | URL: {csv_url}")
    attempt = 1
    while attempt <= 5:
        logger.debug(f"Attempt {attempt}")
        if download_file(csv_url,output_path, source):
            logger.info(f"Proceed to DB update. {table_name}")
            if db_scripts(db_script_function):
                logger.info(f"Table updated successfully. {table_name}")
                return True
            else:
                logger.error(f"Table update failed. {table_name}")
                if send_messages:
                    message = f"{table_name}. Script Failed. ENV: {envs.environment}. Attention: {envs.telegram_mentions}"
                    run_coroutine(send_group_message(message))
                return False
        else:
            logger.warning(f"Attempt {attempt}. Download failed. {table_name}")
            attempt += 1
    else:
        logger.error(f"Download stopped after {attempt-1} attempts. {table_name}")
        if send_messages:
            message = f"{table_name}. Download Failed. ENV: {envs.environment}. Attention: {envs.telegram_mentions}"
            run_coroutine(send_group_message(message))
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parameter_set_name = sys.argv[1]
        if parameter_set_name in PARAMETER_SETS:
            update_table(**PARAMETER_SETS[parameter_set_name])
        else:
            print(f"Invalid parameter set name: {parameter_set_name}")
    else:
        print("Usage: python your_script_name.py [events_full|groups_full|invoices_full|students_full|payments_full|events_filter|invoices_filter|invoices_filter_2|students_filter|payments_filter|leads_full|budgets_full]")


# Test run
# update_table(**PARAMETER_SETS["events_full"])
# update_table(**PARAMETER_SETS["groups_full"])
# update_table(**PARAMETER_SETS["invoices_full"])
# update_table(**PARAMETER_SETS["students_full"])
# update_table(**PARAMETER_SETS["events_filter"])
# update_table(**PARAMETER_SETS["invoices_filter"])
# update_table(**PARAMETER_SETS["invoices_filter_2"])
# update_table(**PARAMETER_SETS["students_filter"])
# update_table(**PARAMETER_SETS["leads_full"])
# update_table(**PARAMETER_SETS["budgets_full"])
# update_table(**PARAMETER_SETS["payments_full"])
# update_table(**PARAMETER_SETS["payments_filter"])