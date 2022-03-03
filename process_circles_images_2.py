import sys
import os
from PIL import Image
import numpy as np
from utils import post_strip_data, STABLE_PALETTE, create_image
from itertools import chain
import requests
from functools import cache

import page_sort

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


def sort_pages(pages):
    for p in pages:
        if hasattr(page_sort, 'sort_pg_'+str(p)):
            pages[p] = getattr(page_sort, 'sort_pg_'+str(p))(pages[p])
        else:
            pages[p] = page_sort.sort_pg_numbers(pages[p])
    return pages


def main():
    pages, leftovers = get_pages()
    pages = sort_pages(pages)

    # create_image(pages[12], 'output/pg12.png')


    # post_strip_data(chain(*[pages[x] for x in sorted(pages)]), name='full')
    # #
    # post_strip_data(leftovers, name='leftovers')
    # for pn in sorted(pages.keys()):
    #     post_strip_data(pages[pn], name=pn)

    # post_strip_data(pages[1], name='1')
    # post_strip_data(pages[8], name='8')
    # post_strip_data(pages[12], name='12')
    # post_strip_data(pages[20], name='20')
    # post_strip_data(pages[21], name='21')
    # post_strip_data(pages[23], name='23')
    # post_strip_data(pages[29], name='29')
    post_strip_data(pages[26], name='26')
    post_strip_data(pages[27], name='27')
    post_strip_data(pages[28], name='28')
    post_strip_data(pages[29], name='29')
    post_strip_data(pages[30], name='30')

    post_strip_data(chain(*[pages[x] for x in [26, 27, 28, 29, 30]]), name='full')
    create_image(chain(*[pages[x] for x in [26, 27, 28, 29, 30]]), 'output/purple_pages.png')
    # create_image(chain(*[pages[x] for x in sorted(pages)]), 'output/full.png')
    print('done')


if __name__ == '__main__':
    sys.exit(main())
