import glob
import os
import random
import shutil

import cv2


def image_size(path):
    # list each image folder
    african_wildcat = glob.glob(os.path.join(path, 'african-wildcat', '*.jpg'))
    blackfoot_cat = glob.glob(os.path.join(path, 'blackfoot-cat', '*.jpg'))
    chinese_mountain_cat = glob.glob(os.path.join(path, 'chinese-mountain-cat', '*.jpg'))
    domestic_cat = glob.glob(os.path.join(path, 'domestic-cat', '*.jpg'))
    european_wildcat = glob.glob(os.path.join(path, 'european-wildcat', '*.jpg'))
    jungle_cat = glob.glob(os.path.join(path, 'jungle-cat', '*.jpg'))
    sand_cat = glob.glob(os.path.join(path, 'sand-cat', '*.jpg'))

    # show print
    print(f'african-wildcat >> {len(african_wildcat)}')
    print(f'blackfoot-cat >> {len(blackfoot_cat)}')
    print(f'chinese-mountain-cat >> {len(chinese_mountain_cat)}')
    print(f'domestic_cat >> {len(domestic_cat)}')
    print(f'european_wildcat >> {len(european_wildcat)}')
    print(f'jungle_cat >> {len(jungle_cat)}')
    print(f'sand_cat >> {len(sand_cat)}')


def create_train_val_split_folder(path):
    all_categories = os.listdir(path)
    print('All Categories >>\n', all_categories)
    os.makedirs('./dataset/train', exist_ok=True)
    os.makedirs('./dataset/val', exist_ok=True)

    for category in sorted(all_categories):
        os.makedirs(f'./dataset/train/{category}', exist_ok=True)
        all_image = os.listdir(path + f'/{category}/')
        for image in random.sample(all_image, int(0.9 * len(all_image))):
            # move from origin location to new location
            shutil.move(path + f'/{category}/{image}',
                        f'./dataset/train/{category}')

    for category in sorted(all_categories):
        os.makedirs(f'./dataset/val/{category}', exist_ok=True)
        all_image = os.listdir(path + f'/{category}/')
        for image in all_image:
            shutil.move(path + f'/{category}/{image}',
                        f'./dataset/val/{category}')


if __name__ == '__main__':
    path = 'C:/Users/labadmin/Downloads/Felis'
    # image_size(path)
    create_train_val_split_folder(path)