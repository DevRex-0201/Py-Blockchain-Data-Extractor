# Blockchain Data Extractor

Blockchain Data Extractor is a sophisticated Python script tailored for the automated extraction of cryptocurrency, wallet provider names and logo information directly from "https://defillama.com/". It streamlines the process of collecting cryptocurrency data, including names and logo URLs, uploading these details into a Google Sheets document for organized access, and saving the logos locally in a specified directory.

## Video Preview

[![Video Preview](https://github.com/DevRex-0201/Project-Images/blob/main/video%20preview/Py-Blockchain-Data-Extractor.png)](https://brand-car.s3.eu-north-1.amazonaws.com/Four+Seasons/Py-Blockchain-Data-Extractor.mp4)

## Features

- **Automated Data Scraping**: Seamlessly scrapes cryptocurrency names and their logo URLs from "https://defillama.com/".
- **Google Sheets Integration**: Efficiently uploads scraped cryptocurrency names and logo URLs to a specified Google Sheets document, ensuring data is easily accessible and manageable.
- **Local Image Saving**: Downloads and saves cryptocurrency logos based on the scraped URLs, organizing them within a designated local directory.

## Prerequisites

To effectively use the Cryptocurrency Icon Downloader, ensure you meet the following requirements:

- Python 3.x installed on your computer.
- Necessary Python packages: `pandas`, `requests`, `gspread`, `oauth2client`, `python-dotenv`. Install these using pip:
  ```
  pip install pandas requests gspread oauth2client python-dotenv
  ```
- A Google Cloud Platform (GCP) project with the Google Sheets API enabled.
- A service account associated with your GCP project and a downloaded JSON key file for this account.

## Setup

1. **Environment Variables**: Define the path to your Google Sheets service account credentials JSON file in an environment variable. This is typically done by creating a `.env` file in your project's directory containing:
   ```
   GOOGLE_SHEETS_CREDENTIALS_PATH=<path_to_your_service_account_json_file>
   ```
   Ensure to replace `<path_to_your_service_account_json_file>` with the actual path to your JSON key file.

2. **Google Sheets Document Access**: Set up a Google Sheets document and adjust its sharing settings to grant edit access to the service account's email found in the JSON key file.

3. **Prepare for Data Scraping**: The script is pre-configured to scrape data from "https://defillama.com/". Ensure you're in compliance with the website's terms of service regarding data scraping.

## Usage

Follow these steps to execute the script:

1. Confirm that your environment variables and Google Sheets document are correctly configured as per the instructions in the setup section.
2. Execute the script with Python by running:
   ```
   python script_name.py
   ```
   Make sure to replace `script_name.py` with the actual name of your Python script.

3. The script will commence by scraping cryptocurrency information from "https://defillama.com/", then proceed to upload this data to the specified Google Sheets document, and finally download the logos into the designated local directory.

## Customization

You can customize several aspects of the script to fit your requirements:

- **Download Directory**: Modify the `download_dir` variable to alter the local directory where logos are saved.
- **Google Sheets URL**: Update the `sheet_url` variable to the URL of your specific Google Sheets document.
- **Worksheet Name**: Change the `worksheet_name` variable if you prefer to use a different worksheet within your Google Sheets document.

## Troubleshooting

- Verify that the service account has been granted appropriate access to the Google Sheets document.
- Double-check that the Google Sheets credentials path environment variable is correctly configured.
- Ensure compliance with "https://defillama.com/" terms of service regarding data scraping.
