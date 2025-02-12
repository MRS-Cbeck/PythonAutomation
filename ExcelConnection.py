import pandas as pd
import os
import re


# Path to OneDrive Excel file
onedrive_path = r"C:\Users\cbeck\OneDrive - Metal Rollforming Systems\WIP SCHEDULE-JOB NAMES 1.xlsm"
# Update filename

# Read the "TABLE OF CONTENTS" sheet into dataframe
try:
    df = pd.read_excel(onedrive_path, sheet_name="TABLE OF CONTENTS")
except Exception as e:
    print(f"Error reading Excel file: {e}")
    exit()
    
# Clean Column E (Remove leading/trailing whitespaces)
df['Column E'] = df['Column E'].astype(str).str.strip()

def extract_numbers_from_i_column(value):
    # Extract numbers from the string
    numbers = re.findall(r'\d+', value)
    # Return the first number found
    return ''. join(numbers) if numbers else None

def match_attachments_to_excel(attachment_names):
    matched_numbers = []
    for attachment in attachment_names:
        # Trim the attachment name
        trimmed_name = re.sub(r'_?\s*NAMEPLATE ORDER\.PDF$', '', attachment, flags=re.IGNORECASE)
        
        # Find rows where Column E contains the trimmed name
        matches = df[df['Column E'].str.contains(trimmed_name, case=False, na=False)]
        
        if not matches.empty:
            # Extract numbers from Column I for all matches
            numbers = [extract_numbers_from_i_column(val) for val in matches['Column I']]
            matched_numbers.extend(numbers)
            print(f"Match For '{trimmed_name}': Die Set Numbers: {numbers}")
        else:
            print(f"No Match For '{trimmed_name}'")
            
    return matched_numbers

