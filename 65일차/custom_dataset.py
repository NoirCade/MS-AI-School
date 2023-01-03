import os
import glob
import numpy as np
from torch.utils.data import Dataset
from PIL import Image


class customDataset(Dataset):
    def __init__(self, data_path, transform=None):
        self.data_path = glob.glob(os.path.join(data_path, '*', "*.png"))
        self.label_list = os.listdir(data_path)
        self.label_dict = {}

        for i in range(len(self.label_list)):
            self.label_dict[self.label_list[i]] = int(i)

        self.transform = transform

    def __getitem__(self, item):
        image_path = self.data_path[item]
        image = Image.open(image_path)
        image = np.array(image)
        label_name = image_path.split('\\')[1]
        label = self.label_dict[label_name]
        # print(image, label)

        if self.transform is not None:
            image = self.transform(image=image)['image']

        return image, label

    def __len__(self):
        return len(self.data_path)


# test = customDataset('./data/train')
# for i in test:
#     pass