import os
import shutil

img_path = "A:/CCTV/01.data/1.Train/image/object/illegal/food_truck"
img_tag = os.path.dirname(img_path).split('/')[6]
img_ctgr = os.path.split(img_path)[1]
cvt_path = f'./cvt/{img_ctgr}'
error_txt = './street_lamp_error.txt'


def error_img_move():
    os.makedirs(f'{img_path}/error')

    with open(f'{error_txt}', 'r') as f:
        error_list = f.readlines()

        for i in range(len(error_list)):
            error_name = error_list[i].split('.')[0]
            try:
                shutil.move(f'{img_path}/{error_name}.jpg', f'{img_path}/error/{error_name}.jpg', )

            except:
                pass


def error_txt_move():
    os.makedirs(f'{cvt_path}/error')
    with open(f'{error_txt}', 'r') as f:
        error_list = f.readlines()

        for i in range(len(error_list)):
            try:
                shutil.move(f'{cvt_path}/{i}.', f'{img_path}/error/{i}', )

            except:
                pass


if __name__ == '__main__':
    error_img_move()
    error_txt_move()
