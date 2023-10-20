import csv
import requests
from requests.auth import HTTPBasicAuth

# Set the base URL for the Redmine instance
BASE_URL = 'https://redmine.example.com'

# Set the path to the CSV file containing the project IDs
CSV_FILE_PATH = 'application.csv'

# Set the API key for authentication
API_KEY = 'your-api-key-here'

# Set up authentication
auth = HTTPBasicAuth(API_KEY, '')

# Set up the request headers
headers = {
    'Content-Type': 'application/json',
}

# Read the project IDs from the CSV file
with open(CSV_FILE_PATH, 'r') as csv_file:
    reader = csv.reader(csv_file)
    project_ids = [row[0] for row in reader]

# Loop through the project IDs and fetch time entries for each project
for project_id in project_ids:
    # Set up the request parameters
    params = {
        'project_id': project_id,
    }

    # Send the request to the Redmine API
    response = requests.get(f'{BASE_URL}/time_entries.json', auth=auth, headers=headers, params=params)

    # Parse the response data
    data = response.json()

    # Print the time entries data for the current project
    print(f'Time entries for project {project_id}:')
    print(data)


import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

# Set the base URL for the Redmine instance
BASE_URL = 'https://redmine.example.com'

# Set the API key for authentication
API_KEY = 'your-api-key-here'

# Set up authentication
auth = HTTPBasicAuth(API_KEY, '')

# Set up the request headers
headers = {
    'Content-Type': 'application/json',
}

# Send a request to the Redmine API to fetch all time entries
response = requests.get(f'{BASE_URL}/time_entries.json', auth=auth, headers=headers)

# Parse the response data
data = response.json()

# Convert the time entries data to a pandas DataFrame
df = pd.DataFrame(data['time_entries'])

# Analyze the time entries data using pandas
# ...
