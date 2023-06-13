import tkinter as tk
from tkinter import filedialog
import data_ingestion
import data_parsing
import mrr_per_client
import mrr_status
import logging_functions

class SaaSMetricsCalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("SaaS Metrics Calculator")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.ingest_data_button = tk.Button(self, text="Ingest Data", command=self.ingest_data)
        self.ingest_data_button.pack(pady=10)

        self.parse_information_button = tk.Button(self, text="Parse Information", command=self.parse_information)
        self.parse_information_button.pack(pady=10)

        self.mrr_per_client_button = tk.Button(self, text="Create MRR Per Client Table", command=self.create_mrr_per_client_table)
        self.mrr_per_client_button.pack(pady=10)

        self.mrr_status_button = tk.Button(self, text="Create MRR Status Table", command=self.create_mrr_status_table)
        self.mrr_status_button.pack(pady=10)

    def ingest_data(self):
        file_type = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("Access Database", "*.accdb")])
        data_ingestion.ingest_data(file_type)

    def parse_information(self):
        data_parsing.parse_information()

    def create_mrr_per_client_table(self):
        mrr_per_client.create_mrr_per_client_table()

    def create_mrr_status_table(self):
        mrr_status.create_mrr_status_table()

if __name__ == "__main__":
    app = SaaSMetricsCalculatorGUI()
    app.mainloop()