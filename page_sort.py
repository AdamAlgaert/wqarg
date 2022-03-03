from PIL import Image
import numpy as np
from functools import partial

def is_white(arr):
    return (np.dot(arr[..., :3], [0.299, 0.587, 0.114]) > 200).all()


def is_black(arr):
    return (np.dot(arr[..., :3], [0.299, 0.587, 0.114]) < 50).all()


def bg_brigtness_sort(img: Image, pix_range=(10110,10330)):
    arr = img.__array__()[pix_range[0]:pix_range[1]]
    return np.dot(arr[..., :3], [0.299, 0.587, 0.114]).mean()

def image_pixel_match_any(img: Image, range, rgba_list):
    return any( [(img.__array__()[range[0]:range[1]] == rgba).any((0,1)).all() for rgba in rgba_list] )

def sort_pg_numbers(images: set):
    out = []
    sort_ranges = [
        (9950, 10100),  # page numbers
    ]
    for range in sort_ranges:
        for f in images.copy():
            img = Image.open(f)
            if not is_white(img.__array__()[range[0]:range[1]]) and is_white(img.__array__()[0:100]):
                out.append(f)
                images.remove(f)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=bg_brigtness_sort, reverse=True)
    images = [i.filename for i in images_objs]

    out.extend(images)
    return out

def sort_pg_1(images: set):
    out = []
    out.extend([

    ])
    out = [x and f'img_slices/{x}.png' or x for x in out]
    images.difference_update(out)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=bg_brigtness_sort)
    images = [i.filename for i in images_objs]

    match_colors = ([87, 87, 87, 255], [50, 50, 50, 255], [149, 148, 149, 255], [189, 188, 189, 255], [254, 254, 254, 255], [222, 221, 222, 255], [121, 120, 121, 255], [213,212,213,255])
    sort_ranges = [
        (2830, 2960),  # short text feature
        (9950, 10100),  # page numbers
    ]

    for range in sort_ranges:
        for f in images.copy():
            img = Image.open(f)
            if image_pixel_match_any(img, range, match_colors) and is_white(img.__array__()[0:100]):
                out.append(f)
                images.remove(f)



    out.extend(images)
    return out

def sort_pg_5(images: set):
    out = []
    out.extend([

    ])
    out = [x and f'img_slices/{x}.png' or x for x in out]
    images.difference_update(out)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=bg_brigtness_sort)
    images = [i.filename for i in images_objs]

    for f in images.copy():
        img = Image.open(f)
        if bg_brigtness_sort(img) < 220:
            out.append(f)
            images.remove(f)


    out.extend(images)
    return out


def sort_pg_8(images: set):
    out = []
    out.extend([

    ])
    out = [x and f'img_slices/{x}.png' or x for x in out]
    images.difference_update(out)

    all_colors = [(156, 155, 159, 255), (217, 215, 218, 255), (194, 192, 195, 255), (228, 226, 228, 255),
                    (232, 230, 231, 255), (183, 182, 185, 255), (234, 232, 233, 255), (62, 62, 63, 255),
                    (210, 208, 211, 255), (170, 170, 173, 255), (221, 220, 222, 255), (104, 103, 105, 255),
                    (16, 18, 22, 255), (203, 201, 204, 255), (225, 223, 225, 255), (134, 133, 137, 255)]
    match_colors = [(62, 62, 63, 255), (16, 18, 22, 255), (134, 133, 137, 255), (104, 103, 105, 255)]
    sort_ranges = [
        (2620, 2800),  # top /
        (9950, 10100),  # page numbers
    ]

    for range in sort_ranges:
        for f in images.copy():
            img = Image.open(f)
            if image_pixel_match_any(img, range, match_colors) and is_white(img.__array__()[2350:2390]):
                out.append(f)
                images.remove(f)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=bg_brigtness_sort, reverse=True)
    images = [i.filename for i in images_objs]

    out.extend(images)
    return out


