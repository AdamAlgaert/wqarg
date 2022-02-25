import os
import requests
from dotenv import load_dotenv
from functools import cache
import pathlib

load_dotenv()


@cache
def get_mapping_data():
    return requests.get('https://tjl.co/wqarg/mapping.json').json()


def post_strip_data(data):
    mapping = get_mapping_data()
    strip_names_3 = {}
    for i, f in enumerate(data):
        p = pathlib.Path(f)
        try:
            short_name = mapping.get(p.stem[0:-2]) + p.stem[-2:]
            strip_names_3[short_name] = i
        except TypeError:
            pass
    url = f'https://tjl.co/wqarg/arrange-save.php?source={os.environ["TJL_ID"]}'
    response = requests.post(url, json=strip_names_3)
    data = response.json()
    if 'error' in data:
        raise Exception('Error from save API: ' + data.error)
    print(f"- {data['url']}")
