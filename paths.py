import os
import envs

#LMS (BO) urls
bo_auth_url = "https://backoffice.algoritmika.org/s/auth/api/e/user/auth"
bo_check_url = "https://backoffice.algoritmika.org/dashboard/default/partner"
bo_csv_url_events = "https://backoffice.algoritmika.org/group/default/schedule?timeframe=all&export=true&name=default&exportType=csv"
bo_csv_url_groups = "https://backoffice.algoritmika.org/group?export=true&name=default&exportType=csv"
bo_csv_url_invoices = "https://backoffice.algoritmika.org/payment/manage/invoices?export=true&name=default&exportType=csv"
bo_csv_url_students = "https://backoffice.algoritmika.org/student?export=true&name=default&exportType=csv"
bo_csv_url_payments = "https://backoffice.algoritmika.org/payment/manage?export=true&name=default&exportType=csv"
bo_csv_url_events_filter = "https://backoffice.algoritmika.org/group/default/schedule?GroupLessonSearch%5Bgroup.status%5D%5B%5D=active&GroupLessonSearch%5Bgroup.status%5D%5B%5D=recruiting&timeframe=all&export=true&name=default&exportType=csv"

# Get environment varibales
root_floder = envs.root_folder
active_folder = envs.active_folder

# Generate paths for the source and output files
events_csv_path = os.path.join(active_folder, envs.file_events)
groups_csv_path = os.path.join(active_folder, envs.file_groups)
invoices_csv_path = os.path.join(active_folder, envs.file_invoices)
students_csv_path = os.path.join(active_folder, envs.file_students)
events_filter_csv_path = os.path.join(active_folder, envs.file_events_filter)
invoices_filter_csv_path = os.path.join(active_folder, envs.file_invoices_filter)
invoices_filter_2_csv_path = os.path.join(active_folder, envs.file_invoices_filter_2)
students_filter_csv_path = os.path.join(active_folder,envs.file_students_filter)
leads_csv_path = os.path.join(active_folder, envs.file_leads)
budgets_csv_path = os.path.join(active_folder, envs.file_budgets)
payments_csv_path = os.path.join(active_folder, envs.file_payments)
payments_filter_csv_path = os.path.join(active_folder, envs.file_payments_filter)