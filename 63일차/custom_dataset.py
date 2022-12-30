import glob
import os
import cv2
import torch
from torch.utils.data import Dataset
# from albumentations.pytorch import ToTensorV2
# import albumentations as A
import numpy as np


class customDataset(Dataset):
    def __init__(self, file_path, transform=None):
        '''
        ../archive
            - train
                - ace ~
                    - 001.jpg
                    - 002.jpg ...
                - jack ~
            - test
        '''
        self.file_path = glob.glob(os.path.join(file_path, '*', '*.jpg'))
        self.class_names = os.listdir(file_path)
        self.class_names.sort()
        self.transform = transform
        self.labels = []

        for path in self.file_path:
            self.labels.append(self.class_names.index(path.split('\\')[1]))
        self.labels = np.array(self.labels)

    def __getitem__(self, item):
        image_path = self.file_path[item]
        image = cv2.imread(image_path)

        label = self.labels[item]
        label = torch.tensor(label)
        if self.transform is not None:
            image = self.transform(image=image)['image']

        return image, label

    def __len__(self):
        return len(self.file_path)


test = customDataset('../archive/train')
for i in test:
    pass
