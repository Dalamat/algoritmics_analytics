import os
import envs
import url_generator

#Specify urls for LMS (BO)
bo_auth_url = "https://backoffice.algoritmika.org/s/auth/api/e/user/auth"
bo_csv_url_events = "https://backoffice.algoritmika.org/group/default/schedule?timeframe=all&export=true&name=default&exportType=csv"
bo_csv_url_groups = "https://backoffice.algoritmika.org/group?export=true&name=default&exportType=csv"
bo_csv_url_invoices = "https://backoffice.algoritmika.org/payment/manage/invoices?export=true&name=default&exportType=csv"
bo_csv_url_students = "https://backoffice.algoritmika.org/student?export=true&name=default&exportType=csv"
bo_csv_url_events_filter = "https://backoffice.algoritmika.org/group/default/schedule?GroupLessonSearch%5Bgroup.status%5D%5B%5D=active&GroupLessonSearch%5Bgroup.status%5D%5B%5D=recruiting&timeframe=all&export=true&name=default&exportType=csv"
bo_csv_url_invoices_filter = url_generator.bo_csv_url_invoices_filter
bo_csv_url_students_filter = url_generator.bo_csv_url_students_filter

# Get environment varibales
root_floder = envs.root_folder
active_folder = envs.active_folder

# Generate paths for the source files
events_csv_path = os.path.join(active_folder, envs.file_events)
groups_csv_path = os.path.join(active_folder, envs.file_groups)
students_csv_path = os.path.join(active_folder, envs.file_students)
invoices_csv_path = os.path.join(active_folder, envs.file_invoices)
events_filter_csv_path = os.path.join(active_folder, envs.file_events_filter)
students_filter_csv_path = os.path.join(active_folder,envs.file_students_filter)
invoices_filter_csv_path = os.path.join(active_folder, envs.file_invoices_filter)

#Generate paths for the database refresh scripts
script_refresh_db_events = os.path.join(root_floder,"db_scripts", "refresh_db_events_check_errors.py")
script_refresh_db_groups = os.path.join(root_floder,"db_scripts","refresh_db_groups_check_errors.py")
script_refresh_db_invoices = os.path.join(root_floder,"db_scripts","refresh_db_invoices_check_errors.py")
script_refresh_db_students = os.path.join(root_floder,"db_scripts","refresh_db_students_check_errors.py")
script_update_db_events = os.path.join(root_floder,"db_scripts","update_db_events_check_errors.py")
script_update_db_invoices = os.path.join(root_floder,"db_scripts","update_db_invoices_check_errors.py")

#Generate output paths
output_path_events = os.path.join(active_folder,envs.file_events)
output_path_groups = os.path.join(active_folder,envs.file_groups)
output_path_invoices = os.path.join(active_folder,envs.file_invoices)
output_path_students = os.path.join(active_folder,envs.file_students)
output_path_events_filter = os.path.join(active_folder,envs.file_events_filter)
output_path_invoices_filter = os.path.join(active_folder,envs.file_invoices_filter)
output_path_students_filter = os.path.join(active_folder,envs.file_students_filter)