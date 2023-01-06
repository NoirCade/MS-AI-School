import glob
import os
from torch.utils.data import Dataset
import cv2


# label_dict = {'paper': 0, 'rock': 1, 'scissors': 2}
class custom_dataset(Dataset):
    def __init__(self, root_path, transform=None):
        self.all_path = glob.glob(os.path.join(root_path, '*', '*.png'))
        self.transform = transform

    def __getitem__(self, item):
        label_dict = {'paper': 0, 'rock': 1, 'scissors': 2}
        image_path = self.all_path[item]
        label_name = image_path.split('\\')[1]
        label = label_dict[label_name]
        image = cv2.imread(image_path)

        if self.transform is not None:
            image = self.transform(image=image)['image']

        return image, label

    def __len__(self):
        return len(self.all_path)


# if __name__ == '__main__':
#     test = custom_dataset('./dataset/train')
#     for i in test:
#         pass
