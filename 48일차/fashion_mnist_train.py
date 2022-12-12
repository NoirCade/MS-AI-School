import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import Dataset
import os
from torchvision.io import read_image
import pandas as pd


class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file, names=['file_name', 'label'], skiprows=[0])
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        try:
            image = read_image(img_path)
        except:
            print(self.img_labels.iloc[idx, 0])
            exit()

        label = int(self.img_labels.iloc[idx, 1])

        if self.transform:
            image = self.transform(image)

        if self.target_transform:
            label = self.target_transform(label)

        return image, label


# Define Neural Network Model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 64)
        self.fc5 = nn.Linear(64, 32)
        self.fc6 = nn.Linear(32, 10)

    def forward(self, x):
        x = x.float()
        h1 = F.relu(self.fc1(x.view(-1, 784)))
        h2 = F.relu(self.fc2(h1))
        h3 = F.relu(self.fc3(h2))
        h4 = F.relu(self.fc4(h3))
        h5 = F.relu(self.fc5(h4))
        h6 = self.fc6(h5)

        return F.log_softmax(h6, dim=1)

# transform = transforms.Compose([
#                         transforms.ToTensor(),
#                         transforms.Normalize((0.1307,), (0.3081,))])

print('init model done')


# Prepare Data Loader

epochs = 10
lr = 0.01   # learning rate
momentum = 0.5  # 관성 -> local 최저점에서 멈추지 않고 global 최저점을 찾도록 하기 위함
no_cuda = True
seed = 1
log_interval = 200  # 200회마다 시스템 로그를 보여준다

use_cuda = not no_cuda and torch.cuda.is_available()

torch.manual_seed(seed)

device = torch.device('cuda' if use_cuda else 'cpu')

kwargs = {'num_workers': 1, 'pin_memory': True} if use_cuda else {}
# -> cpu의 core를 얼마나 사용할 것인가에 대한 설정 -> 여기서는 프로세스 1개만 사용

print('set vars and device done')


dataset = CustomImageDataset(
    annotations_file='./annotations.csv',
    img_dir='./imgs'
    )

dataset_test = CustomImageDataset(
    annotations_file='./annotations_test.csv',
    img_dir='./imgs/test'
    )

test_batch_size = 1000
train_loader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset_test, batch_size=test_batch_size, shuffle=True, **kwargs)

model = Net().to(device)
optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)
# loss를 최적화시키기 위해 적용되는 gradient를 조절하는 파라미터


def train(log_interval, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))


def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format
          (test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


for epoch in range(1, 11):
    train(log_interval, model, device, train_loader, optimizer, epoch)
    test(model, device, test_loader)
torch.save(model, './model_test.pt')