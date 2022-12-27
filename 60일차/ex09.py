# 파이토치로 다층 퍼셉트론 구현
import torch
import torch.nn as nn

# GPU 사용가능 여부 파악
device = 'cuda' if torch.cuda.is_available() else 'cpu'
# print(device)

# xor 문제를 풀기 위한 입력과 출력값 정의
x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]

x = torch.tensor(x, dtype=torch.float32).to(device)
y = torch.tensor(y, dtype=torch.float32).to(device)
# 참고
# CrossEntropy의 경우, 마지막 레이어 노드 수가 2개 이상이어야 한다.
# 마지막 층이 1개의 output이라면, BCELoss를 써야한다.
# BCELoss 함수를 사용할 경우 마지막 레이어의 값을 0~1로 조정해줘야함
# 따라서 BCELoss 함수를 쓸 땐 마지막 레이어에 시그모이드 함수를 적용해야함!

# model
# 입력층, 은닉층 1, 은닉층 2, 은닉층 3, 출력층
model = nn.Sequential(
    nn.Linear(2, 10, bias=True),    # input_layer = 2, hidden_layer 1= 10
    nn.Sigmoid(),
    nn.Linear(10, 10, bias=True),   # hidden_layer 1 = 10, hidden_layer 2 = 10
    nn.Sigmoid(),
    nn.Linear(10, 10, bias=True),   # hidden_layer 2 = 10, hidden_layer 3 = 10
    nn.Sigmoid(),
    nn.Linear(10, 1, bias=True),    # hidden_layer 3 = 10, output_layer = 1
    nn.Sigmoid()                    # 우리가 사용할 Loss가 BCELoss이므로 마지막 레이어에 시그모이드 적용
).to(device)

criterion = torch.nn.BCELoss().to(device)
optimizer = torch.optim.SGD(model.parameters(), lr=0.051)

# 10000번 에포크를 실행합니다.
epoch_number = 100000
for epoch in range(epoch_number + 1):
    output = model(x)

    loss = criterion(output, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 100의 배수에 해당하는 에포크마다 loss print
    if epoch % 100 == 0:
        print(f'Epoch: {epoch} loss: {loss.item()}')

# 인퍼런스 코드
with torch.no_grad():
    output = model(x)
    predicted = (output > 0.5).float()
    acc = (predicted == y).float().mean()
    print('모델의 출력값 output ', output.detach().cpu().numpy())
    print('모델의 예측값 output ', predicted.detach().cpu().numpy())
    print('실제값 (Y) ', y.cpu().numpy())
    print('정확도 -> ', acc.item())
