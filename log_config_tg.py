import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

log_folder = 'logs_tg'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Create formatters for the handlers
formatter_default = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
formatter_debug =logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(funcName)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Create a handler to save chosen logs to the logs.txt file
log_file_path = os.path.join(log_folder, 'logs.log')
file_handler_tg = TimedRotatingFileHandler(log_file_path, when="midnight", interval=1, backupCount=5)
file_handler_tg.setLevel(logging.INFO)
file_handler_tg.setFormatter(formatter_default)

# Create a handler to print the chosen logs in console
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
# console_handler.setFormatter(formatter_default)

# Create a handler to save all logs to the debug_logs.txt file and print in the console
debug_handler_tg = logging.FileHandler(os.path.join(log_folder, 'debug_logs.log'), delay=True)
debug_handler_tg.setLevel(logging.DEBUG)  # Set the level to capture all logs
debug_handler_tg.setFormatter(formatter_debug)

# Configure the root logger
logger_tg = logging.getLogger()
logger_tg.setLevel(logging.DEBUG)  # Set the root logger level to capture all logs
logger_tg.addHandler(file_handler_tg)
# logger.addHandler(console_handler)
# logger.addHandler(debug_handler) # Uncomment this line to enable the debug logger
logging.getLogger("httpx").setLevel(logging.WARNING)
# logger_tg.propagate = False  # Prevent log events from being passed to the parent loggers