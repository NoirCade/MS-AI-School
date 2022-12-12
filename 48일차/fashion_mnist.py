import numpy as np
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import os

# OMP 에러 해결
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# 데이터 다운로드
# -> 다운로드 값이 True여도 루트 경로에 파일이 있으면, 다운로드 하지 않는다!
# -> 따라서 루트값이 바뀌면 계속 다운로드하니, 루트값을 고정하는 것이 중요
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

# 데이터 시각화
# -> 해당 이미지들은 28x28 이미지이며, 바이너리 파일이어서 한 줄로 쭉 이어져 있다
img_size = 28
num_images = 5

with open('./data/FashionMNIST/raw/train-images-idx3-ubyte', 'rb') as f:
    _ = f.read(16)  # 17바이트부터 이미지 데이터여서 16바이트는 날린다
    buf = f.read(img_size*img_size*num_images)
    data = np.frombuffer(buf, dtype=np.uint8).astype(float)
    data = data.reshape(num_images, img_size, img_size, 1)
    image = np.asarray(data[1]).squeeze()
    plt.imshow(image, 'gray')
    plt.show()

with open('data/FashionMNIST/raw/train-labels-idx1-ubyte', 'rb') as f:
    _ = f.read(8)
    buf = f.read(num_images)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    print(labels[1])    # loss구하려면 라벨이 숫자여야하므로, 라벨은 전부 숫자로 되어있다.
# plt.title(f'{labels[0]}')
# plt.show()

# 라벨 목록
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3

# for i in range(1, cols*rows+1):
#     sample_idx = torch.randint(len(training_data), size=(1, )).item()
#     img, label = training_data[sample_idx]
#     figure.add_subplot(rows, cols, i)
#     plt.title(labels_map[label])
#     plt.axis('off')
#     plt.imshow(img.squeeze(), cmap='gray')
# plt.show()
# exit()