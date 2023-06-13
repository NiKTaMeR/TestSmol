import os
import pandas as pd
from tkinter import filedialog, Tk
from openpyxl import load_workbook

def ingest_data():
    root = Tk()
    root.withdraw()

    file_types = [("Excel files", "*.xlsx"), ("Access Database", "*.accdb")]
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=file_types)

    if file_path.endswith(".xlsx"):
        raw_data = pd.read_excel(file_path)
    elif file_path.endswith(".accdb"):
        import pyodbc
        conn_str = (
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
            f"DBQ={file_path};"
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        table_name = cursor.tables().fetchone().table_name
        raw_data = pd.read_sql(f"SELECT * FROM {table_name}", conn)
        conn.close()
    else:
        raise ValueError("Invalid file type. Please select an Excel or Access file.")

    return raw_data, file_path