def sort_pg_12(images: set):
    out = []
    out.extend([
        'f214cfc0-9fac-4667-9550-e8e48249ecfc-4',
        None,
        '39e7c42b-b890-4558-b78e-750d7beda571-5',
        None,
        '06efdd83-2dbe-4da3-bf85-cb7a7f94dfbe-3',
        'cd66e64f-862e-490b-a577-eb86311e262b-4',
        None,
        None,
        '3e13ef27-c189-4fe7-8868-1711feb7aaa0-5',
        None,
        'ecd0ae64-4d45-4e80-914c-2faab7247cfd-1',
        None,
        None,
        '1ebe7dae-ca57-4ead-813c-e035fb85f4af-3',
        None,
        None,
        '5e5a194f-3093-447a-b636-5c4c7c1c2c7a-2',
        'c12748d3-f921-4487-adc6-b33539ed7803-2',
        'be411af9-5c1f-4fc0-85b3-966eda9df5d6-1',
        'd7ba33e4-1e6d-429e-8394-0c6c8d71d289-1',
    ])
    out = [x and f'img_slices/{x}.png' or x for x in out]
    images.difference_update(out)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=partial(bg_brigtness_sort, pix_range=(7100,9100)))
    images = [i.filename for i in images_objs]

    for f in images.copy():
        img = Image.open(f)
        if bg_brigtness_sort(img, pix_range=(7100,9100)) < 220:
            out.append(f)
            images.remove(f)

    match_colors = ([127, 105, 167, 255], [13,12,12,255], [80,79,79,255])
    sort_ranges = [
        #(450, 640),  # top purple /

        (6050, 7060), # signature
        (9950, 10100),  # page numbers
    ]

    for range in sort_ranges:
        for f in images.copy():
            img = Image.open(f)
            if image_pixel_match_any(img, range, match_colors) and is_white(img.__array__()[0:100]):
                out.append(f)
                images.remove(f)



    out.extend(images)
    return out







def sort_pg_20(images: set):
    out = []
    out.extend([

    ])
    out = [x and f'img_slices/{x}.png' or x for x in out]
    images.difference_update(out)

    match_colors = (
        [49, 48, 49, 255], [121, 120, 121, 255], [149, 148, 149, 255], [254, 254, 254, 255], [247, 246, 247, 255],
        [86, 86, 86, 255])
    sort_ranges = [
        (3180, 3330),  # last line on page

        (9950, 10100),  # page numbers
    ]

    for range in sort_ranges:
        for f in images.copy():
            img = Image.open(f)
            if image_pixel_match_any(img, range, match_colors) and is_white(img.__array__()[0:100]):
                out.append(f)
                images.remove(f)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=bg_brigtness_sort, reverse=True)
    images = [i.filename for i in images_objs]

    out.extend(images)
    return out


def sort_pg_21(images: set):
    out = []
    out.extend([

    ])
    out = [x and f'img_slices/{x}.png' or x for x in out]
    images.difference_update(out)

    match_colors = (
        [150, 127, 197, 255], [124, 107, 164, 255], [76, 75, 78, 255], [124, 107, 164, 255], [238, 236, 237, 255],
        [76, 75, 78, 255], [157, 156, 156, 255],
    )
    sort_ranges = [
        (1070, 1250),  # header line 4
        (880, 1050),  # header line 3
        (440, 610),  # header line 1
        (2080, 2230),  # header line 6
        (9950, 10100),  # page numbers
        (680, 840),  # header line 2
        (1830, 1980),  # header line 5
    ]

    for range in sort_ranges:
        for f in images.copy():
            img = Image.open(f)
            # if image_pixel_match_any(img, range, match_colors) and is_black(img.__array__()[0:100]):
            if image_pixel_match_any(img, range, match_colors):
                out.append(f)
                images.remove(f)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=bg_brigtness_sort, reverse=True)
    images = [i.filename for i in images_objs]

    out.extend(images)
    return out

