'''
dataset
    - train
        - cat
            - cat.1.jpg ...
        - dog
    - val
        - cat
        - dog
    - test
        - cat
        - dog
'''

from torch.utils.data.dataset import Dataset
import os
import glob
from PIL import Image
label_dic = {'cat': 0, 'dog': 1}


class cat_dog_mycustomdataset(Dataset):
    def __init__(self, data_path):
        # csv 폴더 읽기, 변환 할당, 데이터 필터링 등 초기 논리를 할당
        self.all_data_path = glob.glob(os.path.join(data_path, '*', '*.jpg'))
        # print(self.all_data_path)

    def __getitem__(self, index):
        # 데이터 레이블 반환 image, label
        image_path = self.all_data_path[index]
        # print(image_path)
        img = Image.open(image_path).convert('RGB')
        label_temp = image_path.split('\\')
        # print(label_temp)
        label = label_dic[label_temp[1]]

        return img, label

    def __len__(self):
        # 전체 데이터 길이를 반환
        pass


test = cat_dog_mycustomdataset('./dataset/train/')

for i in test:
    pass