import glob
import os.path
from torch.utils.data import Dataset
from PIL import Image


class customDataset(Dataset):
    def __init__(self, data_path, transform=None):
        self.data_path = glob.glob(os.path.join(data_path, '*', '*.png'))
        self.transform = transform
        self.label_dic = {"cloudy": 0, "desert": 1, "green_area": 2, "water": 3}

    def __getitem__(self, item):
        img_path = self.data_path[item]
        label_name = img_path.split('\\')[1]
        label = self.label_dic[label_name]
        img = Image.open(img_path)

        if self.transform is not None:
            img = self.transform(img)

        return img, label

    def __len__(self):
        return len(self.data_path)

# test = customDataset('./dataset/train', transform=None)
# for i in test:
#     print(i)
#     pass