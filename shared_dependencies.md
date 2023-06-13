the app is: SaaS Metrics Calculator

the files we have decided to generate are: main.py, config.py, data_ingestion.py, data_parsing.py, mrr_per_client.py, mrr_status.py, gui.py, requirements.txt

Shared dependencies:
1. Exported variables:
   - threshold_contraction
   - threshold_upsell

2. Data schemas:
   - Raw transaction data schema (Excel/Access)
   - Input_Variables schema (Excel)
   - MRR Per Client schema (Excel)
   - MRR Status schema (Excel)

3. Function names:
   - ingest_data()
   - parse_information()
   - create_mrr_per_client_table()
   - create_mrr_status_table()

4. Message names:
   - "Now opening the excel file, fill in the monthly results, save and close the file, before coming back here"
   - "I'm done with the results, go ahead."

5. DOM element id names (for JavaScript functions, if applicable):
   - file_type_selection
   - file_upload_button
   - input_variables_button
   - mrr_per_client_button
   - mrr_status_button