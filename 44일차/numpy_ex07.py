# 넘파이의 얕은 복사와 깊은 복사
import numpy as np

array1 = np.arange(0, 10)
array2 = array1
array2[0] = 99
print('array1 >>> ', array1)
print('array2 >>> ', array2)
# array2를 수정했는데, array1도 변경됨! -> 얕은 복사

array3 = np.arange(5, 15)
array4 = array3.copy()
array4[0] = 99
print('array3 >>> ', array3)
print('array4 >>> ', array4)
# array3를 수정했지만, array4에는 영향이 없음! -< 깊은 복사

# 중복된 원소 제거
array = np.array([1, 2, 1, 2, 3, 4, 3, 4, 5])
print('중복 처리 전 >>> ', array)
print('중복 처리 후 >>> ', np.unique(array))

# np.isin() ->
# 내가 찾는 원소를 포함하고 있는지 여부를 각 index 위치에 true/false로 표시

array = np.array([1, 2, 3, 4, 5, 6, 7])
iwantit = np.array([1, 2, 3, 10])
print('유무 확인 >>> ', np.isin(array, iwantit))