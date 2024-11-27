# Application-Download-Automation

This Python script automates the process of downloading and organising application materials for a certain organisation. The input data was a survey consisting of applicants' responses to filtering questions and links to their supporting materials

The script reads data from a CSV file, downloads specified files from URLs, and organizes them into folders based on applicant and language information.

It's designed to be easily modified to include different CSV headers, files, etc and can be customised for your own applications and file structures.

## Features

- Downloads files (CV, sample translations, etc.) for each applicant from provided URLs.
- Organizes files into a structured directory: `<Base Directory>/<Source Language>/<Applicant Name>`.
- Handles errors like invalid URLs or failed downloads.
- Modular configuration for easy adaptation to other use cases

## Requirements

### Python Version
- Python 3.7 or later

### Libraries
Install the required Python libraries:
```bash
pip install pandas requests
```

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/PratyushBalaji/application-download-automation.git
   cd application-download-automation
   ```

2. **Prepare Your CSV File**
   - Create or update a CSV file containing applicant data. 
   - The default column structure in the configuration includes:
     - **Source Language**: Language of the original source.
     - **Applicant Name: First & Family**: Full name of the applicant.
     - **CV**: URL to the CV file.
     - **Sample Translation (Upto 5000 words each)**: URL to the sample translation file.
     - **Original Source Excerpt**: URL to the original source excerpt file.
     - **Translation Proposal**: URL to the translation proposal file.

3. **Update Configuration**
   - Open the script and modify the `config` dictionary to suit your setup:
     - **`csv_file_path`**: Path to your CSV file.
     - **`base_dir`**: Base directory where files will be organized.
     - **`headings`**: Update column names in the CSV to match your data.

4. **Run the Script**
   ```bash
   python translationfellowships.py
   ```

## Configuration

### Example Configuration
The configuration object (`config`) in the script allows you to specify the following:

- **CSV File Path**:
  ```python
  "csv_file_path": r"C:\Path\To\Your\File.csv"
  ```

- **Base Directory**:
  ```python
  "base_dir": r"C:\Path\To\Save\Files"
  ```

- **Column Headings**:
  Update column names based on your CSV structure. Example:
  ```python
  "headings": {
      "source_language": "Source Language",
      "applicant_name": "Applicant Name: First & Family ",
      "file_columns": {
          "CV": "CV",
          "Sample_Translation": "Sample Translation (Upto 5000 words each)",
          "Source_Excerpt": "Original Source Excerpt",
          "Translation_Proposal": "Translation Proposal",
      },
  }
  ```

## Directory Structure

The script organizes files in the following structure:
```
<Base Directory>
└── <Source Language>
    └── <Applicant Name>
        ├── <Applicant Name>_CV.<file_extension>
        ├── <Applicant Name>_Sample_Translation.<file_extension>
        ├── <Applicant Name>_Source_Excerpt.<file_extension>
        └── <Applicant Name>_Translation_Proposal.<file_extension>
```

## Error Handling

- **Invalid URL**: Logs the error and skips the download.
- **Download Failures**: Logs the issue for review.
