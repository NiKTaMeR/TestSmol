import pandas as pd
import numpy as np
import openpyxl
from datetime import datetime
from dateutil.relativedelta import relativedelta

def create_mrr_per_client_table(input_file, output_file):
    # Read input data
    df = pd.read_excel(input_file)

    # Extract unique client names
    unique_clients = df['Client'].unique()

    # Find earliest and latest transaction dates
    earliest_date = df['Date'].min()
    latest_date = df['Date'].max()

    # Create a list of all months between earliest and latest transaction dates
    all_months = []
    current_month = earliest_date.replace(day=1)
    while current_month <= latest_date:
        all_months.append(current_month.strftime('%m/%Y'))
        current_month += relativedelta(months=1)

    # Initialize MRR Per Client DataFrame
    mrr_per_client = pd.DataFrame(columns=['Logo', 'Cohort Month'] + all_months)
    mrr_per_client['Logo'] = unique_clients

    # Calculate Cohort Month and MRR values for each client
    for client in unique_clients:
        client_data = df[df['Client'] == client]
        cohort_month = client_data['Date'].min().strftime('%m/%Y')
        mrr_per_client.loc[mrr_per_client['Logo'] == client, 'Cohort Month'] = cohort_month

        for month in all_months:
            month_start = datetime.strptime(month, '%m/%Y')
            month_end = month_start + relativedelta(months=1) - relativedelta(days=1)
            monthly_revenue = client_data[(client_data['Date'] >= month_start) & (client_data['Date'] <= month_end)]['Revenue'].sum()
            mrr_per_client.loc[mrr_per_client['Logo'] == client, month] = monthly_revenue

    # Write MRR Per Client table to output Excel file
    with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
        mrr_per_client.to_excel(writer, sheet_name='MRR Per Client', index=False)