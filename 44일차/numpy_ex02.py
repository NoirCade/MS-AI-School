import numpy as np

# 복수 객체 저장하기
array1 = np.random.randint(10, size=10)
array2 = np.random.randint(20, size=20)

print('원본 출력 >>> ', array1, array2)

# 저장하기
np.savez('./save.npz', array1=array1, array2=array2)

# 객체 불러오기
data = np.load('./save.npz')
result1 = data['array1']
result2 = data['array2']

print('저장값1 출력 >>> ', result1)
print('저장값2 출력 >>> ', result2)


