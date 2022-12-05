# 열을 기준으로 원소 정렬
import numpy as np

np.random.seed(1)
array = np.random.randint(20, size=[2,5])
print('열 기준으로 정렬 전 >>> \n', array)

array.sort(axis=0)
print('열 기준으로 정렬 후 >>> \n', array)