import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.w3schools.com/html/html_tables.asp"
headers = {
    "User-Agent": "Mozilla/5.0"
}
# requests.get() sends an HTTP GET request to the website
response = requests.get(url, headers=headers)
print("status code:", response.status_code)
if response.status_code == 200:
    print("website is accessed successfully")
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if table is not None:
        print("table found successfully")
        rows = table.find_all("tr")
        print("number of rows found:", len(rows))
        data = []
        for row in rows:
            cells = row.find_all("td")
            row_data = [
                cell.get_text(strip=True)
                for cell in cells
            ]
            data.append(row_data)
        # Column names
        columns = [
            "Company",
            "Contact",
            "Country"
        ]
        # Create DataFrame
        df = pd.DataFrame(
            data,
            columns=columns
        )
        print("Complete dataframe:")
        print(df)

