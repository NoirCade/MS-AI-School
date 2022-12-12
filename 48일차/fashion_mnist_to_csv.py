import numpy as np
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import os

# OMP 에러 해결
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# 데이터 다운로드
training_data = datasets.FashionMNIST(
    root='data',
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root='data',
    train=False,
    download=True,
    transform=ToTensor()
)

img_size = 28

# 데이터 로드

imgf = open('./data/FashionMNIST/raw/train-images-idx3-ubyte', 'rb')
imgd = imgf.read(16)    # 이미지 헤더
lblf = open('./data/FashionMNIST/raw/train-labels-idx1-ubyte', 'rb')
lbuf = lblf.read(8) # 라벨 헤더
df_dict = {
    'file_name': [],
    'label': []
}   # 데이터 프레임용 딕셔너리

idx = 0
while True:
    imgd = imgf.read(img_size*img_size) # 이미지 하나만 불러오기
    if not imgd:
        break

    data = np.frombuffer(imgd, dtype=np.uint8).astype(np.int64) # 바이트 -> 넘파이 행렬로 변환
    data = data.reshape(1, img_size, img_size, 1)   # 이미지 형태로 변환
    image = np.asarray(data).squeeze()

    lbld = lblf.read(1)
    labels = np.frombuffer(lbld, dtype=np.uint8).astype(np.int64)
    file_name = f'{idx}.png'
    cv2.imwrite(f'./imgs/{file_name}', image)
    idx += 1
    df_dict['label'].append(labels[0])
    df_dict['file_name'].append(file_name)

df = pd.DataFrame(df_dict)
print('----- training df ----- \n', df)
df.to_csv('./annotations.csv')


imgf_test = open('./data/FashionMNIST/raw/t10k-images-idx3-ubyte', 'rb')
imgd_test = imgf_test.read(16)    # 이미지 헤더
lblf_test = open('./data/FashionMNIST/raw/t10k-labels-idx1-ubyte', 'rb')
lbuf_test = lblf_test.read(8) # 라벨 헤더
df_dict_test = {
    'file_name': [],
    'label': []
}   # 데이터 프레임용 딕셔너리

idx = 0
while True:
    imgd_test = imgf_test.read(img_size*img_size) # 이미지 하나만 불러오기
    if not imgd_test:
        break

    data = np.frombuffer(imgd_test, dtype=np.uint8).astype(np.int64) # 바이트 -> 넘파이 행렬로 변환
    data = data.reshape(1, img_size, img_size, 1)   # 이미지 형태로 변환
    image = np.asarray(data).squeeze()

    lbld_test = lblf_test.read(1)
    labels = np.frombuffer(lbld_test, dtype=np.uint8).astype(np.int64)
    file_name = f'{idx}.png'
    cv2.imwrite(f'./imgs/test/{file_name}', image)
    idx += 1
    df_dict_test['label'].append(labels[0])
    df_dict_test['file_name'].append(file_name)

df_test = pd.DataFrame(df_dict_test)
print('----- test df ----- \n', df_test)
df_test.to_csv('./annotations_test.csv')