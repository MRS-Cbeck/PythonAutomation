import win32com.client
import pandas as pd
import os
import re
import pythoncom

# Path to OneDrive Excel file
onedrive_path = "YourPathHere"
# Update filename

# Set definition for target folder
def find_folder(parent_folder, target_name):
    # Check if the parent folder is the target folder
    if parent_folder.Name == target_name:
        return parent_folder
    # Recursively search for the target folder in the subfolders
    for folder in parent_folder.Folders:
        found_folder = find_folder(folder, target_name)
        if found_folder:
            return found_folder
    return None

def process_custom_folder(folder_name):
    # Connect to Outlook
    win32com.client.pythoncom.CoInitialize()
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    namespace.Logon(ShowDialog=False)
    
    #create a list to store the attachments
    matching_attachments = []

    try:
        # Start from root folder
        root_folder = namespace.GetDefaultFolder(6).Parent # Start from the parent of the Inbox folder
        custom_folder = find_folder(root_folder, folder_name)
        
        if not custom_folder:
            raise ValueError(f"Folder '{folder_name}' not found.")
        
        print(f"Found folder '{custom_folder.Name}'.")
        
        # Iterate through the emails in the custom folder
        for item in custom_folder.Items:
            if item.Class == 43: # 43 = Outlook MailItem (Ensure it is an email)
                subject = item.Subject.strip() # Remove leading/trailing whitespaces
                
                # Check if Subject Matches the Criteria
                if subject == "Subject Criteria Here":
                    print(f"\nMatch Found! Subject: {subject}")
                    
                    # Collect Attachment Names
                    attachments = []
                    if item.Attachments.Count > 0:
                        for attachment in item.Attachments:
                            attachments.append(attachment.FileName)
                        print(f"Attachments: {attachments}")
                    else:
                        print("No attachments.")
                        
                    # Add to the Master list
                    matching_attachments.extend(attachments)
                    
        print(f"\nAll matching attachments: {matching_attachments}")
        return matching_attachments # Return the list of matching attachments
    
    except Exception as e:
        print(f"Error: {e}")
        return [] # Return an empty list if an error occurs
    finally:
        # Cleanup COM objects
        for var in ['custom_folder', 'root_folder', 'namespace', 'outlook']:
            if var in locals():
                del locals()[var]

# Release COM objects
win32com.client.pythoncom.CoUninitialize()

# Read the "TABLE OF CONTENTS" sheet into dataframe
try:
    df = pd.read_excel(onedrive_path, sheet_name="Worksheet Name Here")
except Exception as e:
    print(f"Error reading Excel file: {e}")
    exit()
    
# Clean ColumnHere (Remove leading/trailing whitespaces)
df['ColumnHere'] = df['ColumnHere'].astype(str).str.strip()

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

# Run the function
attachment_list = process_custom_folder("Folder Name Here")
matched_numbers = match_attachments_to_excel(attachment_list)

print(f"\nFinal Matched Die Set Numbers: {matched_numbers}")