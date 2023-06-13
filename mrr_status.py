import pandas as pd
from openpyxl import load_workbook
from datetime import datetime
from config import threshold_contraction, threshold_upsell

def create_mrr_status_table(input_file, output_file):
    # Load input file
    df = pd.read_excel(input_file, sheet_name="MRR Per Client", index_col=0)

    # Initialize MRR Status DataFrame
    mrr_status = pd.DataFrame(index=df.index)

    # Iterate through months
    for i in range(1, len(df.columns)):
        current_month = df.columns[i]
        previous_month = df.columns[i - 1]

        # Calculate MRR Status for each client
        mrr_status[current_month] = df.apply(
            lambda row: calculate_mrr_status(row[previous_month], row[current_month]), axis=1
        )

    # Save MRR Status DataFrame to output file
    with pd.ExcelWriter(output_file, engine="openpyxl", mode="a") as writer:
        mrr_status.to_excel(writer, sheet_name="MRR Status")

def calculate_mrr_status(previous_month_billing, current_month_billing):
    if previous_month_billing == 0 and current_month_billing > 0:
        return "New Logo"
    elif previous_month_billing > 0 and current_month_billing == 0:
        return "Churned"
    elif previous_month_billing == current_month_billing:
        return "Stable"
    elif current_month_billing > previous_month_billing * (1 - threshold_upsell):
        return "Upsell"
    elif current_month_billing < previous_month_billing * (1 - threshold_contraction):
        return "Contraction"
    else:
        return "Stable"