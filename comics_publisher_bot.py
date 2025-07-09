import os
import random
import requests
import time
from pathlib import Path

from comics_download_script import download_comic

import telegram
from dotenv import load_dotenv


def get_random_comic(comics_amount: int) -> dict:
    random_comic_number = random.randint(1, comics_amount)

    comics_link = f'https://xkcd.com/{random_comic_number}/info.0.json'
    response = requests.get(comics_link)
    response.raise_for_status()
    comics = response.json()

    random_comic = {
        'img_url': comics['img'],
        'comment': comics['alt']
    }
    return random_comic


def post_comic(token, chat_id, random_comic_comment):
    bot = telegram.Bot(token=token)
    with open(Path('.')/'Files'/'comics.png', 'rb') as photo:
        bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=random_comic_comment
        )


def main():
    load_dotenv()
    token = os.environ['TELEGRAMM_API_KEY']
    chat_id = os.environ['TELEGRAMM_CHAT_ID']
    post_time = int(os.environ['POST_TIME'])
    comics_amount = 3112

    os.makedirs('Files', exist_ok=True)

    while True:
        random_comic = get_random_comic(comics_amount)
        random_comic_img_url = random_comic['img_url']
        random_comic_comment = random_comic['comment']
        download_comic(random_comic_img_url)
        post_comic(token, chat_id, random_comic_comment)
        os.remove(Path('.')/'Files'/'comics.png')
        time.sleep(post_time)


if __name__ == '__main__':
    main()