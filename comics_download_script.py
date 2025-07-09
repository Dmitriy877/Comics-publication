import requests
import os
from pathlib import Path


def download_comic(url: str):
    response = requests.get(url)
    response.raise_for_status()
    try:
        with open(Path('.')/'Files'/'comics.png', 'wb') as file:
            file.write(response.content)
    except ValueError:
        os.remove(Path('.')/'Files'/'comics.png')
