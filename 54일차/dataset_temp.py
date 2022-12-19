import glob
from torch.utils.data import Dataset
from PIL import Image
import os

label_dict = {'dekopon': 0, 'grapefruit': 1, 'kanpei': 2, 'ornage': 3}

class custom_dataset(Dataset):
    def __init__(self, image_file_path, transform=None):
        self.image_file_paths = glob.glob(
            os.path.join(image_file_path, '*', '*.png'))
        self.transform = transform

    def __getitem__(self, index):
        # image loader
        image_path = self.image_file_paths[index]
        image = Image.open(image_path)
        label_temp = image_path.split('\\')[1]
        label = label_dict[label_temp]
        print(label)

        return image, label

    def __len__(self):
        return len(self.image_file_paths)


if __name__ == '__main__':
    test = custom_dataset('./dataset/train', transform=None)
    for i in test:
        pass