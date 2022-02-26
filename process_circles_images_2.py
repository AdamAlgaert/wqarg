import sys
import os
from PIL import Image
import numpy as np
from utils import post_strip_data
from itertools import chain
import requests
from functools import cache

#  '//input received/"Reroute IKO-006-XX750210p"'


@cache
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb[0:3]

def process_palette():
    tj_pal = requests.get('https://tjl.co/wqarg/palettes.json').json()
    final_pal = {}
    out_map = {}
    for i, pal in enumerate(tj_pal):
        final_pal[i] = set(pal)
        other_pals = tj_pal[:i] + tj_pal[i+1:]
        for pal2 in other_pals:
            final_pal[i] -= set(pal2)
    for i, colors in final_pal.items():
        for c in colors:
            out_map[c]=i
    return out_map

def get_pages():
    pal_map = process_palette()
    all_slices = set(['img_slices/' + x for x in os.listdir('img_slices')])
    pages = {}
    for f in all_slices.copy():
        print(f)
        img = Image.open(f)
        arr = img.__array__()
        for pixel_arr in arr[::10, ::10]:
            rgb_hex = rgb_to_hex(tuple(pixel_arr[0]))
            page_num = pal_map.get(rgb_hex)
            if page_num:
                pages.setdefault(page_num, set()).add(f)
                all_slices.remove(f)
                break
    return pages, all_slices


def main():
    pages, leftovers = get_pages()
    post_strip_data(chain(*pages.values()), name='full')
    post_strip_data(leftovers, name='leftovers')
    for pn, z in pages.items():
        post_strip_data(z, name=pn)
    print('done')


if __name__ == '__main__':
    sys.exit(main())
