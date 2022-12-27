# 다중 퍼셉트론으로 손글씨 분류
# 사이킷런에 있는 이미지 이용
import torch
import torch.nn as nn
from torch import optim
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()

# 첫번째 샘플을 출력 .images[인덱스] 8x8
# print(digits.images[1])

# 실제 레이블도 숫자 0인지 첫번째 샘플 레이어 확인 -> target[인덱스]
# print(digits.target[1])

# 전체 이미지 개수 확인
# print('전체 이미지 수: ', len(digits.images))

# 상위 5개 샘플 이미지를 확인
# zip() -> 묶음을 만드는 함수
'''
image = [1, 2, 3, 4]
label = [사과, 바나나, 자몽, 수박]
zip 할 경우
-> 1 사과, 2 바나나, 3 자몽, 4 수박 -> 이런 식으로 나온다
'''
image_and_label_list = list(zip(digits.images, digits.target))

# 이미지 체크
# for index, (image, label) in enumerate(image_and_label_list[:4]):
#     plt.subplot(2, 5, index + 1)
#     plt.axis('off')
#     plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
#     plt.title('sample: %i' % label)
# plt.show()

# 상위 라벨 5개 확인
# for i in range(5):
#     print(i, '번 index sample label: ', digits.target[i])

# train data and label
x = digits.data  # 이미지 데이터
y = digits.target   # 이미지 라벨

model = nn.Sequential(
    nn.Linear(64, 32),  # input_layer = 64, hidden_layer 1 = 32
    nn.ReLU(),
    nn.Linear(32, 16),  # hidden_layer 1 = 32, hidden_layer 2 = 16
    nn.ReLU(),
    nn.Linear(16, 10),  # hidden_layer 2 = 16, output_layer = 10
    # output이 10이므로 CrossentropyLoss() 이용
)
# 모델 체크
# print(model)

x = torch.tensor(x, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.int64)

loss_fun = nn.CrossEntropyLoss()    # 소프트 맥스 함수를 포함!
optimizer = optim.Adam(model.parameters())

losses = []  # loss 그래프 확인
epoch_number = 100

for epoch in range(epoch_number + 1):
    output = model(x)
    loss = loss_fun(output, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print('Epoch: [{:4d}/{} loss: {:.6f}'.format(
            epoch, epoch_number, loss.item()
        ))

    # append
    losses.append(loss.item())

plt.title('loss')
plt.plot(losses)
plt.show()