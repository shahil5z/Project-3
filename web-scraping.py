import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the webpage
url = 'https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table
table = soup.find('table', {'class': 'wikitable'})

# Extracting table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extracting table rows
rows = []
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    if columns:
        row_data = [col.text.strip() for col in columns]
        rows.append(row_data)

# Ensure headers and rows match
max_columns = max(len(row) for row in rows)  # Find the maximum number of columns in any row
headers = headers[:max_columns]  # Adjust headers if necessary

# Creating a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save to the specified CSV file location
file_path = r'C:\Users\YOU CAN WRITE YOUR DOWNLOAD DESTINATION HERE'
df.to_csv(file_path, index=False)