def sort_pg_23(images: set):
    out = []
    out.extend([

    ])
    out = [x and f'img_slices/{x}.png' or x for x in out]
    images.difference_update(out)

    match_colors = (
    [49, 49, 49, 255], [88, 88, 88, 255], [123, 122, 123, 255], [176, 175, 176, 255], [152, 151, 152, 255],
    [194,191,204,255])
    sort_ranges = [
        (8280, 8410), # very short text feature
        (2840, 2970),  # short text feature
        (9950, 10100),  # page numbers
    ]

    for range in sort_ranges:
        for f in images.copy():
            img = Image.open(f)
            if image_pixel_match_any(img, range, match_colors) and is_white(img.__array__()[0:100]):
                out.append(f)
                images.remove(f)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=bg_brigtness_sort, reverse=True)
    images = [i.filename for i in images_objs]

    out.extend(images)
    return out


def sort_pg_26(images: set):
    out = []
    out.extend([
        # Ikora
        '3be0b06f-5fde-43d5-9224-aec6974aca52-3',
        None,
        'a2698fd2-b2f8-44e9-a727-e36eff764e51-3',
        '4fcc7ac7-df42-4996-b46f-f2c32654fda7-5',
        'b4720089-aa9e-40b5-a01d-c21bbfa66848-1',
        '3e4ac44a-44b7-4498-8ee9-d5711d37c13a-5',
        '06efdd83-2dbe-4da3-bf85-cb7a7f94dfbe-4',
        '310edba5-1531-4e5b-8cb5-4a0989d225bb-3',
        None,
        'cf0e4f46-415c-41e4-a6c1-c16a1ad65d91-3',
        '536af6de-6c9e-4784-beab-0f224235c426-5',
        None,
        None,
        'd8d2da1c-77bf-4217-8063-c1e9a5142a91-2',
        None,
        '6c2612ae-c66b-4c56-a008-53ee6ad3d196-5',
        '946c9645-83ef-4a26-b800-e403792050b5-1',
        '01dd0b94-356c-4fce-b3b3-c0beff13c8b5-4',
        None,
        'b2b40669-39de-45c7-be43-eddcaf832ccd-3',
        'e05cbfc0-f7c1-4e40-98f1-8994c8d86868-4',
        'bf812639-2423-4185-8756-649ae50d91db-5',
        '7aec3dbe-a916-4ba6-a46a-6c946d19d645-4',
        '429fe5bc-fdcc-4099-acfd-6b03f6f055ad-4',
        '254a7ab4-bcb3-48b3-a383-30c783dfd9fe-1',
        'ecf5de38-e122-4138-9f12-92be9c7b157f-4',
        None,
        'ee2bced3-d130-46d1-8476-18cc325edac5-4',
        'c9c38d3f-1f1a-49bb-9d0c-5c6fe50639e3-1',
        '9b00f026-b5f3-4f0c-8d37-cb45ff6549a8-4',
        None,
        '5426ddde-dc36-498b-b4f5-8b3452f82ed6-4',  # this section needs work
        'c3fb96e1-e594-4eab-a91f-3224cb57a0f1-5',
        None,
        '12fe851f-2a53-41ec-94f6-904b3b6ba0b4-3',
        '4862ddd5-17a9-4ec4-975e-50529ead3c4e-1',
        'a1c5c66e-f5bf-4e93-a364-88b7d0ad0173-3',
        '6ea2a0f2-3a08-45e4-af8b-1275cc56ee18-4',
        'd1be65cb-0f5b-4df6-8579-c714f24b65c3-2',
        'f9603c1c-1501-49e8-82e4-f48617df37e3-3',
        '1d11de60-b498-4125-9a37-60bc6fc6c914-5',
        'e75187ab-0927-4377-8e9c-7a2b344b3d40-5',
        '61a24ebe-0a38-4d57-aaf8-e63bea91de55-3',
        '30a4387b-dc92-4a36-be63-9ef717adb6d8-4',
        '89f7bd0b-0810-4e2f-9c5e-89ae8a2935d4-5',
        'e66a367f-ec45-4773-9f12-46f477e91f57-2',

        # Rey
        '66eeaaf9-3062-4a47-9f27-937422ceee24-2',
        'ed2c11ee-c0b8-4906-a34d-2c5c5371a2c4-3',
        'b159ee72-05f3-44f0-9876-74aeaafe11d0-3',
        'd9ba59b6-406f-4159-8727-5fc86ebf31cc-3',
        '3dbf1325-e430-4026-aaa0-f68cca70a9cb-2',
        '010f5e34-1aa5-4920-a673-ee9cd53172b3-5',
        'e3b79b88-c73c-47d5-9b8b-e9cc23cc0499-2',
        'bb39d4d3-7b20-470f-bcf5-e8e33adf2469-3',
        '954a71ec-b915-46f8-90d2-f428e75b7c3a-3',
        'f8b7c5fc-1c0d-4d4a-ac90-588271127d06-2',
        None,
        'dd6332c8-5404-4172-b5ef-efdae16ef949-5',
        '605e0718-053a-4412-9c38-7f45591913dc-3',
        'df740319-f335-4f8e-a5fd-4ca1f4e3eee2-2',
        'a5a0f600-9d86-47c0-ae36-bf72847d4fbd-1',
        '8c61da8a-1b9b-4010-8641-1646283e0bbd-2',
        '28de6c3e-e688-4ee1-842c-1e7b0494ef71-3',
        '8b307513-3ac6-40f2-ae5d-cb216508aa0d-1',
        None,
        '89461483-abe3-40af-8a63-32c2544e001a-1',
        '48a0c1f4-3209-460d-b0b8-9d835a8408d1-1',
        'ddf0643d-cdc4-4337-89d4-4427f2cdbe28-3',
        'c8dd29d3-4d04-42e8-9319-cfe99fae17c4-3',
        '09b60866-bce8-434d-8325-75a3c5974e94-5',
        'c9647e74-bda9-4373-b9a8-7d93c5c9456c-1',
        '7b62364e-bb9a-4a20-9d93-75d6912db254-3',
        '80191c5e-a38e-4758-b59f-a08c54094c1a-1',
        '0f4478d1-c9d5-4beb-a76c-37f69e6dcca9-3',
        '77358e7b-3548-4b70-940b-9aced924455a-2',
        'c93755ee-4dc0-43d6-ab24-76faaa6d4554-3',
        '7b62364e-bb9a-4a20-9d93-75d6912db254-2',
        '0815fd9e-45da-408a-ba2c-cebe0bdbfca3-2',
        'c74658ed-5f69-496e-a33d-9174e2d90ec3-2',
        'da6802ab-3464-4d9b-8813-aaaf072e2965-1',
        'f9027ed4-5b4a-4a70-8d96-6363216a7be6-4',
        '64a0e896-0da2-47bd-aacb-1eb3e8cf75fb-3',
        '6d72bbea-926a-4708-957a-4bfec0a819d7-3',
        '10c89f9c-b5c8-4d72-9fc7-fdc87a4da113-2',
        'cd0d4014-50fe-48db-80c9-37c72ba5fa90-2',
        None,
        '42cc596c-509d-4495-a75e-a823cd00a884-5',
        'cf0e4f46-415c-41e4-a6c1-c16a1ad65d91-2',
        'ef03ad03-90c4-4f60-a548-66142ed04348-2',
        'd161a853-0429-4608-9182-add4dfd83018-3',
        None,
        '00b2e4d9-c945-4a51-904b-1d43ed380d35-3',
        'b44092aa-2ad1-454e-bc79-fb1e24666c03-5',
        '962bb69b-fac2-43e6-a3cb-ffd601e002ed-4',
        '55f19a59-3583-44fa-a804-bf7e20337129-2',
        '7177fbf4-4f6d-4324-9603-18a2998b6075-1',
        'c899cc09-a51e-43f2-be85-88421505f973-1',
        'f2c5333c-119a-45d0-8643-d81c1733e57e-4',
        'd509399d-1735-4a91-bae9-9be156d20f09-3',
        'b623d4c3-717f-48a7-88ef-120e255dce30-2',
        '120e0d1b-9d78-492d-950d-2c6bd4fa1ab2-5',
        None,None,None,None,None,
        '2072e6a8-678c-484c-a1a2-6425599bb90b-2',
        '323131e8-b1f0-4ad5-8572-9daf7740cf3e-4',
        '79a68ad3-cd8a-4265-929e-630e1afc7f83-2',
        'd76dad9d-3581-4f1c-bba2-989b9a1f0ee7-3',
        'ec35ab3b-9f3e-4c3b-90e1-27e770a32106-5',
        '1631b181-dd25-460f-a5a8-c9ff972baeda-2',
        'be957298-f9c4-447d-81e3-a68012e83317-3',
        '8efb9b97-6215-468e-99e0-b3c0a92eaa5f-3',
        '1764d0e1-afc3-4eee-bab9-672291e92e1e-5',
        'a93d95d2-c88c-43e0-b395-138a4d59c284-4',

        None,None,None,None,None,None,None,None,None,  # separator

        # page numbers
        '58a70038-deea-47e5-a694-1b5e1beb8744-5',
        'f859c240-cbf6-42c1-8322-6457590b6b93-1',  #This part needs some work
        'cdac678c-4718-44ae-86f9-1f18c00dfbb6-4',
        None,
        None,
        '7c7d244d-8d1f-4b58-bc70-ee6284622360-4',
        'bbc0b7a4-ef98-4fcf-abdf-d8bbdfe81e92-1',
        '12fe851f-2a53-41ec-94f6-904b3b6ba0b4-1',
        '054439ce-d133-43f0-8994-56bcc3189345-4',
        'c91b6ace-68a2-4a27-b83e-a2f080f0ffad-4',
        '9ed9ce1a-3c8d-4740-9c5c-baa0169eeebd-1',
        '9ad7c48d-decb-4ffd-a02d-861be5e8fb42-3',
        'e25c11b1-ca93-42ae-8b62-c42d6df50466-2',
        '62ac2508-5609-4e13-92c9-4c8e7bc38492-5',
        None,
        'd77dc260-cf07-41da-a038-7b034a0fca79-4', # maybe?
        '854f2104-6988-4b51-9f1b-0ef384fd87f7-3',
        '51b03dfd-fa4f-4122-b983-d1c62cf5e795-4',
        '4902c06f-67cf-4595-bf13-98888cb35ef0-5',
        'd4e3a253-ec63-4469-a46c-47f72fe2be5c-2',
        None,
        '7cbb83bc-f1ad-4466-8df5-36ca56a5682e-3',
        '31b671c8-f7eb-4535-bf7f-4a2c25e1676a-3',
        None, None, None, None, None, None, None, None, None,  # separator
    ])
    out = [x and f'img_slices/{x}.png' or x for x in out]
    images.difference_update(out)

    match_colors = ([84, 72, 107, 255], [137, 127, 151, 255], [112, 101, 131, 255], [161, 154, 170, 255], [196, 190, 201, 255], [179, 174, 186, 255], [189, 185, 193, 255])
    sort_ranges = [
        (460, 640),  # top //
        (1190, 1330),  # line 1
        (6700, 7100),  # signature at bottom of page
        (3320, 3450),  # line 9
        (1530, 1670),  # line 2
        (5990, 6140),  # line 20
        (9950, 10100),  # page numbers
        (1570, 1640),
        (1870, 2000),
        (6350, 6450),
    ]

    for range in sort_ranges:
        for f in images.copy():
            img = Image.open(f)
            if image_pixel_match_any(img, range, match_colors) and is_white(img.__array__()[0:100]):
                out.append(f)
                images.remove(f)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=bg_brigtness_sort, reverse=True)
    images = [i.filename for i in images_objs]

    out.extend(images)
    return out


