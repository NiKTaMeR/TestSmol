import tkinter as tk
from tkinter import filedialog
import data_ingestion
import data_parsing
import mrr_per_client
import mrr_status
import error_handling
import logging_functions

def main():
    root = tk.Tk()
    root.title("SaaS Metrics Calculator")

    def ingest_data():
        file_type = file_type_var.get()
        file_path = filedialog.askopenfilename()
        data_ingestion.ingest_data(file_type, file_path)

    def parse_information():
        output_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
        data_parsing.parse_information(output_path)

    def create_mrr_per_client_table():
        mrr_per_client.create_mrr_per_client_table()

    def create_mrr_status_table():
        mrr_status.create_mrr_status_table()

    file_type_var = tk.StringVar(root)
    file_type_var.set("Excel")

    file_type_label = tk.Label(root, text="Select file type:")
    file_type_label.grid(row=0, column=0)

    file_type_option_menu = tk.OptionMenu(root, file_type_var, "Excel", "Access")
    file_type_option_menu.grid(row=0, column=1)

    ingest_data_button = tk.Button(root, text="Ingest Data", command=ingest_data)
    ingest_data_button.grid(row=1, column=0, columnspan=2)

    parse_information_button = tk.Button(root, text="Parse Information", command=parse_information)
    parse_information_button.grid(row=2, column=0, columnspan=2)

    mrr_per_client_button = tk.Button(root, text="Create MRR Per Client Table", command=create_mrr_per_client_table)
    mrr_per_client_button.grid(row=3, column=0, columnspan=2)

    mrr_status_button = tk.Button(root, text="Create MRR Status Table", command=create_mrr_status_table)
    mrr_status_button.grid(row=4, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()