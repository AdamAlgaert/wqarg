import os
import re
import logging
import requests
import pathlib
from PIL import Image

SPREADSHEET_URL = 'https://opensheet.elk.sh/1Y4qoXTpd0ZO2CRZzgYV3Lvd1Aihui_Ya6p0V89nKdNU/Form%20Responses%201'

logger = logging.getLogger(__name__)


def download_file(url):
    local_filename = os.path.join('imgs', url.split('/')[-1])
    if os.path.exists(local_filename):
        return
    print(f'Fetching {url}')
    try:
        with requests.get(url) as r:
            r.raise_for_status()
            if len(r.content) < 100000:
                print('Skipping due to small size.')
                return
            with open(local_filename, 'wb') as f:
                f.write(r.content)
    except requests.exceptions.HTTPError as e:
        logger.error('%s', e)


def slice_image(filename):
    os.makedirs('img_slices', exist_ok=True)
    in_path = pathlib.Path(filename)
    if os.path.exists('img_slices/' + in_path.stem + '-1.png'):
        return  # already sliced
    print('slicing ' + filename)
    img = Image.open(filename)
    arr = img.__array__()
    Image.fromarray(arr[103:10433, 200:210]).save('img_slices/' + in_path.stem + '-1.png')
    Image.fromarray(arr[103:10433, 410:420]).save('img_slices/' + in_path.stem + '-2.png')
    Image.fromarray(arr[103:10433, 620:630]).save('img_slices/' + in_path.stem + '-3.png')
    Image.fromarray(arr[103:10433, 830:840]).save('img_slices/' + in_path.stem + '-4.png')
    Image.fromarray(arr[103:10433, 1040:1050]).save('img_slices/' + in_path.stem + '-5.png')


def main():
    os.makedirs('imgs', exist_ok=True)
    sheet_json = requests.get(SPREADSHEET_URL).json()
    url_re = re.compile('^https://www.bungie.net/pubassets/wqarg/strips/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}.png')
    try:
        image_urls = [x['Paste your Image link here'] for x in sheet_json if url_re.match(x['Paste your Image link here'])]
    except:
        print(sheet_json)
        raise
    for url in image_urls:
        download_file(url)

    # slice the images into individual strips
    for f in ['imgs/' + x for x in os.listdir('imgs')]:
        slice_image(f)


if __name__ == "__main__":
    main()
