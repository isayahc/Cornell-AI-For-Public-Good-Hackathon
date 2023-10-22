import os
import requests
from typing import Any

def create_directory_if_not_exists(directory_path: str) -> None:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def download_file(url: str, save_path: str) -> Any:
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully and saved as {save_path}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

if __name__ == "__main__":
    url = "https://data.cityofnewyork.us/api/views/fgq8-am2v/rows.csv?date=20231022&accessType=DOWNLOAD"
    directory_path = "data"
    save_path = os.path.join(directory_path, "new_york_data.csv")
    
    create_directory_if_not_exists(directory_path)
    download_file(url, save_path)
