import logging
from logging_functions import log_error

def handle_file_error(error):
    log_error(f"File error: {error}")
    print("An error occurred while processing the file. Please check the file format and try again.")

def handle_data_error(error):
    log_error(f"Data error: {error}")
    print("An error occurred while processing the data. Please ensure the data is in the correct format and try again.")

def handle_excel_error(error):
    log_error(f"Excel error: {error}")
    print("An error occurred while working with the Excel file. Please ensure the file is not open in another program and try again.")

def handle_access_error(error):
    log_error(f"Access error: {error}")
    print("An error occurred while working with the Access Database. Please ensure the file is not open in another program and try again.")

def handle_general_error(error):
    log_error(f"General error: {error}")
    print("An unexpected error occurred. Please try again.")