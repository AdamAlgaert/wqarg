import sys
import os
from PIL import Image
import numpy as np
from utils import post_strip_data
from itertools import chain

#  '//input received/"Reroute IKO-006-XX750210p"'


def is_white(arr):
    return (np.dot(arr[..., :3], [0.299, 0.587, 0.114]) > 200).all()


def is_black(arr):
    return (np.dot(arr[..., :3], [0.299, 0.587, 0.114]) < 50).all()


def slice_has_feature_1(filename):
    img = Image.open(filename)
    return (img.__array__()[8220:8480] == [195, 191, 208, 255]).all()


def slice_has_feature_2(filename):
    img = Image.open(filename)
    return (img.__array__()[5465:5740] == [195, 191, 206, 255]).all()


def slice_has_feature_3(filename):
    img = Image.open(filename)
    return (img.__array__()[5930:6200] == [195, 191, 206, 255]).all()


def slice_has_feature_4(filename):
    img = Image.open(filename).__array__()
    return (np.abs(np.dot(img[400:739][..., :3], [0.299, 0.587, 0.114]) - 193) < 20).all()
    # return (img.__array__()[420:730] == [194, 191, 203, 255]).all()


def slice_has_feature_4_1(filename):
    img = Image.open(filename)
    return (img.__array__()[420:490] == [194, 191, 203, 255]).all()


def slice_has_feature_5(filename):
    img = Image.open(filename)
    return (img.__array__()[430:490] == [196, 192, 204, 255]).all()

def slice_has_feature_5_1(filename):
    img = Image.open(filename)
    return (img.__array__()[410:460] == [196, 192, 204, 255]).all()

def slice_has_feature_6(filename):
    img = Image.open(filename)
    return (img.__array__()[430:490] == [195, 192, 203, 255]).all()

def slice_has_feature_7(filename):
    img = Image.open(filename)
    return (img.__array__()[410:490] == [195, 191, 205, 255]).all()

def slice_has_feature_8(filename):
    img = Image.open(filename)
    return (img.__array__()[9440:9710] == [194, 191, 204, 255]).all()

def slice_has_feature_9(filename):
    img = Image.open(filename)
    return (img.__array__()[5950:6200] == [195, 191, 205, 255]).all()



# start black header
def slice_has_feature_19(filename):
    img = Image.open(filename)
    return (img.__array__()[2:2300] == [16, 16, 21, 255]).all()

def slice_has_feature_20(filename):
    img = Image.open(filename)
    return (img.__array__()[2:2300] == [16, 18, 22, 255]).all()

def slice_has_feature_21(filename):
    img = Image.open(filename)
    return (img.__array__()[2:2300] == [16, 18, 23, 255]).all()

def slice_has_feature_22(filename):
    img = Image.open(filename)
    return (img.__array__()[2:2300] == [17, 18, 23, 255]).all()

def slice_has_feature_23(filename):
    img = Image.open(filename)
    return (img.__array__()[2:2300] == [15, 18, 23, 255]).all()

def slice_has_feature_24(filename):
    img = Image.open(filename)
    return (img.__array__()[0:100] == [16, 18, 23, 255]).all() and not (img.__array__()[2080:2230] == [16, 18, 23, 255]).all()

def slice_has_feature_24_1(filename):
    img = Image.open(filename)
    # return (img.__array__()[0:100] == [16, 18, 23, 255]).all() and (img.__array__()[4970:5110] == [232, 230, 230, 255]).all()
    # return (img.__array__()[0:100] == [16, 18, 23, 255]).all() and (np.dot((img.__array__()[4970:5110])[...,:3], [0.299, 0.587, 0.114]) > 200).all()
    return (img.__array__()[0:100] == [16, 18, 23, 255]).all() and is_white(img.__array__()[4970:5110])

def slice_has_feature_24_99(filename):
    img = Image.open(filename)
    return (img.__array__()[0:100] == [16, 18, 23, 255]).all()

def slice_has_feature_25(filename):
    img = Image.open(filename)
    return (img.__array__()[0:100] == [15, 18, 23, 255]).all()


# purple text
def slice_has_feature_40(filename):
    img = Image.open(filename)
    return (img.__array__()[1200:6200] == [87, 75, 109, 255]).any((0,1)).all() and not is_white(img.__array__()[2300:2500])

