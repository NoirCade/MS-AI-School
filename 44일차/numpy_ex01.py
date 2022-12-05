import numpy as np

# 단일 객체 저장 및 불러오기
array = np.random.randint(10, size=10)
print('원본 출력 >>> ', array)

# .npy 파일에 저장
np.save("./save.npy", array)

# 불러오기
result = np.load('./save.npy')
print('저장값 출력 >>> ', result)