# Numpy에서 가장 많이 사용되는 함수
import numpy as np

# 1. 원소 정렬
# def -> 오름차순 정렬
# array = np.random.randint(20, size=5)
# np.save('./array.npy', array)
array_data = np.load('./array.npy') # [ 9 13 19  2  0]
print('기본 상태 >>> ', array_data)
array_data.sort()
print('오름차순 >>> ', array_data)   # [ 0  2  9 13 19]

# 내림차순 정렬
print('내림차순 >>> ', array_data[::-1])    # [19 13  9  2  0]