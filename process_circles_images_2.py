import sys
import os
from PIL import Image
import numpy as np
from utils import post_strip_data, STABLE_PALETTE
from itertools import chain
import requests
from functools import cache

#  '//input received/"Reroute IKO-006-XX750210p"'


@cache
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb[0:3]

def single_true(iterable):
    i = iter(iterable)
    return any(i) and not any(i)

def generate_palette():
    all_slices = set(['img_slices/' + x for x in os.listdir('img_slices')])
    all_palettes = set()
    for f in all_slices.copy():
        img = Image.open(f)
        slice_palette = frozenset([x[1] for x in img.getcolors()])
        if len(slice_palette)==16:
            all_palettes.add(slice_palette)
            all_slices.remove(f)
    print(len(all_palettes), len(all_slices))

    for f in all_slices.copy():
        img = Image.open(f)
        slice_palette = frozenset([x[1] for x in img.getcolors()])
        if single_true([slice_palette.issubset(x) for x in all_palettes]):
            all_slices.remove(f)
    print(f"Palettes: {len(all_palettes)}, Ambiguous slices: {len(all_slices)}")
    out_palette = {p: i for i, p in enumerate(all_palettes, start=1)}
    return out_palette


def get_pages():
    # pal_map = process_palette()
    # my_pal = generate_palette()
    my_pal = STABLE_PALETTE
    all_slices = set(['img_slices/' + x for x in os.listdir('img_slices')])
    pages = {}
    for f in all_slices.copy():
        # print(f)
        img = Image.open(f)
        # arr = img.__array__()
        slice_palette = frozenset([x[1] for x in img.getcolors()])
        page = [y for x, y in my_pal.items() if slice_palette.issubset(x)]
        if len(page) == 1:
            pages.setdefault(page[0], set()).add(f)
            all_slices.remove(f)
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
