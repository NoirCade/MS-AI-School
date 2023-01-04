import os
import glob
from torch.utils.data import Dataset
import cv2


class chihuahuaDataset(Dataset):
    def __init__(self, root_path, transform=None):
        self.all_path = glob.glob(os.path.join(root_path, '*', '*.jpg'))
        self.transform = transform
        self.label_list = os.listdir(root_path)
        self.label_dict = {}

        for i in range(len(self.label_list)):
            self.label_dict[self.label_list[i]] = int(i)

    def __getitem__(self, item):
        image_path = self.all_path[item]
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_name = image_path.split('\\')[2]
        label_name = image_path.split('\\')[1]
        label = self.label_dict[label_name]

        if self.transform is not None:
            image = self.transform(image=image)['image']

        return image, label

    def __len__(self):
        return len(self.all_path)


# test = chihuahuaDataset('C:/Users/labadmin/Downloads/data04/train', transform=None)
# for i in test:
#     pass
