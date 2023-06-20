from download import download_and_update
import paths
import sys

def main(args):
    parameter_sets = {
        "events_full":{"csv_url":paths.bo_csv_url_events,"output_path":paths.output_path_events,"table_name":"EVENTS FULL","script_path":paths.script_refresh_db_events},
        "groups_full":{"csv_url":paths.bo_csv_url_groups,"output_path":paths.output_path_groups,"table_name":"GROUPS FULL","script_path":paths.script_refresh_db_groups},
        "invoices_full":{"csv_url":paths.bo_csv_url_invoices,"output_path":paths.output_path_invoices,"table_name":"INVOICES FULL","script_path":paths.script_refresh_db_invoices},
        "students_full":{"csv_url":paths.bo_csv_url_students,"output_path":paths.output_path_students,"table_name":"STUDENTS FULL","script_path":paths.script_refresh_db_students},
        "events_filter":{"csv_url":paths.bo_csv_url_events_filter,"output_path":paths.output_path_events_filter,"table_name":"EVENTS FILTER","script_path":None}, #TODO Add the script
        "invoices_filter":{"csv_url":paths.bo_csv_url_invoices_filter,"output_path":paths.output_path_invoices_filter,"table_name":"INVOICES FILTER","script_path":None}, #TODO Add the script
        "students_filter":{"csv_url":paths.bo_csv_url_students_filter,"output_path":paths.output_path_students_filter,"table_name":"STUDENTS FILTER","script_path":None} #TODO Add the script
    }

    if len(args) == 2:
        set_name = args[1]
        if set_name in parameter_sets:
            print("Updating "+parameter_sets[set_name]["table_name"])
            result = download_and_update(**parameter_sets[set_name])
        else:
            print(f"Parameter set '{set_name}' not found")
    else:
        print("Usage: python my_script.py <parameter_set_name>")

if __name__ == '__main__':
    main(sys.argv)    