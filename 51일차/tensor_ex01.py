import torch
import numpy as np

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)

# x_ones = torch.ones_like(x_data)
# print(f'Ones Tensor >> \n', x_ones)
#
# x_rand = torch.rand_like(x_data, dtype=torch.float)
# print(x_rand)
# torch.randn()

# shape = (3, 3)
# randn_tensor = torch.rand(shape)
# ones_tensor = torch.ones(shape)
# zeroes_tensor = torch.zeros(shape)
#
# print(f'Random Tensor >> \n, {randn_tensor} \n')
# print(f'Ones Tensor >> \n, {ones_tensor} \n')
# print(f'Zeroes Tensor >> \n, {zeroes_tensor} \n')

# tensor = torch.rand(3, 4)
#
# print(f'shape of tensor: {tensor.shape}')
# print(f'data type of tensor: {tensor.dtype}')
# print(f'device tensor stored on: {tensor.device}')

# tensor = torch.ones(4, 4)
# tensor[:, 1] = 3
# # print(tensor)
#
# t1 = torch.cat([tensor, tensor, tensor], dim=1)
# print(tensor*tensor)

# t = torch.ones(5)
# print('tensor -> ', t)
# n = [1, 1, 1, 1]
# print('numpy -> ', n)

# view
# t = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
# ft = torch.FloatTensor(t)
# print(ft.shape)
# print(ft.view([-1, 3])) # -1은 알아서 채워넣으라는 의미

# squeeze
# 3x1
# ft = torch.FloatTensor([[0], [1], [2]])
# print(ft)
# print(ft.shape)
# print(ft.squeeze())
# print(ft.squeeze().shape)

# unsqueeze
ft = torch.FloatTensor([[0, 1, 2]])
# print(ft)
# print(ft.shape)

# print(ft.unsqueeze(0))
# print(ft.unsqueeze(0).shape)

print(ft.view(1, -1))
print(ft.view(1, -1).shape )