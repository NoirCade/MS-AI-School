from utils import image_file, expand2square
from PIL import Image, ImageOps
import os

train_image_path = './dataset/train_image'
train_data = image_file(train_image_path)

test_image_path = './dataset/test_image'
test_data = image_file(test_image_path)

# print(len(train_data))    569개
# print(len(test_data))     318개

test_resize = False
if test_resize:
    t_path = './dataset/test.jpg'
    img = Image.open(t_path)
    img = ImageOps.exif_transpose(img)
    file_name_temp = t_path.split('/')[2]
    file_name = file_name_temp.split('.')[0]

    img_new = expand2square(img, (0, 0, 0)).resize((400, 400))

train_image_resize = True
if train_image_resize:
    for i in train_data:
        f_name_temp = i.split('\\')[2]
        file_name = f_name_temp.split('.')[0]
        f_name = i.split('\\')[1]

        if f_name == '0':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            # 저장
            os.makedirs('./data/train/0', exist_ok=True)
            img_new.save(f'./data/train/0/{file_name}.png')

        elif f_name == '1':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/train/1', exist_ok=True)
            img_new.save(f'./data/train/1/{file_name}.png')

        elif f_name == '2':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/train/2', exist_ok=True)
            img_new.save(f'./data/train/2/{file_name}.png')

        elif f_name == '3':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/train/3', exist_ok=True)
            img_new.save(f'./data/train/3/{file_name}.png')

        elif f_name == '4':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/train/4', exist_ok=True)
            img_new.save(f'./data/train/4/{file_name}.png')

        elif f_name == '5':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/train/5', exist_ok=True)
            img_new.save(f'./data/train/5/{file_name}.png')

        elif f_name == '6':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/train/6', exist_ok=True)
            img_new.save(f'./data/train/6/{file_name}.png')

        elif f_name == '7':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/train/7', exist_ok=True)
            img_new.save(f'./data/train/7/{file_name}.png')

        elif f_name == '8':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/train/8', exist_ok=True)
            img_new.save(f'./data/train/8/{file_name}.png')

        elif f_name == '9':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/train/9', exist_ok=True)
            img_new.save(f'./data/train/9/{file_name}.png')

test_image_resize = True
if test_image_resize:
    for i in test_data:
        f_name_temp = i.split('\\')[2]
        file_name = f_name_temp.split('.')[0]
        f_name = i.split('\\')[1]

        if f_name == '0':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            # 저장
            os.makedirs('./data/test/0', exist_ok=True)
            img_new.save(f'./data/test/0/{file_name}.png')

        elif f_name == '1':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/test/1', exist_ok=True)
            img_new.save(f'./data/test/1/{file_name}.png')

        elif f_name == '2':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/test/2', exist_ok=True)
            img_new.save(f'./data/test/2/{file_name}.png')

        elif f_name == '3':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/test/3', exist_ok=True)
            img_new.save(f'./data/test/3/{file_name}.png')

        elif f_name == '4':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/test/4', exist_ok=True)
            img_new.save(f'./data/test/4/{file_name}.png')

        elif f_name == '5':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/test/5', exist_ok=True)
            img_new.save(f'./data/test/5/{file_name}.png')

        elif f_name == '6':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/test/6', exist_ok=True)
            img_new.save(f'./data/test/6/{file_name}.png')

        elif f_name == '7':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/test/7', exist_ok=True)
            img_new.save(f'./data/test/7/{file_name}.png')

        elif f_name == '8':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/test/8', exist_ok=True)
            img_new.save(f'./data/test/8/{file_name}.png')

        elif f_name == '9':
            img = Image.open(i)
            img = ImageOps.exif_transpose(img)
            img_new = expand2square(img, (0, 0, 0)).resize((400, 400))
            os.makedirs('./data/test/9', exist_ok=True)
            img_new.save(f'./data/test/9/{file_name}.png')