def sort_pg_27(images: set):
    out = []
    out.extend([
        'c2b20d81-6acd-4f30-8a16-3eb6bebf4db4-2',
        '051a2b92-2106-40b1-bb72-eb3584aa5552-1',
        'b4717bec-0e22-4304-ab02-8caf83d7104a-4',
        'a436d4a5-268a-4972-8ade-5690fd1a713c-3',
        'f4f39cd9-0098-42fb-bfd2-52901b136adc-1',
        '2ce9fc71-5a28-413b-ae02-06f64aea963c-1',
        None,
        '85b59e6f-5ba8-40c3-a28c-656af687facb-1',
        '93753e58-0cd7-44c4-8406-397011d8ea2f-2',
        '0d8b5f29-068d-4133-a32f-7883dcf02641-4',
        'd95c2e94-3820-4f31-b602-0533a630f5d5-3',
        None,
        'b4779a70-7032-4895-8903-39fe0cfa7f50-3',
        '8cc35754-17a4-4d70-bbcb-49c087277455-2',
        'a64e6216-056c-47b1-a082-0ee48b0da5a0-1',
        '8d732adc-c244-4573-b9e0-c2c8c27cc4db-1',
        '3776657b-c37f-49c0-a1aa-ec62693d4231-4',
        '20f13451-f925-4b05-bde1-28ecfdc99555-2',
        'fd8aab98-a026-4587-a904-f61dc974c283-3',
        'd3773ff8-ad5f-4873-9bba-7b61ddaa7bdd-5',
        '2930ce8b-d963-404f-80ce-ee25e0e65867-2',
        '0fc6f7a0-a8c8-4224-861a-71870cacd3ea-3',
        'aa47e755-5c30-454a-9285-6f75910d58e1-1',
        'de52b104-70c4-43ef-866b-7ad4df14b865-1',
        '1a87a023-515b-4dbc-ad71-2c8debf1678a-4',
        'd235f99a-9f8f-45a8-9735-cdfd7a52e7e2-5',
        'bac6323b-11f6-4cda-b93e-c495ac2134b4-1',
        '629326d3-34e2-4c70-acd9-d300b670bf5b-4',
        '7d251655-8d98-4108-ae67-12a9bf04c70e-5',
        '4ff5a346-5933-4293-87b0-417ce4a7f49c-5',
        '6500bb3a-08a5-4c3f-8146-40b574bfb159-1',


        '62f139c8-ebe2-4870-b20d-8a259da8c5ce-1',
        '84c75f00-cdf0-45cc-af07-8a6fa58b4b1d-2',
        'a1ca28fd-335b-4ce3-82ac-e58608e85891-1',
        '4d67923a-6435-41b7-b0e1-69e755ce108a-4',
        '4c1fcd9f-7593-4988-9917-b799f0db8735-3',
        'a577ddda-ac3c-424e-97d4-987bc7cac7bd-1',
        'a33e124a-3690-4fa6-a2ed-f77bba2ad896-4',
        '63c9fda2-8016-4963-ad4a-459ae3e4ef4b-3',
        None, None, None, None, None, None, None, None, None,  # separator
    ])
    out = [x and f'img_slices/{x}.png' or x for x in out]
    images.difference_update(out)

    match_colors = ([210, 203, 214, 255], [135, 125, 150, 255], [198, 190, 204, 255], [113, 102, 132, 255], [160, 151, 171, 255], [182, 174, 191, 255])
    sort_ranges = [
        (450, 640),  # top /
        (7390, 7530),
        (830, 980),  # top greeting
        (2300, 2460),  # last line of first paragraph
        (9390, 9540),
        (9950, 10100),  # page numbers

    ]

    for range in sort_ranges:
        for f in images.copy():
            img = Image.open(f)
            if image_pixel_match_any(img, range, match_colors) and is_white(img.__array__()[0:100]):
                out.append(f)
                images.remove(f)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=bg_brigtness_sort, reverse=True)
    images = [i.filename for i in images_objs]

    out.extend(images)
    return out


