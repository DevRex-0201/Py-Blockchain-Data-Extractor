import os
import requests
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import gspread
from dotenv import load_dotenv

load_dotenv()

# Replace 'your_file.xlsx' with the path to your Excel file
excel_file_path = 'chain_list.xlsx'
# Replace 'images' with your desired download directory
download_dir = 'images'

# Load Google Sheets credentials from environment variable
google_credentials_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH')
if not google_credentials_path:
    raise ValueError("The Google Sheets credentials path is not set in the environment variables")

# Set the scope and credentials for Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(google_credentials_path, scope)
client = gspread.authorize(creds)

# Open the Google Spreadsheet by title
sheet_url = "https://docs.google.com/spreadsheets/d/1KfbSzffctVJfm5BqJ_N6YJOuOfhA5zpiL4iW7tCddCY/edit?usp=sharing"
spreadsheet = client.open_by_url(sheet_url)

worksheet_name = "Sheet1"
worksheet = spreadsheet.get_worksheet(0)

# If the worksheet is not found, create a new one
if worksheet is None:
    worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows="100", cols="20")

# Define the header names
header_names = ["Coin Name", "Logo URL"]
# Check if the worksheet is empty (no header row) and add headers if needed
existing_headers = worksheet.row_values(1)
if not existing_headers:
    worksheet.insert_row(header_names, index=1)

def download_image(image_url, filename, folder):
    """
    Download an image from a URL and save it to a specific folder with a specific filename.
    """
    # Check if the folder exists, if not, create it
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    # The path to save the image
    filepath = os.path.join(folder, filename)
    
    # Get the image content
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filepath, 'wb') as img:
            img.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}. Status code: {response.status_code}")

# Load the Excel file
df = pd.read_excel(excel_file_path)

# Iterate over the rows in the DataFrame
for index, row in df.iterrows():
    bitcoin_name = row[0]  # Bitcoin icon name
    image_url = row[1]     # Image URL
    record = [bitcoin_name, image_url]
    worksheet.append_row(record)
    # Create a valid filename (replace spaces with underscores and remove special characters)
    filename = f"{bitcoin_name}.png".replace(' ', '_').translate({ord(c): "" for c in r"!@#$%^&*()[]{};:,/<>?\|`~-=+"})
    # Download the image
    download_image(image_url, filename, download_dir)
