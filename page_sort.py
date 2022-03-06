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
    # Letter from  Ikora to Misraaks
    out = []
    out.extend([
        # Ikora
        '3be0b06f-5fde-43d5-9224-aec6974aca52-3',
        'cf5a1b38-94c3-4e56-b7e4-88780eeaa8b9-1',
        'a2698fd2-b2f8-44e9-a727-e36eff764e51-3',
        '4fcc7ac7-df42-4996-b46f-f2c32654fda7-5',
        'b4720089-aa9e-40b5-a01d-c21bbfa66848-1',
        '3e4ac44a-44b7-4498-8ee9-d5711d37c13a-5',
        '06efdd83-2dbe-4da3-bf85-cb7a7f94dfbe-4',
        '310edba5-1531-4e5b-8cb5-4a0989d225bb-3',
        '69f16e44-ffa8-44bc-b557-4613a89d8773-2',
        'cf0e4f46-415c-41e4-a6c1-c16a1ad65d91-3',
        '536af6de-6c9e-4784-beab-0f224235c426-5',
        'ae648827-64c7-4340-8608-14b070062e1f-3',
        '7f2391bb-4b73-4d72-a599-5fc497a32571-2',
        'd8d2da1c-77bf-4217-8063-c1e9a5142a91-2',
        'c2c3ac07-b8c2-4f30-b258-35b25fe8267c-4',
        '6c2612ae-c66b-4c56-a008-53ee6ad3d196-5',
        '946c9645-83ef-4a26-b800-e403792050b5-1',
        '01dd0b94-356c-4fce-b3b3-c0beff13c8b5-4',
        '8100f946-70ae-4396-b868-5dc723c995ba-4',
        'b2b40669-39de-45c7-be43-eddcaf832ccd-3',
        'e05cbfc0-f7c1-4e40-98f1-8994c8d86868-4',
        'bf812639-2423-4185-8756-649ae50d91db-5',
        '7aec3dbe-a916-4ba6-a46a-6c946d19d645-4',
        '429fe5bc-fdcc-4099-acfd-6b03f6f055ad-4',
        '254a7ab4-bcb3-48b3-a383-30c783dfd9fe-1',
        'ecf5de38-e122-4138-9f12-92be9c7b157f-4',
        'dd8ae46f-9f42-4318-a7b9-fbbd3f03e664-5',
        'ee2bced3-d130-46d1-8476-18cc325edac5-4',
        'c9c38d3f-1f1a-49bb-9d0c-5c6fe50639e3-1',
        '9b00f026-b5f3-4f0c-8d37-cb45ff6549a8-4',
        'e16b2ecc-8695-49dc-b668-54d773822598-5',
        '5426ddde-dc36-498b-b4f5-8b3452f82ed6-4',
        'c3fb96e1-e594-4eab-a91f-3224cb57a0f1-5',
        '6e578ddf-309d-410e-a2bc-d4ce42efb108-2',
        '12fe851f-2a53-41ec-94f6-904b3b6ba0b4-3',
        '4862ddd5-17a9-4ec4-975e-50529ead3c4e-1',
        'a1c5c66e-f5bf-4e93-a364-88b7d0ad0173-3',
        '6ea2a0f2-3a08-45e4-af8b-1275cc56ee18-4',
        '968257c0-bf08-4acb-9246-3e1b776dd1d4-1',
        'd1be65cb-0f5b-4df6-8579-c714f24b65c3-2',
        'f9603c1c-1501-49e8-82e4-f48617df37e3-3',
        '1d11de60-b498-4125-9a37-60bc6fc6c914-5',
        'e75187ab-0927-4377-8e9c-7a2b344b3d40-5',
        'bd79bca2-cd38-45bf-af50-722172de310d-2',
        '61a24ebe-0a38-4d57-aaf8-e63bea91de55-3',
        '30a4387b-dc92-4a36-be63-9ef717adb6d8-4',
        '89f7bd0b-0810-4e2f-9c5e-89ae8a2935d4-5',
        'e66a367f-ec45-4773-9f12-46f477e91f57-2',

        # Rey
        '66eeaaf9-3062-4a47-9f27-937422ceee24-2',
        '026780b8-4251-4c1c-834b-08e5de2db093-5',
        'ed2c11ee-c0b8-4906-a34d-2c5c5371a2c4-3',
        'b159ee72-05f3-44f0-9876-74aeaafe11d0-3',
        'd9ba59b6-406f-4159-8727-5fc86ebf31cc-3',
        '3dbf1325-e430-4026-aaa0-f68cca70a9cb-2',
        '010f5e34-1aa5-4920-a673-ee9cd53172b3-5',
        'e3b79b88-c73c-47d5-9b8b-e9cc23cc0499-2',
        'bb39d4d3-7b20-470f-bcf5-e8e33adf2469-3',
        '954a71ec-b915-46f8-90d2-f428e75b7c3a-3',
        'f8b7c5fc-1c0d-4d4a-ac90-588271127d06-2',
        'c9561316-ebd1-4723-983d-1068827c2cac-2',
        'efb67f28-70b9-4628-ab18-cfa3dfe5348b-3',
        'dd6332c8-5404-4172-b5ef-efdae16ef949-5',
        '605e0718-053a-4412-9c38-7f45591913dc-3',
        'df740319-f335-4f8e-a5fd-4ca1f4e3eee2-2',
        'a5a0f600-9d86-47c0-ae36-bf72847d4fbd-1',
        '8c61da8a-1b9b-4010-8641-1646283e0bbd-2',
        '28de6c3e-e688-4ee1-842c-1e7b0494ef71-3',
        '8b307513-3ac6-40f2-ae5d-cb216508aa0d-1',
        'c68f3118-4baf-4e2b-b416-c57ec916c661-1',
        '89461483-abe3-40af-8a63-32c2544e001a-1',
        '48a0c1f4-3209-460d-b0b8-9d835a8408d1-1',
        'ddf0643d-cdc4-4337-89d4-4427f2cdbe28-3',
        '02387888-c12b-4500-8b26-95e1b7d3992f-4',
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
        '6e4730bc-93a2-4317-a520-e532d3b8f164-2',
        'c74658ed-5f69-496e-a33d-9174e2d90ec3-2',
        'da6802ab-3464-4d9b-8813-aaaf072e2965-1',
        'f9027ed4-5b4a-4a70-8d96-6363216a7be6-4',
        '64a0e896-0da2-47bd-aacb-1eb3e8cf75fb-3',
        '6d72bbea-926a-4708-957a-4bfec0a819d7-3',
        '10c89f9c-b5c8-4d72-9fc7-fdc87a4da113-2',
        'cd0d4014-50fe-48db-80c9-37c72ba5fa90-2',
        'b0bb74d6-9e48-44d2-8f59-f38b21fb91ca-2',
        '42cc596c-509d-4495-a75e-a823cd00a884-5',
        '8f516b7a-6ea7-4142-a5a6-9a4b4648122c-3',
        'cf0e4f46-415c-41e4-a6c1-c16a1ad65d91-2',
        'ef03ad03-90c4-4f60-a548-66142ed04348-2',
        'd161a853-0429-4608-9182-add4dfd83018-3',
        'bad9feba-efb9-4da3-95e0-ec0de54e8a86-2',
        '00b2e4d9-c945-4a51-904b-1d43ed380d35-3',
        'b44092aa-2ad1-454e-bc79-fb1e24666c03-5',
        '962bb69b-fac2-43e6-a3cb-ffd601e002ed-4',
        '779560fd-ef20-4ca0-920e-e6afbfb8c8fc-1',
        '55f19a59-3583-44fa-a804-bf7e20337129-2',
        '7177fbf4-4f6d-4324-9603-18a2998b6075-1',
        'c899cc09-a51e-43f2-be85-88421505f973-1',
        'f2c5333c-119a-45d0-8643-d81c1733e57e-4',
        'd509399d-1735-4a91-bae9-9be156d20f09-3',
        'b623d4c3-717f-48a7-88ef-120e255dce30-2',
        '120e0d1b-9d78-492d-950d-2c6bd4fa1ab2-5',
        'fdf18e79-f5f5-438e-a695-a0e51090e353-2',
        'd85865fe-4fea-4a53-9879-999f94fd7806-1',
        '29a93dad-1449-44f0-896c-38cd4431e399-4',
        '2d55f20d-80f7-46bf-a89d-00cad384ba34-2',
        'cf8c1abe-11c0-4464-80aa-d7ac83b8a235-3',
        'b91e9f67-2112-4945-9cc9-c4a1c025cfe4-4',
        'e46f0663-823a-4d66-bb0c-85b98288534f-2',
        '48d05582-5e30-463f-a1c4-e2130634bae2-2',
        '55608781-addf-41a6-911b-faad7e53cb7e-4',
        '7d3611e2-c3fc-4dda-a544-609130f119a9-2',
        '79a68ad3-cd8a-4265-929e-630e1afc7f83-2',
        '00b87aca-2e90-4d42-b68c-3019ce176077-5',
        '138960cd-96e4-40ed-9994-5c1ba71c64ad-1',
        '271f0ae4-f457-486b-b2b8-3670ff95a940-1',
        '2072e6a8-678c-484c-a1a2-6425599bb90b-2',
        '323131e8-b1f0-4ad5-8572-9daf7740cf3e-4',
        '400f1094-9451-4d54-886a-46a4b65b1188-2',
        '4cece000-e3d1-45cd-9c40-e7a46a80c885-4',
        'd76dad9d-3581-4f1c-bba2-989b9a1f0ee7-3',
        'ec35ab3b-9f3e-4c3b-90e1-27e770a32106-5',
        '1631b181-dd25-460f-a5a8-c9ff972baeda-2',
        'be957298-f9c4-447d-81e3-a68012e83317-3',
        '8efb9b97-6215-468e-99e0-b3c0a92eaa5f-3',
        '1764d0e1-afc3-4eee-bab9-672291e92e1e-5',
        '63f7d8a5-ca8c-4dc1-83cd-fb64540de3eb-1',
        'a93d95d2-c88c-43e0-b395-138a4d59c284-4',
        '1bc273b2-18ce-491f-b31b-a1ce9c2de032-3',
        '42394bcb-0667-41cb-ac6d-1717ed396a09-4',
        'c9558c97-ed6e-42a7-a733-09b3e05e0b3b-4',
        '27d9e152-c773-4df3-a65e-249070e61b18-1',
        '554984b5-662e-4218-a6a8-ffe0eb5b2e12-2',
        '7621aba5-9c65-4681-adfc-98ea2dfe6d5d-3',
        'b4679146-eb18-41ae-bb6a-6193f55385f0-2',
        '9321f88b-0f60-4e08-a428-5464c1214f05-2',
        '6ae76f9f-059f-490f-bb26-12a239b9c243-5',
        'fb6950fe-8556-4647-b699-e05e1cc24bdb-1',
        'c0c423b5-700d-4a68-ad28-c0a313546337-2',
        '42ca434d-2e08-4f53-96d5-07eeca287195-1',
        '1fa573fb-584d-4a29-8294-e2b3b0d6e658-3',
        'a71c9404-7824-4e22-82da-70bc6e2f9bda-4',
        'bd4d1d25-1194-4781-b89f-54dbddd7e050-1',
        'dd32764a-243f-4868-a075-83ba42e17e62-2',
        '341142fc-0d33-4c36-82ba-288a6b8ef975-5',



        None,None,None,None,None,None,None,None,None,  # separator

        # page numbers
        '185d9283-1c5e-4009-86a8-132919a8a93d-1',
        '31b671c8-f7eb-4535-bf7f-4a2c25e1676a-3',
        'cdac678c-4718-44ae-86f9-1f18c00dfbb6-4',
        '2ce1de3f-d94e-4994-bafa-324a19ef0007-5',
        '506a8607-97df-4824-856e-8512a2b296a1-2',
        '7c7d244d-8d1f-4b58-bc70-ee6284622360-4',
        '6b56ab2e-eaab-4b69-8767-9dbfc971bfdb-3',
        'bbc0b7a4-ef98-4fcf-abdf-d8bbdfe81e92-1',
        '12fe851f-2a53-41ec-94f6-904b3b6ba0b4-1',
        '054439ce-d133-43f0-8994-56bcc3189345-4',
        'c91b6ace-68a2-4a27-b83e-a2f080f0ffad-4',
        '9ed9ce1a-3c8d-4740-9c5c-baa0169eeebd-1',
        '9ad7c48d-decb-4ffd-a02d-861be5e8fb42-3',
        'e25c11b1-ca93-42ae-8b62-c42d6df50466-2',
        '62ac2508-5609-4e13-92c9-4c8e7bc38492-5',
        'ed739f9b-437f-4c5e-bd53-a56835cbea61-5',
        'd77dc260-cf07-41da-a038-7b034a0fca79-4', # maybe?
        '854f2104-6988-4b51-9f1b-0ef384fd87f7-3',
        '51b03dfd-fa4f-4122-b983-d1c62cf5e795-4',
        '4902c06f-67cf-4595-bf13-98888cb35ef0-5',
        'fdf18e79-f5f5-438e-a695-a0e51090e353-3',
        'd4e3a253-ec63-4469-a46c-47f72fe2be5c-2',
        '6241e0b4-fe4e-4897-8930-a0b6c4d232f8-2',
        '7cbb83bc-f1ad-4466-8df5-36ca56a5682e-3',
        '33d490e3-9427-44d9-84b1-2f3fb9963aae-3',
        'a1e9974e-1538-4289-a22f-197831f4445f-4',
        '859a48f0-b52c-4273-a0ae-86f230a9cbad-1',
        '94ca14de-1776-4e77-8237-213677fb2645-1',
        '58a70038-deea-47e5-a694-1b5e1beb8744-5',
        'f859c240-cbf6-42c1-8322-6457590b6b93-1',
        'be2a354a-4a5f-4e81-a73e-32aae511cba6-2',
        'f402bd55-d247-48c1-af09-b09054bb8740-3',
        '1723131c-f72e-44f4-8aa5-3a025bd2f080-3',
        '07236006-81c9-4067-901a-1cf5cf589caa-2',
        '590df96a-e7ad-4d6e-8b17-a899f32b98e8-5',
        #'31b671c8-f7eb-4535-bf7f-4a2c25e1676a-3',
        None, None, None, None, None, None, None, None, None,  # separator

        # Machine output

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
        '320d7101-dbce-47be-8d9a-d127fa479444-5',
        '85b59e6f-5ba8-40c3-a28c-656af687facb-1',
        '93753e58-0cd7-44c4-8406-397011d8ea2f-2',
        '0d8b5f29-068d-4133-a32f-7883dcf02641-4',
        'd95c2e94-3820-4f31-b602-0533a630f5d5-3',
        'c7a67c8f-34f5-4dfe-9887-4b9c867b874d-2',
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
        '15c8e084-a002-4049-90ad-87d25301aa06-1',
        'aa47e755-5c30-454a-9285-6f75910d58e1-1',
        'de52b104-70c4-43ef-866b-7ad4df14b865-1',
        '1a87a023-515b-4dbc-ad71-2c8debf1678a-4',
        'd235f99a-9f8f-45a8-9735-cdfd7a52e7e2-5',
        '0e65a6a6-5cef-4752-b2ae-d83e19d34e51-5',
        'bac6323b-11f6-4cda-b93e-c495ac2134b4-1',
        '629326d3-34e2-4c70-acd9-d300b670bf5b-4',
        '6d3d85ec-b951-43f6-ae86-d14afb9398e0-3',
        '7d251655-8d98-4108-ae67-12a9bf04c70e-5',
        '4ff5a346-5933-4293-87b0-417ce4a7f49c-5',
        '6500bb3a-08a5-4c3f-8146-40b574bfb159-1',
        '893be0c1-03b5-40b3-b419-5c18e779a040-4',
        '62f139c8-ebe2-4870-b20d-8a259da8c5ce-1',
        '84c75f00-cdf0-45cc-af07-8a6fa58b4b1d-2',
        'a1ca28fd-335b-4ce3-82ac-e58608e85891-1',
        '0c670d11-999a-4803-ba72-e82c1b0dd78d-2',
        '4d67923a-6435-41b7-b0e1-69e755ce108a-4',
        '4c1fcd9f-7593-4988-9917-b799f0db8735-3',
        'a577ddda-ac3c-424e-97d4-987bc7cac7bd-1',
        '896544a9-39f1-4765-a072-f1ac359b3e09-4',
        'a33e124a-3690-4fa6-a2ed-f77bba2ad896-4',
        '63c9fda2-8016-4963-ad4a-459ae3e4ef4b-3',
        '7f2391bb-4b73-4d72-a599-5fc497a32571-4',
        '4d3b1fbc-86ef-4193-ada4-07a16c0fc583-5',
        'f6ade64f-8819-4476-82e2-c6ff9a2b4ed3-1',
        '4c0f2ca5-b317-4a1b-90b7-29413761d5ef-5',
        'e513ba05-3e19-4fcc-aa8e-f5ec69931c0c-5',
        'acfbec1a-3786-4b7c-8de5-513816293b02-1',
        '916f9b20-6321-4cce-b855-3072ad168454-2',
        '42ca434d-2e08-4f53-96d5-07eeca287195-3',
        '4007e400-4bb7-49a5-a7f3-09e35a5f654c-2',
        '5b5cf5ea-4a3d-44e8-898d-fcd075bfe93b-2',
        '48f024f3-1078-41f8-8320-6fdfdbadbf52-2',
        'cc687376-35ad-4838-a87d-0a1d9f71a97f-2',
        '739deb7c-e187-4ac1-8518-eb992defea70-4',
        '55f93afb-58b9-4a66-bd78-82046ea4ef9f-2',
        'a36eb3b8-f4d5-41ac-be40-aa70cc58d738-2',
        '6e4730bc-93a2-4317-a520-e532d3b8f164-4',
        'f116ac38-2099-401e-a703-eb6a59fc616e-1',
        '8d53bc41-3795-41ff-bffa-ed4672624884-3',
        'e90791c4-1d29-49c6-be50-8179510dd6ce-4',
        '20fe8684-7f77-42f5-a6e1-e3e534f4e016-3',
        '9517879d-533d-403a-abe0-1954b75d99a2-1',
        '144053d7-433d-4eaf-8d64-09c687562a50-4',
        'f6c4827f-68e4-4cf4-a526-f1d1e4ecaf56-1',
        '2d9867c2-86a9-44c0-8b18-849459ec68b2-4',
        'a89df036-16d8-45c4-9ae5-fd9703910441-2',
        'a5a0f600-9d86-47c0-ae36-bf72847d4fbd-2',
        'a5086e6c-fa0e-49c5-9384-2c52017bcff6-1',
        'd1153c84-4cdf-4970-b029-bcc98eaa4ee7-1',
        '995da1c6-3f74-4724-936f-1c8376423255-2',
        'b087b67f-39aa-4b40-b1d9-32bc8d32be08-2',
        'b3229bc4-140d-43a4-9799-923af424d7a7-2',
        '30d8a1f6-19ce-485a-adec-7aff95a66c07-1',
        '9e09d4c7-af80-44a9-aac0-5a397688b8e6-3',
        '18814950-39ab-4f74-a76b-a43dbd8a6557-2',
        '4ff2a43e-aa33-4e4e-bd69-33ce62013649-1',
        '80220a4e-113f-4c8e-a9f8-e45e72cb4974-2',
        'd4a53660-950e-4650-ab2d-bfcb5603c70c-5',
        '0df197b4-fe4f-4207-8c5b-21ca75de9f98-5',
        '69923a4d-38bc-466b-8224-f192bb469d27-5',
        'a9de4e28-f49d-4be6-a077-8117c4d551cd-2',
        '6904e3c7-9c0c-4a33-96c2-39540befc87c-4',
        'a391ed8e-5ba4-4492-849f-e197f49ca6e9-5',
        '4bac91d8-23ae-4d61-96b2-1dc11461ed3d-1',
        'e8610d25-5f34-41b0-b915-372959aa5df0-2',
        'b125f8e9-c938-4b77-995a-ed1ed1b231a1-3',
        'df29f2b7-99c8-4f1f-92b0-be69fae39103-2',
        '8d230113-92bf-40e3-ae1a-5cfdfc024dd7-1',
        'bb11a096-0399-4c7a-98bd-2d8dffb2acbe-5',
        '403e0f04-e814-4661-9803-83f4aa610aa0-1',
        'eb1b1221-acf3-4ab8-9dea-e595071e947e-5',
        '8b804195-c944-4782-8fb1-3ffe44d012a7-2',
        '1423a00e-b87a-4a5c-9e9f-ea257930af56-4',
        '9b96c1e4-febd-4320-a3dc-fbd2ffdf0bc9-5',
        'd62b0d06-c6cf-4975-8f46-0429969938ea-3',
        '2dfa4bc3-c8b2-4f6b-8173-d51817dd9c66-4',
        'ac2893e4-e9ac-4c0e-ae14-b4ecbff15b85-2',
        '9ac8d4e3-7797-4598-8536-5a34d75352c2-5',
        '84ca82ab-d928-46a8-86de-8b7eb57558ab-1',
        'fcdb0d36-d88b-4e57-8b1c-8e3b4b3f4d63-1',
        '50d9655e-feae-49f6-be17-b91695c0b7ca-3',
        '79e86ce8-edf4-48d5-8477-e4ff0d38edd3-1',
        '1ac895e3-a456-477f-aeb2-24246b0224c8-2',
        'df9dda00-6d69-448e-ae0f-31846b203590-1',
        '1df14f0a-42d0-47b7-a7f8-41b796e3ee02-1',
        '2ce9fc71-5a28-413b-ae02-06f64aea963c-3',
        '48d3a450-16ad-40d2-99ae-2ba2450497e6-5',
        '42b100f7-4fd2-49bc-b5ca-0ac185c35cb5-3',
        'e16b2ecc-8695-49dc-b668-54d773822598-3',
        'f1e1b3a0-dd0c-4f9b-bb59-a9fbe3b33d43-3',
        'bb4444d2-8601-4c88-a235-c737b38fa0b9-2',
        'df2b6170-c1ae-46bf-b040-bdcbf2cfa249-2',
        'ce7a1f97-328a-452e-af65-ec4551300958-5',
        'ba8bd739-4e77-4b98-8ce1-46e8fbfe3aef-5',
        'e99e4880-eac5-4c43-9959-87d32664d69c-1',
        'dc3ef6a0-b5c8-425d-8dbc-8ddc9a2ddae6-5',
        'b3472a20-4ca1-4bca-91c3-2ce1c697342b-5',
        '6c9ffdc8-498a-4d4a-ab12-5300d2a8fd6c-3',
        '4aa0b90c-aca7-4f71-ad2a-2442c25795ff-5',
        'd1b76d01-8b1d-4597-b93b-24f600fb1b1f-3',
        'f90d3052-ab1d-4066-bdd8-48d6da03d4d0-2',
        'e6feadfd-83d3-4f00-b208-b613bd05c804-3',
        '0fdb0243-6b5a-4bdd-88f2-117b4f9512b7-1',
        'fe008959-9304-4e48-a28c-6decfd639ba2-1',
        'be98a5e3-8462-4cc6-b497-838d50be58be-1',
        'f116ac38-2099-401e-a703-eb6a59fc616e-5',
        'e22860ae-3db2-4ece-a799-c748dba1d203-1',
        '47192fdb-5c47-4bc1-a7a9-5c0de22bf8c6-1',
        '9a71a91d-bc0c-4b09-a2e4-013d9621e2b9-2',
        'f23f02dc-187e-4782-9fad-20ca48b567d0-2',
        '75c18834-0ef0-48d8-866b-be0f52b01952-4',
        '01a96379-a077-499e-8823-0f30c072f954-5',
        'a0559d6c-e79a-4d0c-959a-f31eff673ff0-5',
        '6508becd-9bad-419c-b6df-d6c8f5048466-1',
        'c4bf2cd2-26a6-4a9b-a18b-b2434145dfd7-1',
        'f8c093b6-311c-4318-ab80-e88bdefd3f8d-1',
        'c5178f28-a77f-4e72-8d72-b8d6ced983d1-5',
        'b3b584c5-f823-460b-be08-709e0c4f5064-5',
        '0d285e47-d773-49dd-ac33-07e7710113d4-4',
        '3d5485c7-b164-4a40-9b56-64fcf41d404e-3',
        '0ca2e8b4-89d2-4be1-929b-a873487ca56e-2',
        'd65a1e75-54bc-44f7-8696-4c0c3efe0089-5',
        'cd690c62-0b5b-4cb9-9c8d-2fbaec09683d-1',
        '25fc1f6d-a52f-4339-b3cd-24086ebf319d-2',
        '9a01f07b-5f2e-424d-bd6f-455624cc0615-1',
        '76a9bb7c-47e2-4366-af1c-13f6615ef84a-2',
        '2cf573fd-8967-4755-bcb4-09b58f85f9b1-4',
        '1e55ead1-b280-4bfd-86a0-0143d4768f7e-2',
        '21c86e3c-b8bd-4143-82ad-60176718ab7e-3',
        '602d573a-7df4-4c57-a660-30ef776e4530-3',
        'a89df036-16d8-45c4-9ae5-fd9703910441-1',
        'd84589cb-2526-4525-acca-d0b476db5056-4',
        '25a6e2e3-0b18-4b76-8571-ee6f4e5acffa-4',
        '1a576629-a916-4cd7-abe7-13b7ac049760-2',
        '85c18485-70e1-4640-997d-c553fb13012d-5',
        '0e3973d9-fbc1-44fa-af00-c495843b5385-3',
        'c8429621-71aa-4070-917d-d2aeb8d5d57d-3',
        'e1112aa9-c1cc-471b-a1fc-b04e6320df35-3',
        '3d1c90d3-1935-45a1-95e4-c05486ec55aa-1',
        '2d0498c9-e6d2-49c3-8952-5f21666f6957-3',
        '77f45db8-3a1c-445e-aa75-273ad8518b85-5',
        'bc4a465a-26d6-4263-8709-276602fc2d92-4',
        '2e75b883-729b-472d-93ab-240fb41522d8-4',
        'ade4237d-883e-47b6-af44-e7d246c38dbe-3',
        '7e6c4843-3c02-4ff8-b924-75989742c99c-5',
        '3886835a-b927-47d2-9b13-92d27196f480-1',
        '5befbbe4-72a2-4d4e-a09a-8c59924c07d5-3',
        '2127fb76-385d-412d-93a2-ff869c9c965c-3',
        '002418c8-374e-40d3-a8de-9f524e90b409-5',
        'b35738de-2a69-4f1b-bfba-e5a742624d69-1',
        'c0d6b454-9fc7-4de7-aed3-17f0194bd249-3',
        'f830a0c5-f64b-4f33-9ee8-1a81aae8f7c9-5',
        '7c65dc4c-a483-45ee-acaf-0562a338a056-2',
        'cedabbd9-0cd1-400d-966f-c8ce06301a14-3',
        'c0d6b454-9fc7-4de7-aed3-17f0194bd249-2',
        'c9aa6efb-047a-4dbe-bb7f-f6460a896a80-5',
        '38a0b96d-70a5-4733-a711-ade12d9c60db-5',
        '83586db3-7e5d-4009-94de-39e8b0421e53-5',
        '38a0b96d-70a5-4733-a711-ade12d9c60db-2',
        '47192fdb-5c47-4bc1-a7a9-5c0de22bf8c6-4',
        '300b2fdc-c868-4b5e-82ba-6c41c2b05888-5',
        '9541f413-07f1-4168-aeef-8aae19b02be5-5',
        '25070b4b-f4ba-4d1d-9cd3-c56d10c5a545-3',
        '7c0137a3-57c6-4f0e-ab3c-88000d1fda4d-1',
        '4db208fa-e0f5-46b4-a4ed-58f5e80a08cb-5',

        # Machine output
        '9317c743-08cf-4af8-b019-fd6c89a09aea-3', '5e73c821-7ace-43bd-a29d-7b931b325fd6-5',
        '9d656473-0d0e-47eb-9307-f809a8cf6f0b-1', 'b83d4aaa-9a5f-4e72-959b-34155c0373bf-1',
        '0eff1a3e-e6fa-4bbb-8190-882a1a13211e-2', '122ed8aa-c2df-4ace-940d-e7fd84dec067-2',
        '47b218ac-ac0e-4dae-b49c-fe3d0a8d402f-1', 'c91b6ace-68a2-4a27-b83e-a2f080f0ffad-1',
        '33f6ef11-b918-4b07-809a-bca2b48fe01b-4', '8bbbc4ba-d943-4c8f-b5ab-6da35b56fdb9-3',
        'af02f2aa-694e-4f92-a3fb-4c875acb31d4-2', '4ef77163-baa7-4087-8bca-5b1bb768f9d2-4',
        '9276f0f6-59f0-4ed6-9533-45eb1b954542-4', '83d95b54-8ded-4e9a-97ba-a4c060939c32-4',
        '68b3f969-808f-4b22-b7e4-53899c349f6a-3', '71f48eef-bbb1-4724-987a-dcbeda4eabc6-4',
        'ce48841c-f7ef-42ef-b115-0bdb457f4eb3-4', '01346ae0-e2ba-482e-ad3d-684b295565e7-2',
        '84611f24-2b2f-4567-a5e7-b1a2a96a8268-5', 'd3b94d68-5d5d-427f-84c5-2fe6a3e0a8d8-2',
        '3163e5a5-ee89-49ab-90b0-e52232c8a958-5',
        'e8dc2925-9b1d-4cd4-939d-662aa8ebd2a5-4',
        'c2bdb18d-0ce9-4476-b6d3-24902d9691c2-3',
        '90335426-7f2e-488a-8f2a-ac059d5378ab-2',
        '741bf2cb-a6cd-4e28-a52f-d2ce55ede0f5-3',
        '41603517-45ed-4dfd-b729-0d57b79a3011-3',
        '2d02326e-62b8-4808-b93b-4e4be8dde1ab-4',
        'c899cc09-a51e-43f2-be85-88421505f973-4',
        '5d4d0855-9e92-43f4-80c9-6fd74f04e66e-2',
        '15d6f96e-6ed8-4d7d-a591-af303263a7e5-1',
        'e15dfa8d-5c56-4f53-828f-7b4f8ab3295b-4',
        'b56c33d9-391e-4cca-bfad-6e2eb41e5c19-4',
        '7de8a023-c6ac-4af3-9286-6f524b127a10-5',
        '4bf40c31-3a4b-4595-9c03-d5756c0eecee-4',
        '8e0802a6-5ef4-4654-93d9-0e69400cf256-1',
        '25ed2ab8-e65f-4287-9b1a-2f308dc32004-5',
        '874a9c88-6672-48b0-90bf-2c637593a23c-4',
        'a43d5dbe-b387-4754-bdf7-18b94af5b128-5',
        'e998b050-9399-4e9d-b08d-e76c30a90b04-3',
        '6aa9c9a8-300d-4056-8bf2-2b8d4a7a9ad0-2',
        'd3e05e03-246e-4eb0-b186-58cdc2f93646-3',
        '1a1a1088-cdfe-48ae-aa4e-85b9fe391583-3',
        '0ca88e91-5413-4f88-84d9-ce50d6cb84c1-1',
        'ea59a8ae-8d3b-4b06-8745-82b31973a413-3',
        'd3f4b0a7-4d33-430a-99d4-b38c09c0d720-3',
        'fa7dac6c-23b1-46bd-a7e4-a291dedbcea6-3',
        'fad2e29a-616c-45bb-aa8e-43df76b082e0-2',
        '123127fd-155e-44bc-9f40-66838b6c9999-3',
        '39e2564d-2afb-4cf6-821a-d5d9e4754a25-2',
        'b78fa810-893d-46bb-9d74-a1a7c14014bd-4',
        'f4e1f7fe-5eea-498b-b5e8-ee3696006fb2-3',
        '5d8adf30-6940-4bcf-a62c-64f04b727554-1',
        'dede5745-4de5-4cba-92d0-4e0d679c27ec-2',
        'f5798057-eb0f-4fd7-b833-88cfebd09e20-1',
        'bfdcbd30-9989-4477-a2da-328bdd1858a6-5',
        'cebbd6ec-3f4b-4566-89e9-9fb52e9ff98c-1',
        '127659d8-8baa-4fe8-8549-177dc51e5fc7-2',
        '1dce2a5a-4142-400c-9467-df9ab01c6a7d-3',
        'a4f83892-2bd5-4d43-90a5-fa8e64beaa60-2',
        'c9c38d3f-1f1a-49bb-9d0c-5c6fe50639e3-5',
        'e3b79b88-c73c-47d5-9b8b-e9cc23cc0499-4',
        'ea40f600-3c91-488f-8640-d42ef464b936-5',
        '81070233-96d2-4e76-9df6-488f8c0a5bd6-2',
        '769dd66f-0a47-46d1-b250-c05fba9ffd3c-5',
        '72dc0e16-730d-4ad4-a542-d8e2215a41b6-4',
        '6f0fe4e7-7f44-4dc8-aaae-06150aa859fe-1',
        '4439db99-476c-487b-9e17-48ef666dfbde-3',
        'dfd4b74a-fed3-4997-a55b-680f26da74ef-4',
        '685f3507-7418-4310-9570-33aab3e784af-5',
        '1cba5af4-1a10-4256-87ba-e24df803ca11-3',
        'c0bcc197-5cea-4618-8ce1-24eb9599c187-3',
        '323131e8-b1f0-4ad5-8572-9daf7740cf3e-5',
        '42b0f1de-37d4-4985-8547-94090445bfb9-1',
        'cd690c62-0b5b-4cb9-9c8d-2fbaec09683d-3',
        '1abd58cc-645e-4a32-a4f1-277f88a4d0bb-4',
        'ff07167d-04f1-4c5c-a5ab-66337c374213-3',
        # page numbers by tj
        '20ffee6e-00aa-4fc9-bc84-888b5d803b67-1',
        '874a9c88-6672-48b0-90bf-2c637593a23c-2',
        'bd35ea37-787e-4b8e-87f1-aec088a3ceda-1',
        '324cb069-95ae-48a6-a10d-ecc3bfe14ce7-1',
        '916bc684-2b3a-4f85-8e6a-d28ce9eff07e-5',
        '833643ae-77ea-4e38-814d-998201a9afac-2',
        'a43d5dbe-b387-4754-bdf7-18b94af5b128-1',
        'fd6f8198-c53c-4589-8406-fd262aae5f2d-3',
        'c3dddc45-0dc8-48aa-a9ba-a826854e1c2e-4',
        'efeedada-db6a-4d52-aea3-3ce0a0cb963e-3',
        'b7e95599-f7aa-406c-95c9-ca9ad9296449-2',
        '133946ab-914f-4a9a-815b-f7fcb3d0a2b2-5',
        '06c246d2-e8d3-46ab-8161-671f721454fd-1',
        'f3fbf88e-7584-47e7-a3a0-aa12ec04b6f3-5',
        '6ccc3ab4-2f72-4ea1-be77-dde5273314e4-4',
        '63e91867-1260-4e46-8e5e-6866a7198d35-1',
        'f8706dfe-9f5a-4f14-a0e2-cf4839028c5b-5',
        '1e55ead1-b280-4bfd-86a0-0143d4768f7e-1',
        'c3b27dc7-3a68-45ca-a21f-338c71568e10-2',
        'a2f6336b-3fba-4711-80e1-9690c0833949-1',
        '41603517-45ed-4dfd-b729-0d57b79a3011-4',
        '5f9e2dcc-4255-4769-b403-03b621def541-5',
        '089e31d7-bbef-4a36-87d7-91d16c4767fe-2',
        'e6541d8b-7e05-4a3b-bf99-3ec60df29279-5',
        '54782301-b448-43e6-97dc-dc0dd336f52d-4',
        '622b1033-7f50-496a-9e45-9ae9f6694cc9-1',
        '73428559-b286-415c-b5b5-4a89288c3df1-4',
        '33d5a0cc-9da0-4fd5-ab43-ccacfe15e835-2',
        '2dad7f1e-92ba-45df-89fd-3263173603f7-2',
        '39e7c42b-b890-4558-b78e-750d7beda571-2',
        'a0e41edf-9a17-4f8b-8b94-372abe7c5185-1',
        '288bcbdc-c9a0-464e-9cc3-63c240ad16f2-2',
        'fd6f2af8-41ae-424e-9d54-30ac7362ada0-5',
        'ec46ffa7-05f8-4eb0-9f07-9138f8db48e2-3',
        'e0b9551e-1768-4ae7-b40a-bfb4c97966b3-1',
        '560f9779-f7a4-4a6c-9560-3f894362daf4-5',
        'bdd479f5-c43b-4ae3-8935-2a8174718679-5',
        '32d2e40b-c5fe-4a5f-a325-9b00da63a94b-3',
        '868c4041-329b-4947-b55d-5f7cb874a2aa-2',
        'e5740eb5-edc4-4521-aa6b-487e0c48a8de-5',
        '896544a9-39f1-4765-a072-f1ac359b3e09-3',
        '61847842-5e4b-4196-bf5f-1df6b95cc123-4',
        '010f5e34-1aa5-4920-a673-ee9cd53172b3-1',
        '8c35f5c2-35a0-4ec3-8237-3e13a05b0109-2',
        '5ab2c465-3a94-4fa3-bcbc-e6abbf8c4fa0-1',
        '5087a003-73d4-4e90-bf7b-6f5bb5657a3b-1',
        '80100108-6cab-42da-aefc-3889512fdd7b-5',
        '0b7c8b6f-220f-4b14-aae2-66048fb288e0-4',
        '0b1ae5c0-7b5a-4490-b166-0344030f6ac1-5',
        '2f907130-03f8-464f-9410-e1f3579ccf2e-3',
        'b1be332a-dd68-4cc2-b7a3-2d6ecd5e3e32-2',
        'e3b6e4b5-9261-4b58-a196-b009c133b7a5-3',
        '54abe86c-bd8d-44af-845e-d5001c67713e-2',
        'e3b6db7b-5def-4619-9bef-ddd3658108a0-5',
        '971931ad-8f95-4a91-b519-b95a13c3b90e-5',
        'ce697e93-d5b4-4d8a-a504-bce5815dd14b-4',
        '4eb622e8-dfac-45aa-9d06-d375e072e374-4',
        'e9e46bf7-7171-494a-a245-590216ee944e-4',
        'db4a788f-3ce7-4c02-b194-eb3c1bc78c58-2',
        '6b21f160-041e-46c7-b6c2-fc622b29b247-3',
        '5cf4355d-7178-4641-b3fe-855a6b93edb9-3',
        'cd0d4014-50fe-48db-80c9-37c72ba5fa90-5',
        'e5a98c6b-f8d0-48cc-8f91-d4c97596dcd4-3',
        '3d337fc7-75e1-4fb5-91f2-d057fbecf8f0-1',
        None,
        '8948098f-69e9-4c58-8851-9cde52aea440-5',
        '5d2c5c66-7943-4e07-aa51-4747aca50872-1',
        'a7a12c54-479c-4c50-a6ac-a9512d47617e-2',
        '43a7ac18-5ec6-418c-bccd-41211a103581-1',
        '454ecac6-1c30-40c7-b188-77da0c3a31ca-4',
        'b72048da-2a8f-4fc8-8aa1-970fd8885a70-2',
        '04e1c7df-a37c-437d-b7c0-8a1afa506320-3',
        'e894455d-b7cc-4960-9499-5ead9afd4e9d-4',
        'a0e35645-9e4a-4c16-a39d-d05e19c3fb19-1',
        'a32b1810-c8a0-4f5d-960f-7294811232bb-3',
        '8288e0be-ba22-42cc-ade8-304e768a1d0e-5',
        'd35e32ea-9e92-48ee-be47-8f3735555802-5',
        '85ec685b-7399-4702-a157-cfba93c1602a-1',
        'ad0ba6dc-ba7e-417a-8180-04c93808ded3-2',
        'b2ad7244-d95d-44b1-9e16-6b99f90e7cd1-4',
        '3f9b1523-b488-44dc-bde9-b2253aee738f-4',
        '17cd9288-0e1a-47bd-b6ea-50d90aa6c197-3',
        '6c3fcdef-0031-4f8f-b86b-ceb61b51c754-4',
        '2485da65-a2f1-4bdd-94af-5f02d3598d83-2',
        '3880b971-ddf4-4e50-8068-ea9bbfd97fa8-5',
        '2303e82f-eff4-4590-9066-d4020d82184f-2',
        '929d8244-3ae9-47c0-8eb6-541ffe9bedf6-3',
        'c7d653aa-fa88-4b8d-8fdc-a97a721b20f8-2',
        '07caf3dd-3ebd-4861-a12b-8ebc290e468c-1',
        '8aa74f12-6d76-4aa2-acb3-2a55fbee885f-5',
        '9c6af2ee-990a-4ba6-9aca-53c876a4ce81-1',
        'd8adcc44-3914-4598-9a7d-57da525f3106-4',
        '1a175835-bb74-4804-abcb-435213fa8b6f-2',
        '7f51df82-c69e-4a71-ac2f-6537d6c2915a-4',

        #here
        None, None, None, None, None, None, None, None, None,  # separator
        None, None, None, None, None, None, None, None, None,  # separator

        None, None, None, None, None, None, None, None, None,  # separator
        None, None, None, None, None, None, None, None, None,  #
        'ba8e5662-1b2f-48dd-a5ac-f537720d6de0-2',
        '98e04ff9-fadc-47af-bbd2-e2a869ceef51-3',
        'e307949d-6336-46e7-bb89-f4b5fc15374a-3',
        'e3ea915c-d93a-45e2-a4af-c2e05a807b6c-3',
        '9d656473-0d0e-47eb-9307-f809a8cf6f0b-5',
        'e08db1a7-b3f1-4758-87e6-85345b76db3e-3',
        '8d992b88-8df0-49fc-b53b-659c40f5cd07-5',
        '9c85d721-18e7-4da5-90f3-0d49e77985b5-2',
        '8d732adc-c244-4573-b9e0-c2c8c27cc4db-2',
        '5e038c9a-61ce-46a4-97d7-0a635a80638f-4',
        '1ebe7dae-ca57-4ead-813c-e035fb85f4af-2',
        'fe1b3e40-96fc-41a0-9fb3-286207b189ac-3',
        '26dded00-eaa0-4740-84da-c6888ae55389-3',
        '1701c7ad-c30e-4fbe-8f90-8e218e5469d0-1',
        None, None, None, None, None, None, None, None, None,  # separator
        None, None, None, None, None, None, None, None, None,  #
        '5d37938d-fb99-4611-a939-48e145bd357a-2',
        'd95c2e94-3820-4f31-b602-0533a630f5d5-5',
        '8f1c0116-2baf-4dbd-b51d-f8dbfbff360f-1',
        '66ae78a1-dee2-4411-ae5f-e82b638d344d-2',
        '896544a9-39f1-4765-a072-f1ac359b3e09-5',
        '12337ef2-e0b4-491d-9ca2-c0c80e209132-3',
        None, None, None, None, None, None, None, None, None,  # separator
        None, None, None, None, None, None, None, None, None,  #
        'e9c877e4-c270-4075-b18c-74d5e5285036-1',
        'dc56caac-7573-4ad6-a128-16c2baf71b8b-1',
        '72fa55bc-4758-4258-9181-f2643e5b3cb6-3',
        'db4e105f-760a-457a-8759-763f12555499-4',
        '57a3d5cc-e7eb-4bc5-9bd3-d37961920dea-5',
        '84a0d470-0d1e-4db9-a849-806c0d4dcfdd-1',
        '018d6030-d80e-46d0-ab85-07ccfbc4789b-4',
        '3bc47e66-9acf-4449-8942-f178bcc9ab75-3',
        '1d177182-20b5-4615-a51d-1ec278d0c562-2',
        '35b9242a-ddee-4204-9e04-e156269cbaec-4',
        '9758ea5c-452b-4e6c-ac3b-09b529df327a-2',
        '0ec64b6b-5ddf-4eea-a03b-0859965c3874-5',
        '9fea20ac-786e-4a2a-af69-ec4b13506ff2-1',
        '3acc774f-80dd-4665-b1a8-9f2fdadb724d-3',
        '71110eb2-dfec-416d-acbe-031e23597a4b-1',
        'f2e3b206-d98f-4d53-be80-6de290b99f19-5',
        '16774569-d4c4-45f8-8839-c0d9d8e4de33-4',
        '15cbca5d-cfa0-43ff-8c29-026c38238543-2',
        '3d5485c7-b164-4a40-9b56-64fcf41d404e-5',
        'bcd74599-a8f6-49a3-83de-958b371f4e91-4',
        '9dd92995-0b57-453d-bfca-5607b64ffae2-3',
        '86a4cf64-0393-455e-bab3-57a87828d1d1-3',
        '8a3deefb-a574-4539-a32b-7b4614f2c6a9-2',
        'eee78ee1-d183-4aa6-94ef-fe199dcbb1fc-5',
        '21f0cbff-db9e-4a96-8e8d-ca1901cdb00d-3',
        '78994fc6-05d5-44fd-ac8e-22955c2b49b4-4',
        '4074dcbe-8152-4d23-be88-babb475851e9-4',
        '65248194-0db0-420c-b7d0-d3c8a213d1bd-2',
        '219e1240-cf01-49d5-934f-217745bcb4df-2',
        'c581533e-83df-4094-b120-71c3a65576c5-4',
        'f694db7b-f7ba-46a9-bc0e-6ea8ed9b25b8-5',
        '8aced920-6007-4eb8-a724-3ac8b11b1653-5',
        '2334c29a-5e9a-4fd9-9689-5e67c839e245-4',
        'a2dbcab0-5b32-4899-920f-83cbb0bb764d-5',
        '4074dcbe-8152-4d23-be88-babb475851e9-2',
        'eadc18ec-8983-4f45-862a-559cc75e8d12-1',
        '27fb9c0b-e89c-4a21-b2e5-874bf4514032-5',
        '827eba31-6acb-4174-be41-1bd56bda6cde-1',

        None, None, None, None, None, None, None, None, None,  # separator
        None, None, None, None, None, None, None, None, None,  #
        '4c6b5494-6311-4508-b375-0bac665ab839-4',
        '17807de3-2338-47d6-aaee-a02906dc7db3-2',
        '0100075f-226e-466b-9611-25208d4a4660-2',
        'c8f2c993-597a-4636-8ba4-0aa56a773918-3',
        'b142d5d0-80ae-48a6-9cd6-667e4e001042-5',
        '2f8036b4-1bde-4a5c-8169-7c2cabc832bd-2',

        None, None, None, None, None, None, None, None, None,  # separator
        None, None, None, None, None, None, None, None, None,  #

        None, None, None, None, None, None, None, None, None,  # separator
        None, None, None, None, None, None, None, None, None,  #
        '5d9067ba-2d75-488f-be66-bb15cdafbf94-5',
        'a8c89491-03d7-484a-a705-d3fcaafe727e-3',
        'e105eaa2-699f-41c7-b37d-16777b7e9c1d-5',
        'f65bf072-3f20-462b-bff1-67aa0122723e-1',
        '6f2baef6-b904-4999-8013-698b17ef5c1f-5',

        None, None, None, None, None, None, None, None, None,  # separator
        None, None, None, None, None, None, None, None, None,  #
        'f78442b5-b498-4a47-b996-5f383ffff191-3',
        '3d04fbce-34d3-4d8b-a587-048fc422c868-5',
        'b8f3f272-3a97-464d-b183-3131db5ff0b8-4',
        'fcec99e6-a824-4af2-90b0-b9cfbe52a333-4',
        'c31a7ec5-1dac-413a-9fab-e60b018cf3e3-2',
        '6e096b7b-698a-42b9-8ca9-bfac0e988b26-2',
        'b7e02fdd-7196-413f-9102-c4dc8af0be5f-2',
        '9801c769-bab3-44f2-9fa2-832f2874090e-5',
        '7e365a79-8bb5-4465-8b47-474c7b94199c-1',
        '27c2bdfe-a3ae-44a8-90e6-a784d118b0cd-1',
        '051a2b92-2106-40b1-bb72-eb3584aa5552-5',
        '24628ec6-4db0-4e60-8dde-eab8377fb426-2',
        'a8fca1fe-2607-4dfb-b801-9b7342ac64ea-2',
        '5a86fcde-5a77-4a4b-90b6-7065e501f757-1',
        'c011d700-e8b3-43ed-ab74-eaed1f2c46da-1',
        'fb1a703d-6e86-4ce2-949d-9f4b6979eb32-5',
        '553f1024-7e78-4347-a43f-fdecf4c3c87b-3',
        'b4b71ce5-404c-4204-b34b-5a6528bfe4c5-2',
        '97a8d5df-aa2e-42d1-88b4-c5c1c9c30752-4',
        '0bad912a-85ab-498c-8005-58ead69df7f5-2',
        '11b27546-9189-44da-a9ad-021fc4278546-2',
        '553f1024-7e78-4347-a43f-fdecf4c3c87b-5',
        '781b11eb-dc29-4050-b3a6-9c578646c0a2-2',
        'e0196856-fe44-46b5-8b85-2f9bc4ca0f27-5',
        '8f43fde9-17c1-4257-93af-55cd7ae57a49-3',
        None, None, None, None, None, None, None, None, None,  # separator
        None, None, None, None, None, None, None, None, None,  #


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
        (1190, 1330),
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
        'efc8f8f2-18b2-4a80-bfc4-d8fcdef4af46-4',
        'b0ec1b2e-2227-4318-964b-3f5d619b619b-2',
        '13b9b6e5-74cf-43b5-a502-9b6dd5dc2206-2',
        '50d9655e-feae-49f6-be17-b91695c0b7ca-1',
        '9be8f5b2-aada-48af-8985-d43183b45c5b-1',
        'dede5745-4de5-4cba-92d0-4e0d679c27ec-3',
        'ae3d9620-5b76-4923-90fb-097a1bb8fb37-4',
        '2fe52d08-6699-42a2-92bd-73c3e7b28eba-4',
        '25070b4b-f4ba-4d1d-9cd3-c56d10c5a545-4',
        '4872d4b7-577c-45b9-911c-4a3d5dd94d9b-4',
        '6e1c51ae-2d58-4a4a-9584-4cec1ad43f97-3',
        '963c6ce9-167d-42dd-a368-94a3cec61cdf-5',
        '433b4986-dc21-4c8f-ac27-db8051a9bf6d-1',
        'a89007b4-0d3d-4f14-baae-9f347680cfbb-1',
        'a71c9404-7824-4e22-82da-70bc6e2f9bda-3',
        '746761d8-d0c9-46fa-8915-783c8983d12c-5',
        '24628ec6-4db0-4e60-8dde-eab8377fb426-5',
        '01f24881-32f9-4121-a3bc-3d8afeec5253-5',
        'a435f86f-4ce4-40b3-b97d-f7aa9b6ae6b3-1',
        'e8dc2925-9b1d-4cd4-939d-662aa8ebd2a5-1',
        '93753e58-0cd7-44c4-8406-397011d8ea2f-5',
        '9c85d721-18e7-4da5-90f3-0d49e77985b5-3',
        'b341312f-d54d-42bf-b4aa-9be16e5893ce-1',
        '2ceec095-71ac-49d5-a3fa-9c70a0351a80-1',
        '48b1b500-567e-4574-b986-6559129e93f1-2',
        '61eca3d9-c9d9-4e04-8295-3ea464c92b6e-2',
        '0e3973d9-fbc1-44fa-af00-c495843b5385-2',
        '931e33fd-ba70-465c-a4c8-5d2d0a36e498-5',
        '92a843b5-f2cc-41c0-a297-7176afbd6abe-2',
        '407dab0b-6cc0-4c6b-8939-1fca36879b21-1',
        '10a678e8-a663-4638-82ff-ae07039d57ff-1',  # o
        '21c18f16-427f-4a7e-aacb-2998d363154f-2',
        'db07c3bf-7cf7-4638-88ce-8d9453f0b874-3',
        '4cece000-e3d1-45cd-9c40-e7a46a80c885-2',
        '62512f39-d013-47c5-b364-0ffe90fc4588-3',
        None,
        '0a3442a9-6abc-4c3d-b999-459c1140307b-5',
        '40a77b83-c64a-4ac4-9e6f-c595fa6d77a0-1',
        None,
        '9ee3cfb7-5394-4cc8-85ed-588978216eb2-5',  # r
        'f54405dd-e8d4-49b7-8457-c981fc1618b9-2',
        'ec733ffb-3508-4b92-aa5d-bd33b72ff9ce-4',
        '11bd893d-0f34-4ac4-af6f-7ebea1ab49f7-3',
        'b299b8c7-a989-4721-bc0c-c324439b7b28-5',
        'f28dbbfb-3651-49bf-96e1-ce63a769137f-5',
        'a7a12c54-479c-4c50-a6ac-a9512d47617e-1',
        '2262ee87-2786-40e6-ae58-51b0946b2f8c-3',
        'b137580a-43e6-42cb-a32a-25dd389e7504-4',
        'e7d64056-2b1a-460b-815b-727dcf2acf91-2',
        'ee494916-557d-4915-aebb-d586be99aeef-3',
        'd8a2a22a-30f4-43da-9dae-23e2bb3769de-3',
        'd452d7ae-9fc2-458a-b987-862dadec9f82-3',
        '20bba6bf-199a-4c84-8e3d-eebd077c3d14-3',
        'f694db7b-f7ba-46a9-bc0e-6ea8ed9b25b8-4',

        'b883ec18-1f25-4acb-823d-872058266a42-2',
        'a6444c9f-dc1d-4460-893b-c874933be4e6-2',
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
        'fdf18e79-f5f5-438e-a695-a0e51090e353-1',
        'f11f389c-48f6-49eb-a6d7-c7994e1f5695-2',
        '24f2ebe0-b17c-4fc5-a5a0-71e1ffa18da3-5',
        '3f34a276-becc-4c31-b5b8-cd7cc65e81cf-4',
        '8d2425bb-54ca-4a89-ad9e-e1aaf226da6b-2',
        'c38e1e4b-7d82-4869-844c-cea4f05b8f5b-5',
        '6a1f45f7-b0f7-455a-b283-7e4ec6473259-1',
        '39c78bda-9a33-4757-b480-0813a2f86657-4',
        '6f755207-7188-4ec8-bfe4-82f1f2cd5a0f-1',
        '860050d1-0f4d-4384-b438-adefe7a7e5e3-3',
        'c9120dec-791a-4f42-ad59-b998592f7669-3',
        '055fcf75-6b6c-4b5e-ac5f-647072ff8763-4',
        'ea535e30-5f2f-4e92-8526-974784cc0846-2',
        'f2c8a596-090a-4056-b99a-5c3fe7acbbf9-5',
        '38026acf-330b-4ce6-9058-06cf14e654ed-3',
        'e3d8f253-1e02-45d7-8186-e6e6d6c03920-5',
        '7c08dd75-fd0c-4950-9a07-e83989b07c58-3',
        '601172ea-3429-48c6-9372-7b2abd216ee1-2',
        '94e1ab8a-5c2f-4b6b-8296-fddb6cdf5d45-3',
        '86252f32-9745-416a-9f39-a35dfa917a18-1',
        '30bdf6ef-3c8a-45e1-bd12-b88a062504c3-5',
        '3fa3197f-f28f-47fc-bb96-03e4ebd15e42-3',
        '61ad76c6-6a57-4bdb-b0db-c67067700770-3',
        'e43b9873-922f-4246-aa51-4483895240a3-1',
        '6bad2900-1c66-474b-bd80-c4b83e2acc78-3',
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