def slice_has_feature_40_1(filename):
    img = Image.open(filename)
    return (img.__array__()[1200:6200] == [87, 75, 109, 255]).any((0,1)).all()

def slice_has_feature_41(filename):
    img = Image.open(filename)
    return (img.__array__()[940:1800] == [87, 74, 109, 255]).any((0,1)).all()

def slice_has_feature_41_1(filename):
    img = Image.open(filename)
    return (img.__array__()[3400:3700] == [87, 74, 109, 255]).any((0,1)).all()

def slice_has_feature_41_2(filename):
    img = Image.open(filename)
    return (img.__array__()[8500:9000] == [87, 74, 109, 255]).any((0,1)).all()

def slice_has_feature_42(filename):
    img = Image.open(filename)
    return (img.__array__()[115:1510] == [89, 77, 111, 255]).any((0,1)).all()

def slice_has_feature_42_1(filename):
    img = Image.open(filename)
    return (img.__array__()[1800:2500] == [89, 77, 111, 255]).any((0,1)).all()

def slice_has_feature_43(filename):
    img = Image.open(filename)
    return (img.__array__()[1500:3800] == [84, 72, 107, 255]).any((0,1)).all()

def slice_has_feature_43_1(filename):
    img = Image.open(filename)
    return (img.__array__()[3000:3300] == [84, 72, 107, 255]).any((0,1)).all()


def get_pages():
    slices1 = []
    pages = {}
    all_slices = set(['img_slices/' + x for x in os.listdir('img_slices')])
    for f in all_slices.copy():
        if slice_has_feature_1(f):
            slices1.append(f)
            pages.setdefault(1, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_2(f):
            slices1.append(f)
            pages.setdefault(2, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_3(f):
            slices1.append(f)
            pages.setdefault(3, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_4(f):
            slices1.append(f)
            pages.setdefault(4, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_4_1(f):
            slices1.append(f)
            pages.setdefault(4, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_5(f):
            slices1.append(f)
            pages.setdefault(5, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_5_1(f):
            slices1.append(f)
            pages.setdefault(5, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_6(f):
            slices1.append(f)
            pages.setdefault(6, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_7(f):
            pages.setdefault(7, []).append(f)
            slices1.append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_8(f):
            pages.setdefault(8, []).append(f)
            slices1.append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_9(f):
            slices1.append(f)
            pages.setdefault(9, []).append(f)
            all_slices.remove(f)


    # start black header
    for f in all_slices.copy():
        if slice_has_feature_19(f):
            slices1.append(f)
            pages.setdefault(19, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_20(f):
            slices1.append(f)
            pages.setdefault(20, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_21(f):
            slices1.append(f)
            pages.setdefault(21, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_22(f):
            slices1.append(f)
            pages.setdefault(22, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_23(f):
            slices1.append(f)
            pages.setdefault(23, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_24(f):
            slices1.append(f)
            pages.setdefault(24, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_24_1(f):
            slices1.append(f)
            pages.setdefault(24, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_24_99(f):
            pages.setdefault(24, []).append(f)
            slices1.append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_25(f):
            pages.setdefault(25, []).append(f)
            slices1.append(f)
            all_slices.remove(f)
    # purple text
    for f in all_slices.copy():
        if slice_has_feature_40(f):
            slices1.append(f)
            pages.setdefault(40, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_40_1(f):
            slices1.append(f)
            pages.setdefault(40, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_41(f):
            slices1.append(f)
            pages.setdefault(41, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_41_1(f):
            slices1.append(f)
            pages.setdefault(41, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_41_2(f):
            slices1.append(f)
            pages.setdefault(41, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_42(f):
            slices1.append(f)
            pages.setdefault(42, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_42_1(f):
            slices1.append(f)
            pages.setdefault(42, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_43(f):
            slices1.append(f)
            pages.setdefault(43, []).append(f)
            all_slices.remove(f)
    for f in all_slices.copy():
        if slice_has_feature_43_1(f):
            slices1.append(f)
            pages.setdefault(43, []).append(f)
            all_slices.remove(f)

    return pages, all_slices


def main():
    pages, leftovers = get_pages()
    # bucketed slices
    post_strip_data(chain(*pages.values()))
    # leftover slices
    post_strip_data(leftovers)

    #per-page slices
    for pn, z in pages.items():
        post_strip_data(z)

    print('done')


if __name__ == '__main__':
    sys.exit(main())
