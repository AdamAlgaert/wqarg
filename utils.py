import os
import requests
from dotenv import load_dotenv
from functools import cache
import pathlib

load_dotenv()

STABLE_PALETTE = {frozenset({(213, 212, 213, 255), (149, 148, 149, 255), (247, 246, 247, 255), (203, 202, 202, 255), (242, 240, 241, 255), (233, 231, 232, 255), (235, 233, 234, 255), (171, 170, 171, 255), (230, 229, 230, 255), (50, 50, 50, 255), (222, 221, 222, 255), (254, 253, 254, 255), (87, 87, 87, 255), (121, 120, 121, 255), (238, 236, 237, 255), (189, 188, 189, 255)}): 1, frozenset({(247, 246, 247, 255), (88, 87, 88, 255), (231, 229, 230, 255), (176, 176, 176, 255), (124, 123, 124, 255), (223, 221, 223, 255), (233, 231, 232, 255), (235, 233, 234, 255), (195, 191, 206, 255), (242, 240, 241, 255), (215, 214, 214, 255), (205, 204, 204, 255), (153, 152, 153, 255), (48, 47, 47, 255), (238, 236, 237, 255), (254, 254, 254, 255)}): 2, frozenset({(213, 212, 213, 255), (241, 239, 240, 255), (246, 245, 246, 255), (82, 81, 82, 255), (236, 234, 235, 255), (230, 229, 230, 255), (117, 116, 117, 255), (145, 144, 145, 255), (186, 185, 186, 255), (223, 221, 222, 255), (238, 236, 237, 255), (254, 254, 254, 255), (201, 200, 201, 255), (239, 237, 238, 255), (45, 45, 45, 255), (168, 167, 168, 255)}): 3, frozenset({(177, 176, 179, 255), (247, 246, 247, 255), (242, 240, 241, 255), (223, 221, 223, 255), (233, 231, 232, 255), (235, 233, 234, 255), (89, 89, 89, 255), (155, 154, 157, 255), (206, 205, 207, 255), (229, 226, 228, 255), (127, 127, 128, 255), (238, 236, 237, 255), (254, 254, 254, 255), (194, 191, 203, 255), (45, 45, 45, 255), (216, 214, 216, 255)}): 4, frozenset({(192, 191, 193, 255), (247, 246, 247, 255), (242, 240, 241, 255), (233, 231, 232, 255), (235, 233, 234, 255), (216, 215, 217, 255), (125, 124, 125, 255), (90, 89, 90, 255), (175, 174, 176, 255), (153, 152, 153, 255), (50, 50, 50, 255), (224, 222, 224, 255), (238, 236, 237, 255), (254, 254, 254, 255), (230, 228, 229, 255), (206, 204, 206, 255)}): 5, frozenset({(237, 235, 235, 255), (206, 204, 208, 255), (127, 125, 128, 255), (231, 229, 230, 255), (246, 245, 246, 255), (195, 191, 208, 255), (223, 221, 223, 255), (242, 240, 241, 255), (234, 232, 233, 255), (37, 36, 37, 255), (254, 253, 253, 255), (87, 85, 89, 255), (179, 177, 179, 255), (155, 154, 156, 255), (239, 237, 238, 255), (215, 214, 215, 255)}): 6, frozenset({(194, 193, 195, 255), (153, 152, 154, 255), (17, 18, 23, 255), (130, 108, 167, 255), (249, 248, 249, 255), (218, 216, 218, 255), (234, 232, 233, 255), (96, 96, 96, 255), (171, 170, 172, 255), (184, 183, 185, 255), (211, 209, 211, 255), (58, 57, 58, 255), (203, 201, 203, 255), (224, 222, 224, 255), (129, 128, 129, 255), (230, 228, 229, 255)}): 7, frozenset({(156, 155, 159, 255), (217, 215, 218, 255), (194, 192, 195, 255), (228, 226, 228, 255), (232, 230, 231, 255), (183, 182, 185, 255), (234, 232, 233, 255), (62, 62, 63, 255), (210, 208, 211, 255), (170, 170, 173, 255), (221, 220, 222, 255), (104, 103, 105, 255), (16, 18, 22, 255), (203, 201, 204, 255), (225, 223, 225, 255), (134, 133, 137, 255)}): 8, frozenset({(230, 228, 229, 255), (154, 153, 154, 255), (47, 47, 47, 255), (109, 109, 109, 255), (171, 170, 170, 255), (249, 248, 249, 255), (223, 221, 223, 255), (220, 219, 220, 255), (234, 232, 233, 255), (80, 79, 79, 255), (185, 184, 185, 255), (226, 224, 225, 255), (208, 207, 208, 255), (134, 133, 134, 255), (198, 197, 197, 255), (216, 214, 216, 255)}): 9, frozenset({(167, 167, 167, 255), (132, 131, 132, 255), (219, 217, 218, 255), (232, 230, 231, 255), (202, 201, 202, 255), (181, 180, 181, 255), (249, 248, 249, 255), (80, 80, 80, 255), (192, 191, 192, 255), (234, 232, 233, 255), (151, 150, 151, 255), (49, 49, 49, 255), (9, 9, 9, 255), (226, 224, 225, 255), (211, 210, 211, 255), (108, 107, 108, 255)}): 10, frozenset({(113, 111, 114, 255), (227, 223, 227, 255), (233, 230, 230, 255), (129, 110, 170, 255), (202, 201, 202, 255), (73, 71, 74, 255), (180, 179, 180, 255), (220, 218, 220, 255), (150, 128, 198, 255), (212, 211, 212, 255), (16, 18, 23, 255), (238, 236, 237, 255), (224, 223, 223, 255), (160, 160, 160, 255), (138, 138, 138, 255), (193, 192, 192, 255)}): 11, frozenset({(194, 193, 195, 255), (127, 105, 167, 255), (216, 214, 217, 255), (183, 182, 183, 255), (232, 230, 231, 255), (146, 145, 146, 255), (221, 219, 221, 255), (225, 223, 224, 255), (80, 79, 79, 255), (234, 232, 233, 255), (115, 114, 115, 255), (210, 208, 211, 255), (228, 226, 227, 255), (13, 12, 12, 255), (203, 201, 204, 255), (168, 167, 168, 255)}): 12, frozenset({(253, 251, 251, 255), (227, 222, 229, 255), (182, 174, 191, 255), (113, 102, 132, 255), (135, 125, 150, 255), (235, 233, 234, 255), (160, 151, 171, 255), (87, 75, 109, 255), (244, 240, 246, 255), (233, 231, 226, 255), (198, 190, 204, 255), (210, 203, 214, 255), (237, 234, 240, 255), (240, 237, 235, 255), (246, 244, 240, 255), (220, 214, 223, 255)}): 13, frozenset({(99, 97, 101, 255), (133, 132, 135, 255), (217, 215, 218, 255), (55, 54, 56, 255), (246, 245, 246, 255), (208, 206, 209, 255), (223, 221, 223, 255), (234, 232, 233, 255), (242, 240, 242, 255), (239, 238, 238, 255), (159, 158, 160, 255), (196, 192, 204, 255), (237, 235, 236, 255), (254, 253, 253, 255), (181, 179, 182, 255), (228, 226, 228, 255)}): 14, frozenset({(130, 129, 130, 255), (229, 227, 228, 255), (247, 246, 247, 255), (92, 91, 92, 255), (195, 192, 203, 255), (46, 46, 46, 255), (242, 240, 241, 255), (233, 231, 232, 255), (235, 233, 234, 255), (206, 205, 207, 255), (222, 221, 222, 255), (157, 157, 158, 255), (238, 236, 237, 255), (254, 254, 254, 255), (178, 178, 179, 255), (216, 214, 216, 255)}): 15, frozenset({(214, 213, 215, 255), (86, 85, 86, 255), (247, 246, 247, 255), (231, 229, 230, 255), (123, 122, 123, 255), (233, 231, 232, 255), (235, 233, 234, 255), (204, 203, 203, 255), (195, 191, 206, 255), (223, 222, 222, 255), (44, 44, 44, 255), (153, 152, 153, 255), (242, 241, 241, 255), (177, 176, 176, 255), (238, 236, 237, 255), (254, 254, 254, 255)}): 16, frozenset({(202, 201, 202, 255), (15, 18, 23, 255), (228, 227, 227, 255), (225, 223, 224, 255), (77, 75, 79, 255), (233, 231, 231, 255), (220, 218, 220, 255), (177, 176, 177, 255), (212, 211, 212, 255), (237, 235, 236, 255), (151, 128, 199, 255), (126, 108, 166, 255), (156, 155, 156, 255), (125, 125, 125, 255), (196, 195, 196, 255), (189, 188, 189, 255)}): 17, frozenset({(178, 174, 182, 255), (236, 235, 236, 255), (234, 231, 231, 255), (16, 16, 21, 255), (201, 198, 202, 255), (140, 132, 151, 255), (124, 120, 131, 255), (159, 155, 164, 255), (230, 225, 230, 255), (189, 187, 192, 255), (227, 227, 228, 255), (198, 189, 207, 255), (211, 208, 213, 255), (224, 223, 224, 255), (90, 84, 102, 255), (219, 217, 221, 255)}): 18, frozenset({(223, 223, 225, 255), (84, 72, 107, 255), (227, 223, 228, 255), (179, 174, 186, 255), (161, 154, 170, 255), (231, 230, 230, 255), (221, 218, 222, 255), (236, 234, 235, 255), (213, 210, 214, 255), (227, 227, 222, 255), (137, 127, 151, 255), (203, 200, 205, 255), (229, 227, 230, 255), (112, 101, 131, 255), (189, 185, 193, 255), (196, 190, 201, 255)}): 19, frozenset({(182, 174, 191, 255), (113, 102, 132, 255), (232, 230, 226, 255), (254, 252, 251, 255), (246, 244, 240, 255), (87, 75, 109, 255), (235, 233, 234, 255), (160, 151, 171, 255), (244, 240, 246, 255), (199, 192, 204, 255), (135, 124, 150, 255), (237, 234, 240, 255), (240, 237, 235, 255), (221, 217, 222, 255), (212, 207, 214, 255), (226, 224, 227, 255)}): 20, frozenset({(227, 223, 227, 255), (76, 75, 78, 255), (157, 156, 156, 255), (16, 18, 23, 255), (225, 227, 223, 255), (202, 201, 202, 255), (191, 190, 191, 255), (150, 127, 197, 255), (124, 107, 164, 255), (232, 230, 230, 255), (220, 218, 221, 255), (212, 211, 213, 255), (238, 236, 237, 255), (224, 223, 223, 255), (177, 176, 177, 255), (125, 125, 125, 255)}): 21, frozenset({(182, 174, 191, 255), (113, 102, 132, 255), (87, 74, 109, 255), (254, 252, 251, 255), (241, 239, 236, 255), (135, 125, 150, 255), (235, 233, 234, 255), (160, 151, 171, 255), (233, 231, 226, 255), (198, 190, 204, 255), (210, 203, 214, 255), (237, 234, 240, 255), (244, 240, 246, 255), (228, 223, 229, 255), (246, 244, 240, 255), (220, 214, 223, 255)}): 22, frozenset({(247, 246, 247, 255), (123, 122, 123, 255), (152, 151, 152, 255), (233, 231, 232, 255), (235, 233, 234, 255), (242, 240, 241, 255), (223, 222, 222, 255), (194, 191, 204, 255), (230, 229, 230, 255), (49, 49, 49, 255), (205, 204, 204, 255), (88, 88, 88, 255), (176, 175, 175, 255), (238, 236, 237, 255), (254, 254, 254, 255), (215, 214, 215, 255)}): 23, frozenset({(217, 215, 217, 255), (229, 227, 228, 255), (154, 153, 154, 255), (123, 122, 123, 255), (195, 191, 205, 255), (242, 240, 241, 255), (223, 221, 223, 255), (233, 231, 232, 255), (235, 233, 234, 255), (208, 206, 208, 255), (85, 84, 85, 255), (44, 44, 44, 255), (178, 177, 177, 255), (238, 236, 237, 255), (254, 254, 254, 255), (247, 246, 246, 255)}): 24, frozenset({(149, 148, 149, 255), (247, 246, 247, 255), (205, 203, 205, 255), (195, 191, 205, 255), (242, 240, 241, 255), (233, 231, 232, 255), (230, 229, 229, 255), (235, 233, 234, 255), (174, 173, 174, 255), (222, 221, 222, 255), (118, 117, 118, 255), (238, 236, 237, 255), (254, 254, 254, 255), (79, 79, 79, 255), (214, 213, 214, 255), (36, 36, 36, 255)}): 25, frozenset({(247, 246, 247, 255), (152, 152, 153, 255), (89, 88, 88, 255), (124, 123, 124, 255), (233, 231, 232, 255), (235, 233, 234, 255), (192, 191, 192, 255), (242, 240, 241, 255), (224, 222, 223, 255), (50, 50, 50, 255), (238, 236, 237, 255), (254, 254, 254, 255), (230, 228, 229, 255), (206, 204, 206, 255), (175, 174, 175, 255), (216, 214, 216, 255)}): 26, frozenset({(194, 193, 195, 255), (79, 78, 78, 255), (109, 109, 109, 255), (249, 248, 249, 255), (209, 207, 210, 255), (135, 135, 135, 255), (234, 232, 233, 255), (230, 228, 230, 255), (221, 219, 222, 255), (172, 171, 172, 255), (226, 224, 226, 255), (202, 200, 203, 255), (185, 184, 185, 255), (45, 44, 45, 255), (156, 155, 156, 255), (216, 214, 216, 255)}): 27, frozenset({(230, 228, 229, 255), (239, 237, 238, 255), (238, 236, 241, 255), (246, 245, 246, 255), (85, 85, 85, 255), (242, 240, 241, 255), (174, 174, 174, 255), (204, 203, 203, 255), (150, 149, 149, 255), (46, 45, 45, 255), (222, 221, 221, 255), (254, 253, 254, 255), (238, 236, 237, 255), (121, 120, 121, 255), (194, 191, 203, 255), (214, 213, 214, 255)}): 28, frozenset({(213, 212, 213, 255), (149, 148, 149, 255), (247, 246, 247, 255), (202, 201, 201, 255), (231, 229, 230, 255), (171, 170, 170, 255), (242, 240, 241, 255), (233, 231, 232, 255), (235, 233, 234, 255), (121, 120, 121, 255), (86, 86, 86, 255), (49, 48, 49, 255), (222, 221, 222, 255), (238, 236, 237, 255), (254, 254, 254, 255), (188, 187, 188, 255)}): 29, frozenset({(219, 213, 223, 255), (245, 243, 241, 255), (253, 252, 251, 255), (135, 124, 150, 255), (113, 103, 133, 255), (182, 174, 192, 255), (239, 238, 239, 255), (243, 239, 239, 255), (89, 77, 111, 255), (243, 239, 245, 255), (198, 190, 205, 255), (237, 235, 231, 255), (229, 223, 230, 255), (210, 203, 214, 255), (159, 150, 171, 255), (239, 237, 243, 255)}): 30}

@cache
def get_mapping_data():
    return requests.get('https://tjl.co/wqarg/mapping.json').json()


def post_strip_data(data, name=''):
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
    print(f"{name}- {data['url']}")
