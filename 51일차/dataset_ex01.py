from torch.utils.data.dataset import Dataset
from torchvision import transforms
label_dic = {'cat': 0, 'dog': 1}


class MyCustomDataset(Dataset):
    def __init__(self, path):
        # data path등 데이터셋 정의하는 부분
        self.all_data_path = './image/*.jpg'
        self.transforms = transforms
        pass

    def __getitem__(self, index):
        image_path = self.all_data_path[index]
        # '이미지1, 이미지2, 이미지3 ...
        label_temp = image_path.split('/')
        # [., image, 이미지1.jpg] 이런식으로 나올 것
        label_temp = label_temp[2]
        label_temp = label_temp.replace('.jpg', '')
        label = label_dic[label_temp]
        # 라벨 딕셔너리에 정리

        # 이미지 읽기
        image = cv2.imread(image_path)

        # Augmentation
        if self.transforms is not None:
            image = self.transforms(image)

        return image, label


    def __len__(self):
        return len(self.all_data_path)
