# 파이토치의 nn.Linear와 nn.Sigmoid로 로지스틱 회귀 구현
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# train datat -> Tensor
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]

# Tensor로 변환
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

# nn.Sequential() 함수는 Wx+b와 같은 수식과 시그모이드 함수와 같은 여러 함수들을 서로 연결해주는 역할
model = nn.Sequential(
    nn.Linear(2, 1),    # input idm = 2, output dim = 1
    nn.Sigmoid()    # 출력은 Sigmoid 함수를 거친다
)

optimizer = optim.SGD(model.parameters(), lr=0.1)
epoch_num = 1000

for epoch in range(epoch_num + 1):
    output = model(x_train)

    # loss
    loss = F.binary_cross_entropy(output, y_train)

    # loss H(x)로 개선
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        prediction = output >= torch.FloatTensor([0.5])  # 예측값이 기준(현재 0.5) 이상이면 True, 이하면 False
        correct_prediction = prediction.float() == y_train  # 예측값과 실제값이 같은 경우만 True
        acc = correct_prediction.sum().item() / len(correct_prediction)  # 정확도 계산
        print('Epoch: {:4d}/{} loss: {:.6f} acc: {:.2f}%'.format(
            epoch, epoch_num, loss.item(), acc * 100))

print(model(x_train))
