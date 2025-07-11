import requests
from pathlib import Path


def download_comic(url: str):
    response = requests.get(url)
    response.raise_for_status()
    with open(Path('.')/'Files'/'comics.png', 'wb') as file:
        file.write(response.content)
