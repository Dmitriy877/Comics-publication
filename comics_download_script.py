import requests
import os


def download_comics(url: str):
    os.makedirs('Files', exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open('./Files/comics.png', 'wb') as file:
        file.write(response.content)
