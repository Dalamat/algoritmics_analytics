import logging
import os

log_folder = 'logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Create formatters for the handlers
formatter_default = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
formatter_debug =logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(funcName)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Create a handler to save chosen logs to the logs.txt file
file_handler = logging.FileHandler(os.path.join(log_folder, 'logs.log'))
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter_default)

# Create a handler to print the chosen logs in console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter_default)

# Create a handler to save all logs to the debug_logs.txt file and print in the console
debug_handler = logging.FileHandler(os.path.join(log_folder, 'debug_logs.log'))
debug_handler.setLevel(logging.DEBUG)  # Set the level to capture all logs
debug_handler.setFormatter(formatter_debug)

# Configure the root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Set the root logger level to capture all logs
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(debug_handler) # Uncomment this line to enable the debug logger