import os
import time
import sys
import requests
from dotenv import load_dotenv

load_dotenv()


def send_notifications(new_bungie_url: str):
    # post to a discord channel
    if os.getenv('DISCORD_WEBHOOK'):
        urls = os.getenv('DISCORD_WEBHOOK').split(';')
        for webhook_url in urls:
            requests.post(
                webhook_url,
                json={'content': f'@everyone Circles URL updated to {new_bungie_url}'},
            )

    # send a push notification to my phone
    if os.getenv('PUSHOVER_TOKEN') and os.getenv('PUSHOVER_USER'):
        requests.post(
            'https://api.pushover.net/1/messages.json',
            data={
                'token': os.getenv('PUSHOVER_TOKEN'),
                'user': os.getenv('PUSHOVER_USER'),
                'message': f'Circles URL updated to {new_bungie_url}',
                'sound': 'Savathuns_Song',
            },
        )


def main():
    while True:
        try:
            r = requests.get('http://bungie.net/circles')
            r.raise_for_status()
            if r.url != 'https://www.bungie.net/':
                print(f'URL updated to {r.url}, sending notifications.')
                send_notifications(r.url)
                break
            print('No change, sleeping.')
            time.sleep(60)
        except Exception as e:
            print(f'Exception: {e}')
            time.sleep(60)


if __name__ == '__main__':
    sys.exit(main())
