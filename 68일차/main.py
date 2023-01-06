from custom_dataset import custom_dataset
from torch.utils.data import DataLoader
import torch
from torch import nn
from torch import optim
from torchvision import models
import albumentations as A
from albumentations.pytorch import ToTensorV2
from data_split import data_split
from timm.loss import LabelSmoothingCrossEntropy
from tqdm import tqdm
import matplotlib.pyplot as plt
import sys

device = 'cuda' if torch.cuda.is_available() else 'cpu'


def main():
    # Data preprocessing
    data_split('./data')

    # Augmentation
    train_transform = A.Compose([
        A.SmallestMaxSize(max_size=160),
        A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.05, rotate_limit=15, p=0.8),
        A.GaussianBlur(p=0.2),
        A.RandomBrightnessContrast(p=0.5),
        A.RandomShadow(p=0.5),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ToTensorV2()
    ])

    val_transform = A.Compose([
        A.SmallestMaxSize(max_size=160),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ToTensorV2()
    ])

    test_transform = val_transform

    # Dataset call
    train_dataset = custom_dataset('./dataset/train', transform=train_transform)
    val_dataset = custom_dataset('./dataset/val', transform=val_transform)
    test_dataset = custom_dataset('./dataset/test', transform=test_transform)

    # DataLoader
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

    # Model call
    net = models.__dict__['resnet18'](pretrained=True)
    num_ftrs = net.fc.in_features
    net.fc = nn.Linear(num_ftrs, 3)
    net.to(device)

    # Hyperparameters
    criterion = LabelSmoothingCrossEntropy().to(device)
    optimizer = optim.Adam(net.parameters(), lr=0.001)
    num_epochs = 50
    train_steps = len(train_loader)
    valid_steps = len(val_loader)
    save_path = './best.pt'

    for epoch in range(num_epochs):
        train_loss_ls = []
        val_loss_ls = []
        train_acc_ls = []
        val_acc_ls = []
        val_run_loss = 0
        running_loss = 0
        best_val_acc = 0
        val_acc = 0
        train_acc = 0

        net.train()
        train_bar = tqdm(train_loader, file=sys.stdout, colour='red')
        for step, data in enumerate(train_bar):
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = net(images)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            train_acc += (torch.argmax(outputs, dim=1) == labels).sum().item()
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            train_bar.desc = f'train epoch[{epoch + 1} / {num_epochs}], loss{loss.data:.3f}'


        net.eval()
        with torch.no_grad():
            valid_bar = tqdm(val_loader, file=sys.stdout, colour='red')
            for data in valid_bar:
                images, labels = data
                images, labels = images.to(device), labels.to(device)
                outputs = net(images)
                val_acc += (torch.argmax(outputs, dim=1) == labels).sum().item()
            val_run_loss += criterion(outputs, labels).item()
        val_accuracy = val_acc / len(val_dataset)
        train_accuracy = train_acc / len(train_dataset)

        train_loss_ls.append(running_loss/train_steps)
        val_loss_ls.append(val_run_loss/valid_steps)

        print(f'Epoch [{epoch + 1}/{num_epochs}] Train Loss: {(running_loss / train_steps):.3f} '
              f'Train Accuracy: {train_accuracy:.3f} Valid Accuracy: {val_accuracy:.3f}')

        if val_accuracy > best_val_acc:
            best_val_acc = val_accuracy
            torch.save(net.state_dict(), save_path)

    # loss 그래프 표현
    plt.subplots(1, 2, figsize=(12, 12))
    plt.subplot(121)
    plt.plot(train_loss_ls, '-r')
    plt.plot(val_loss_ls, '-b')
    plt.xlabel('Epoch')
    plt.ylabel("Loss")
    plt.legend(['train, val'])
    plt.title('Train vs Val Loss')

    plt.subplot(122)
    plt.plot(train_acc_ls, '-r')
    plt.plot(val_acc_ls, '-b')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend(['train, val'])
    plt.title('Train vs Val Acc')
    plt.show()


if __name__ == '__main__':
    main()
