import glob

import numpy as np
from torch.utils.data import Dataset
from PIL import Image
import cv2
import os

'''
오렌지: Orange
자몽: Grapefruit
레드향: Kanpei
한라봉: Dekopon
'''

label_dict = {'오렌지': 0, '자몽': 1, '레드향': 2, '한라봉': 3}


class custom_dataset(Dataset):
    def __init__(self, image_file_path, transform=None):
        self.image_file_paths = glob.glob(
            os.path.join(image_file_path, '*', '*.png'))
        self.transform = transform

    def __getitem__(self, index):
        # image loader
        image_path = self.image_file_paths[index]
        # image = Image.open(image_path)
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        label_temp = image_path.split('\\')[1]
        label = label_dict[label_temp]

        if self.transform is not None:
            image = self.transform(image=image)['image']
        image = image.float()
        # print(image)
        return image, label

    def __len__(self):
        return len(self.image_file_paths)


if __name__ == '__main__':
    test = custom_dataset('./dataset/train', transform=None)
    for i in test:
        pass