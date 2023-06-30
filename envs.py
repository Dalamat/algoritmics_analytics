import os

#Please create OS environmental variables for the secrets or populate them directly
#Adjust root_folder and active_folder based on your preferences

#Folders
root_folder = "C:\\Cream\\algoritmics_analytics\\"
active_folder = "C:\\Cream\\Active\\"

#Source files names
file_events = "Events.csv"
file_groups = "Groups.csv"
file_invoices = "Invoices.csv"
file_students = "Students.csv"
file_events_filter = "Events_Updates.csv"
file_invoices_filter = "Invoices_Updates.csv"
file_students_filter = "Students_Updates.csv"
file_leads = "Leads.csv"
file_budgets = "Budgets.csv"

#DB Connection
database = os.environ.get("database")
db_user = os.environ.get("db_user")
db_password = os.environ.get("db_password")
db_host = "localhost"
db_port = "5432"

#Backoffice account
bo_login = os.environ.get("bo_login")
bo_password = os.environ.get("bo_password")

#AMO CRM accounts
amo_login = os.environ.get('amo_email')
amo_password = os.environ.get('amo_password')
amo_host = os.environ.get('amo_host')

#Google Spreadsheets Access
# Define the path to your credentials JSON file
gcp_credentials_file = 'gcp_sa_key.json'
# Define the ID of your Google Spreadsheet
gcp_spreadsheet_id = os.environ.get('gcp_spreadsheet_id')
# Define the name of the sheet from which you want to download data
gcp_sheet_name = 'Default'

#Telegram
telegram_bot_token = os.environ.get("telegram_bot_token")
telegram_group = os.environ.get("telegram_group")
telegram_mentions = os.environ.get("telegram_mentions") # Use @Telegram mentions for the tagged notification for the update failures