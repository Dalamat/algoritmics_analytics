import paths
import login
import asyncio
from download import download_file
from db_scripts_controller import db_scripts
from telegram_client import send_group_message


PARAMETER_SETS = {
    "events_full": {"csv_url":paths.bo_csv_url_events,"output_path":paths.output_path_events,"table_name":"EVENTS FULL","db_script_function":"refresh_db_events","send_messages":True},
    "groups_full":{"csv_url":paths.bo_csv_url_groups,"output_path":paths.output_path_groups,"table_name":"GROUPS FULL","db_script_function":"refresh_db_groups","send_messages":True},
    "invoices_full":{"csv_url":paths.bo_csv_url_invoices,"output_path":paths.output_path_invoices,"table_name":"INVOICES FULL","db_script_function":"refresh_db_invoices","send_messages":True},
    "students_full":{"csv_url":paths.bo_csv_url_students,"output_path":paths.output_path_students,"table_name":"STUDENTS FULL","db_script_function":"refresh_db_students","send_messages":True},
    "events_filter":{"csv_url":paths.bo_csv_url_events_filter,"output_path":paths.output_path_events_filter,"table_name":"EVENTS UPDATES","db_script_function":"update_db_events","send_messages":True},
    "invoices_filter":{"csv_url":paths.bo_csv_url_invoices_filter,"output_path":paths.output_path_invoices_filter,"table_name":"INVOICES UPDATES","db_script_function":"update_db_invocies","send_messages":True},
    "students_filter":{"csv_url":paths.bo_csv_url_students_filter,"output_path":paths.output_path_students_filter,"table_name":"STUDENTS UPDATES","db_script_function":"update_db_students","send_messages":True},
    "events_full_silent": {"csv_url":paths.bo_csv_url_events,"output_path":paths.output_path_events,"table_name":"EVENTS FULL","db_script_function":"refresh_db_events","send_messages":False},
    "groups_full_silent":{"csv_url":paths.bo_csv_url_groups,"output_path":paths.output_path_groups,"table_name":"GROUPS FULL","db_script_function":"refresh_db_groups","send_messages":False},
    "invoices_full_silent":{"csv_url":paths.bo_csv_url_invoices,"output_path":paths.output_path_invoices,"table_name":"INVOICES FULL","db_script_function":"refresh_db_invoices","send_messages":False},
    "students_full_silent":{"csv_url":paths.bo_csv_url_students,"output_path":paths.output_path_students,"table_name":"STUDENTS FULL","db_script_function":"refresh_db_students","send_messages":False},
    "events_filter_silent":{"csv_url":paths.bo_csv_url_events_filter,"output_path":paths.output_path_events_filter,"table_name":"EVENTS UPDATES","db_script_function":"update_db_events","send_messages":False},
    "invoices_filter_silent":{"csv_url":paths.bo_csv_url_invoices_filter,"output_path":paths.output_path_invoices_filter,"table_name":"INVOICES UPDATES","db_script_function":"update_db_invocies","send_messages":False},
    "students_filter_silent":{"csv_url":paths.bo_csv_url_students_filter,"output_path":paths.output_path_students_filter,"table_name":"STUDENTS UPDATES","db_script_function":"update_db_students","send_messages":False}
}


def update_table(csv_url, output_path, table_name, db_script_function,send_messages=True):
    session = login.get_authenticated_session()
    if session:
        print(f"Download started. {table_name}")
        if send_messages:
            asyncio.run(send_group_message(table_name+" "+"Started*"))
        attempt = 1
        while attempt <= 5:
            print(f"Attempt {attempt}")
            if download_file(session,csv_url,output_path):
                print(f"Proceed to DB update. {table_name}")
                if db_scripts(db_script_function):
                    print(f"Table updated successfully. {table_name}")
                    if send_messages:
                        asyncio.run(send_group_message(table_name+" "+"Updated*"))
                else:
                    print(f"Table update failed. {table_name}")                    
                    if send_messages:
                        asyncio.run(send_group_message(table_name+" "+"Script Failed*"))
                break
            else:
                print(f"Attempt {attempt}. Download failed. {table_name}")
                attempt += 1
        else:
            print(f"Download stopped after {attempt} attempts. {table_name}")
            if send_messages:
                asyncio.run(send_group_message(table_name+" "+"Download Failed*"))
    session.close()

# Test run
# update_table(**PARAMETER_SETS["invoices_filter_silent"])