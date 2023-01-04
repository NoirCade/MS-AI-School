import os.path
import sys
from tqdm import tqdm
import torch
import torchvision.models
from torch import nn
from utils import aug_function
from custom_dataset_chihuahua import chihuahuaDataset
from torch.utils.data import DataLoader
import pandas as pd

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

train_aug = aug_function(mode_flag='train')
val_aug = aug_function(mode_flag='val')

train_dataset = chihuahuaDataset('C:/Users/labadmin/Downloads/data04/train', transform=train_aug)
val_dataset = chihuahuaDataset('C:/Users/labadmin/Downloads/data04/test', transform=val_aug)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False)

finetune_net = torchvision.models.efficientnet_b3(pretrained=True)
finetune_net.classifier[1] = nn.Linear(1536, 7)
finetune_net.to(device)

loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(finetune_net.parameters(),
                              lr=0.005, weight_decay=0.006)   # 데이터 수가 매우 적어서 lr, weight_decay 아주 낮게 설정

num_epochs = 50
best_val_acc = 0.0

train_steps = len(train_loader)
valid_steps = len(val_loader)
save_path = './best_chihuahua.pt'
Accuracydf = pd.DataFrame(index=list(range(num_epochs)), columns=['Epochs', 'Accuracy'])

if os.path.exists(save_path):
    best_val_acc = max(pd.read_csv('./modelaccuracy_chihuahua.csv')['Accuracy'].tolist())
    finetune_net.load_state_dict(torch.load(save_path))

for epoch in range(num_epochs):
    running_loss = 0
    val_acc = 0
    train_acc = 0

    finetune_net.train()
    train_bar = tqdm(train_loader, file=sys.stdout, colour='red')
    for step, data in enumerate(train_bar):
        images, labels = data
        images, labels = images.to(device), labels.to(device)
        outputs = finetune_net(images)
        loss = loss_function(outputs, labels)

        optimizer.zero_grad()
        train_acc += (torch.argmax(outputs, dim=1) == labels).sum().item()
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        train_bar.desc = f'train epoch[{epoch+1} / {num_epochs}], loss{loss.data:.3f}'

    finetune_net.eval()
    with torch.no_grad():
        valid_bar = tqdm(val_loader, file=sys.stdout, colour='red')
        for data in valid_bar:
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = finetune_net(images)
            val_acc += (torch.argmax(outputs, dim=1) == labels).sum().item()

    val_accuracy = val_acc / len(val_dataset)
    train_accuracy = train_acc / len(train_dataset)

    Accuracydf.loc[epoch, 'Epoch'] = epoch + 1
    Accuracydf.loc[epoch, 'Accuracy'] = round(val_accuracy, 3)
    print(f'Epoch [{epoch+1}/{num_epochs}] Train Loss: {(running_loss / train_steps):.3f} '
          f'Train Accuracy: {train_accuracy:.3f} Validation Accuracy: {val_accuracy:.3f}')

    if val_accuracy > best_val_acc:
        best_val_acc = val_accuracy
        torch.save(finetune_net.state_dict(), save_path)

    if epoch == num_epochs-1:
        Accuracydf.to_csv('./modelAccuracy_chihuahua.csv', index=False)
