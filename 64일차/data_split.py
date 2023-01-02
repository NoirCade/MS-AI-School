import os
import glob
from sklearn.model_selection import train_test_split
from PIL import Image

# 데이터를 나눠야하는데, 학습/평가/테스트 8:1:1로 분할
root_path = './data'
# cloudy 분할
label_list = os.listdir(root_path)
each_path = []

for i in range(len(label_list)):
    # 각 데이터들의 라벨명을 저장해두고, each_path[]에 라벨별로 파일 리스트 저장 + 분할한 데이터 저장할 폴더 생성
    label_name = label_list[i]
    each_path.append(glob.glob(os.path.join(root_path, label_name, '*.jpg')))
    # print(len(each_path[i]))  # check each data amount

    each_train_data, each_val_list = train_test_split(each_path[i], test_size=0.2, random_state=99)
    each_val_data, each_test_data = train_test_split(each_val_list, test_size=0.5, random_state=99)

    for j in range(len(each_train_data)):
        each_train_path = each_train_data[j]
        each_train_img = Image.open(each_train_path)
        each_train_name = os.path.basename(each_train_path).split('.')[0]
        os.makedirs('./dataset/train/' + label_name, exist_ok=True)
        each_train_img.convert('RGB').save('./dataset/train/' + label_name + f'/{each_train_name}.png', 'png')

    for j in range(len(each_val_data)):
        each_val_path = each_val_data[j]
        each_val_img = Image.open(each_val_path)
        each_val_name = os.path.basename(each_val_path).split('.')[0]
        os.makedirs('./dataset/val/' + label_name, exist_ok=True)
        each_val_img.convert('RGB').save('./dataset/val/' + label_name + f'/{each_val_name}.png', 'png')

    for j in range(len(each_test_data)):
        each_test_path = each_test_data[j]
        each_test_img = Image.open(each_test_path)
        each_test_name = os.path.basename(each_test_path).split('.')[0]
        os.makedirs('./dataset/test/' + label_name, exist_ok=True)
        each_test_img.convert('RGB').save('./dataset/test/' + label_name + f'/{each_test_name}.png', 'png')