def sort_pg_29(images: set):
    out = []
    out.extend([

    ])
    out = [x and f'img_slices/{x}.png' or x for x in out]
    images.difference_update(out)

    match_colors = (
    [87, 75, 109, 255], [113, 102, 132, 255], [135, 124, 150, 255], [254, 252, 251, 255], [182, 174, 191, 255],
    [199,192,204,255])
    sort_ranges = [
        (4430, 4600), # very short text feature
        (8440, 8580),  # short text feature
        (9950, 10100),  # page numbers
    ]

    for range in sort_ranges:
        for f in images.copy():
            img = Image.open(f)
            if image_pixel_match_any(img, range, match_colors) and is_white(img.__array__()[0:100]):
                out.append(f)
                images.remove(f)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=bg_brigtness_sort, reverse=True)
    images = [i.filename for i in images_objs]

    out.extend(images)
    return out


def sort_pg_30(images: set):
    out = []
    out.extend([
        # ikora
        '9b9344dc-62c9-4738-8c5e-d941c30999ae-4',
        None,
        '13b9b6e5-74cf-43b5-a502-9b6dd5dc2206-2',
        '50d9655e-feae-49f6-be17-b91695c0b7ca-1',
        None,
        'dede5745-4de5-4cba-92d0-4e0d679c27ec-3',
        'ae3d9620-5b76-4923-90fb-097a1bb8fb37-4',
        '2fe52d08-6699-42a2-92bd-73c3e7b28eba-4',
        '25070b4b-f4ba-4d1d-9cd3-c56d10c5a545-4',
        '4872d4b7-577c-45b9-911c-4a3d5dd94d9b-4',
        '6e1c51ae-2d58-4a4a-9584-4cec1ad43f97-3',
        '963c6ce9-167d-42dd-a368-94a3cec61cdf-5',
        None,
        None,
        None,
        None,
        None,
        '01f24881-32f9-4121-a3bc-3d8afeec5253-5',
        'a435f86f-4ce4-40b3-b97d-f7aa9b6ae6b3-1',
        'e8dc2925-9b1d-4cd4-939d-662aa8ebd2a5-1',
        '93753e58-0cd7-44c4-8406-397011d8ea2f-5',
        '9c85d721-18e7-4da5-90f3-0d49e77985b5-3',
        'b341312f-d54d-42bf-b4aa-9be16e5893ce-1',
        '2ceec095-71ac-49d5-a3fa-9c70a0351a80-1',
        None,
        '0e3973d9-fbc1-44fa-af00-c495843b5385-2',
        '931e33fd-ba70-465c-a4c8-5d2d0a36e498-5',
        '92a843b5-f2cc-41c0-a297-7176afbd6abe-2',
        '407dab0b-6cc0-4c6b-8939-1fca36879b21-1',
        '10a678e8-a663-4638-82ff-ae07039d57ff-1',  # o

        None, None, None,  # separator
        '62512f39-d013-47c5-b364-0ffe90fc4588-3',
        None, None, None,  # separator
        '9ee3cfb7-5394-4cc8-85ed-588978216eb2-5',  # r
        'f54405dd-e8d4-49b7-8457-c981fc1618b9-2',
        'ec733ffb-3508-4b92-aa5d-bd33b72ff9ce-4',
        '11bd893d-0f34-4ac4-af6f-7ebea1ab49f7-3',
        'b299b8c7-a989-4721-bc0c-c324439b7b28-5',
        'f28dbbfb-3651-49bf-96e1-ce63a769137f-5',
        'a7a12c54-479c-4c50-a6ac-a9512d47617e-1',
        '2262ee87-2786-40e6-ae58-51b0946b2f8c-3',
        'b137580a-43e6-42cb-a32a-25dd389e7504-4',
        'ee494916-557d-4915-aebb-d586be99aeef-3',
        'd452d7ae-9fc2-458a-b987-862dadec9f82-3',
        '20bba6bf-199a-4c84-8e3d-eebd077c3d14-3',
        'f694db7b-f7ba-46a9-bc0e-6ea8ed9b25b8-4',
        'b883ec18-1f25-4acb-823d-872058266a42-2',
        '1ecb9ec5-dd16-4f8f-93b3-80b750646fbd-4',  # a
        '64a0e896-0da2-47bd-aacb-1eb3e8cf75fb-5',
        'ce8e219f-d7e8-4542-929d-fc7ddf15008e-5',
        '0133c310-8a2a-4d48-a543-bad2b378c723-1',
        '13d3e062-eeb1-43e7-bee3-3f567e5814c9-4',
        '97a8d5df-aa2e-42d1-88b4-c5c1c9c30752-3',
        '76d0c767-cb14-4174-908c-cbfbf042c030-2',
        '2494c286-35f1-4834-a6a1-4d58d0780160-2',
        '0e882acf-fa2d-4aa9-87e3-bf1b631e1ca0-5',

        #rey
        '68fed451-dc7b-4a94-a102-ccd23dfeec10-2',
        '7b6e78bc-2fec-45ef-b460-88327ad01d61-5',
        'c4a24434-9c6f-435d-a7a0-d848c383b2d2-5',
        '7fc6a5cb-51ed-4443-82da-8e81e3954aaf-2',
        None,
        None,
        '24f2ebe0-b17c-4fc5-a5a0-71e1ffa18da3-5',
        '3f34a276-becc-4c31-b5b8-cd7cc65e81cf-4',
        'c38e1e4b-7d82-4869-844c-cea4f05b8f5b-5',
        '6a1f45f7-b0f7-455a-b283-7e4ec6473259-1',
        '39c78bda-9a33-4757-b480-0813a2f86657-4',
        None,
        '860050d1-0f4d-4384-b438-adefe7a7e5e3-3',
        None,
        '055fcf75-6b6c-4b5e-ac5f-647072ff8763-4',
        'ea535e30-5f2f-4e92-8526-974784cc0846-2',
        'f2c8a596-090a-4056-b99a-5c3fe7acbbf9-5',
        '38026acf-330b-4ce6-9058-06cf14e654ed-3',
        'e3d8f253-1e02-45d7-8186-e6e6d6c03920-5',
        '601172ea-3429-48c6-9372-7b2abd216ee1-2',
        '94e1ab8a-5c2f-4b6b-8296-fddb6cdf5d45-3',
        '86252f32-9745-416a-9f39-a35dfa917a18-1',
        '30bdf6ef-3c8a-45e1-bd12-b88a062504c3-5',
        '3fa3197f-f28f-47fc-bb96-03e4ebd15e42-3',
        None,
        'e43b9873-922f-4246-aa51-4483895240a3-1',
        '0393bd73-cea2-448c-b1b2-33f332adc2df-5',
        '7a6ab482-54d1-44f7-b78c-fbdd913e3155-1',
        '4c6b5494-6311-4508-b375-0bac665ab839-2',
        '25d75a6d-cf72-4c52-b31f-16777cb4f962-1',
        '3e4ac44a-44b7-4498-8ee9-d5711d37c13a-3',
        'fad2e29a-616c-45bb-aa8e-43df76b082e0-1',
        '8260055b-81fc-49e7-b5cb-9b12dc506e82-4',
        None,
        None,
        None,
        None,
        None,

    ])
    out = [x and f'img_slices/{x}.png' or x for x in out]
    images.difference_update(out)

    match_colors = ([113, 103, 133, 255], [135, 124, 150, 255], [169, 150, 171, 255], [210, 203, 115, 255], [89,77,111,255], [159,150,171,255], [198, 190, 205, 255], [253, 252, 251, 255])
    sort_ranges = [
        (4690, 4970),  # / at bottom of entry
        (870, 1000),  # very short page feature
        (3710, 4320),  # signature at bottom of page
        (3020, 3180),
        (9950, 10100),  # page numbers
    ]

    for range in sort_ranges:
        for f in images.copy():
            img = Image.open(f)
            if image_pixel_match_any(img, range, match_colors) and is_white(img.__array__()[0:100]):
                out.append(f)
                images.remove(f)

    images_objs = [Image.open(path) for path in images]
    images_objs.sort(key=bg_brigtness_sort, reverse=True)
    images = [i.filename for i in images_objs]

    out.extend(images)
    return out