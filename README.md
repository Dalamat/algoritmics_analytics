# algoritmics_analytics
This project allows to:
* connect, fetch, and upload data to a self-hosted PostgreSQL database from:
  * Algorithmics LMS
  * AMO CRM
  * Google Spreadsheets
* connect the pre-configured PowerBI templates to the database
* enjoy auto-updating insightful analytics
* get regular status updates on Telegram

<h2>Installation</h2>
<h3>Windows</h3>

* Install Python - in this project the version is fixed to 3.11.4
  * Install pipenv
  * Install alembic
* Configure Database
  * Install PostgreSQL - the app has been tested with v.11 and v.15
  * Install npgsql driver v4.0.10 - this is requered for PowerBi to remotely fetch the data from the PostgreSQL DB
    * https://github.com/npgsql/npgsql/releases/tag/v4.0.10
    * Make sure to enable GAC Installation in the wizard
  * Create a new DB (Optional)
* Install GIT for Windows
* Install VS Code (Optional)
* Install DBeaver (Optional)
* Create Google Service Account
  * https://docs.gspread.org/en/latest/oauth2.html#enable-api-access
  * Save a key as a json file

* Configure the project
  * initialize pipenv
    * pipenv --python "path to 3.11.4 python.exe"
    * pipenv install
    * pipenv shell
  * Set environmental variables
    * Update set_env_var.bat
    * Run it
  * Set folders in envs.py
    * Create active_folder if necessary
  * Set DB details for squlalchemy.url in alembic.ini
  * Upgrade the DB up to the latest migrations
    * alembic upgrade head
* Copy google key json to \gcp_sa_key.json
* Create a task in Task Scheduler (Optional)
  * Name - algoritmics_analytics
  * Run only when user is logged in
  * Trigger - At startup
  * Action - Start a program
    * %\algoritmics_analytics\run.bat
    * %\algoritmics_analytics
* Execute run.bat

* Connect Power BI
  * Install Power BI On-premis Data Gateway
  * Install Power BI Desktop