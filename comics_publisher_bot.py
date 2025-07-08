from dotenv import load_dotenv
import os
import time
import telegram
from comics_download_script import download_comics
import requests
import random


def get_random_comics(comics_amount: int) -> dict:
    random_comics_number = random.randint(1, comics_amount)

    comics_link = f'https://xkcd.com/{random_comics_number}/info.0.json'
    response = requests.get(comics_link)
    response.raise_for_status()
    comics = response.json()

    random_comics = {
        'img_url': comics['img'],
        'comment': comics['alt']
    }
    return random_comics


def post_comics(token, chat_id, random_comics_comment):
    bot = telegram.Bot(token=token)
    with open('./Files/comics.png', 'rb') as photo:
        bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=random_comics_comment
        )
    os.remove('./Files/comics.png')


def main():
    load_dotenv()
    token = os.environ['TELEGRAMM_API_KEY']
    chat_id = os.environ['TELEGRAMM_CHAT_ID']
    post_time = int(os.environ['POST_TIME'])
    comics_amount = 3112

    while True:
        random_comics = get_random_comics(comics_amount)
        random_comics_img_url = random_comics['img_url']
        random_comics_comment = random_comics['comment']
        download_comics(random_comics_img_url)
        post_comics(token, chat_id, random_comics_comment)
        time.sleep(post_time)


if __name__ == '__main__':
    main()