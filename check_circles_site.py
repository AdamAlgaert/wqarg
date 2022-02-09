import os
import time
import sys
import requests
from dotenv import load_dotenv
import playwright.sync_api

load_dotenv()


def send_url_notifications(new_bungie_url: str = ''):
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
                # 'sound': 'Savathuns_Song',
            },
        )


def detect_url_change():
    while True:
        try:
            r = requests.get('http://bungie.net/circles')
            r.raise_for_status()
            if r.url != 'https://www.bungie.net/':
                print(f'URL updated to {r.url}, sending notifications.')
                send_url_notifications(r.url)
                break
            print('No change, sleeping.')
            time.sleep(60)
        except Exception as e:
            print(f'Exception: {e}')
            time.sleep(60)


def send_page_notifications(screenshot: bytes):
    # post to a discord channel
    if os.getenv('DISCORD_WEBHOOK'):
        urls = os.getenv('DISCORD_WEBHOOK').split(';')
        for webhook_url in urls:
            requests.post(
                webhook_url,
                json={'content': f'@everyone new circles page content.'},
            )

    # send a push notification to my phone
    if os.getenv('PUSHOVER_TOKEN') and os.getenv('PUSHOVER_USER'):
        requests.post(
            'https://api.pushover.net/1/messages.json',
            data={
                'token': os.getenv('PUSHOVER_TOKEN'),
                'user': os.getenv('PUSHOVER_USER'),
                'message': f'Circles page changed.',
                # 'sound': 'Savathuns_Song',
            },
            files={
                'attachment': ('screenshot.png', screenshot, 'image/png')
            }
        )


def detect_page_change():
    with playwright.sync_api.sync_playwright() as p:
        browser = p.chromium.launch()
        while True:
            try:
                page = browser.new_page()
                res = page.goto("https://www.bungie.net/7/en/Direct/Circles")
                assert res.status == 200, f'Got HTTP status {res.status}'
                try:
                    page.wait_for_selector('text="COMING SOONz" >> visible=true')
                    print('coming soon')
                    time.sleep(60)
                except playwright.sync_api.TimeoutError:
                    print("it's go time")
                    screenshot = page.screenshot()
                    send_page_notifications(screenshot)
                    break
            except (playwright.sync_api.Error, AssertionError) as e:
                print(f'Failed to load ARG page: {str(e)}')
                time.sleep(60)
            finally:
                page.close()
        browser.close()


def main():
    # detect_url_change()
    detect_page_change()


if __name__ == '__main__':
    sys.exit(main())
