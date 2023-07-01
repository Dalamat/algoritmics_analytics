import gspread
from oauth2client.service_account import ServiceAccountCredentials
import envs
from log_config import logger

# Define the path to your credentials JSON file
credentials_file = envs.gcp_credentials_file

# Define the ID of your Google Spreadsheet
spreadsheet_id = envs.gcp_spreadsheet_id

# Define the name of the sheet from which you want to download data
sheet_name = envs.gcp_sheet_name


def gcp_get_values():
    try:
        # Set up authentication using the credentials file
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        client = gspread.authorize(credentials)

        # Open the specified spreadsheet and sheet
        spreadsheet = client.open_by_key(spreadsheet_id)
        sheet = spreadsheet.worksheet(sheet_name)

        # Get all the values from the sheet
        values = sheet.get_all_values()
        return values
    except Exception as e:
        logger.error(f"Error: {e}")
        return False


# print(gcp_get_values())