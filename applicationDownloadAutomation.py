import os
import pandas as pd
import requests
from urllib.parse import urlparse
from pathlib import Path


def download_file(url, folder_path, new_file_name, index):
    # Downloads a file from a URL and saves it to the specified path.
    if not url.startswith('http'):
        print(f"Invalid URL: {url}")
        return

    response = requests.get(url)
    if response.status_code == 200:
        try:
            file_path = os.path.join(folder_path, new_file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
        except Exception as e:
            print(f"Error writing file to disk: {e}")
    else:
        print(f"Failed to download {url} for applicant number {index + 1}")


def create_applicant_folder(base_dir, source_language, applicant_name):
    # Creates a folder structure for the applicant.
    folder_name = applicant_name.replace(' ', '_')
    folder_path = os.path.join(base_dir, source_language, folder_name)
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    return folder_path


def process_applications(config):
    # Processes the applications based on the provided configuration.
    # Load the CSV file
    df = pd.read_csv(config["csv_file_path"])

    # Iterate through each applicant in the CSV
    for index, row in df.iterrows():
        source_language = row[config["headings"]["source_language"]]
        applicant_name = row[config["headings"]["applicant_name"]].replace(' ', '_')

        print(f"Processing: {applicant_name}")

        # Create folder structure for the applicant
        applicant_folder = create_applicant_folder(
            config["base_dir"], source_language, applicant_name
        )

        # Download required files
        for file_type, heading in config["headings"]["file_columns"].items():
            url = row[heading]
            if pd.notna(url):  # Ensure URL is not NaN
                file_extension = urlparse(url).path.split('.')[-1]
                file_name = f"{applicant_name}_{file_type}.{file_extension}"
                download_file(url, applicant_folder, file_name, index)

    print("Processing complete.")


if __name__ == "__main__":
    # Configuration
    config = {
        "csv_file_path": r"C:\Path\To\CSV\File",  # Path to the CSV file
        "base_dir": r"C:\Path\To\Save\Files",  # Path to Base directory
        "headings": {  # Define the column headings. Change based on application
            "source_language": "Source Language",
            "applicant_name": "Applicant Name: First & Family ",
            "file_columns": {
                "CV": "CV",
                "Sample_Translation": "Sample Translation (Upto 5000 words each)",
                "Source_Excerpt": "Original Source Excerpt (not more than 5000 words: scanned and submitted in a PDF)",
                "Translation_Proposal": "Translation Proposal (not more than 5000 words)",
            },
        },
    }

    # Process applications
    process_applications(config)