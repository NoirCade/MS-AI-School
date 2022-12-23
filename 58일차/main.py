from dataset_temp import custom_dataset
import albumentations as A
from albumentations.pytorch import ToTensorV2
from torch.utils.data import DataLoader
import torch
import torch.nn as nn
import hy_parameter
from torchvision import models
from utils import train, validate, save_model

# OMP 중복실행 에러
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# device
device = torch.device('cpu')

# train aug
train_transform = A.Compose([
    A.Resize(height=224, width=224),
    ToTensorV2()
])

# val aug
val_transform = A.Compose([
    A.Resize(height=224, width=224),
    ToTensorV2()
])

# dataset
train_dataset = custom_dataset('./dataset/train', transform=train_transform)
val_dataset = custom_dataset('./dataset/val', transform=val_transform)

# dataloader
train_loader = DataLoader(train_dataset, batch_size=24, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=24, shuffle=False)

# model call
net = models.__dict__['resnet18'](pretrained=True)

# 모델에서 설정한 기본 변수들을 일부 변경할 경우
# pretrained = true, num_classes=4 수정하기
net.fc = nn.Linear(512, 3)  # input 512, output 4로 수정
net.to(device)

# criterion
criterion = nn.CrossEntropyLoss()

# optimizer
optim = torch.optim.Adam(net.parameters(), lr=hy_parameter.lr)

# model save dir
model_save_dir = './model_save'
os.makedirs(model_save_dir, exist_ok=True)

train(number_epoch=hy_parameter.epoch, train_loader=train_loader, val_loader=val_loader,
      criterion=criterion, optimizer=optim, model=net, save_dir=model_save_dir, device=device)
