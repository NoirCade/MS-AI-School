import numpy as np

arr = np.array({1,2,3,4})
print(arr)
print(type(arr))

# 0으로 초기화된 배열

arr = np.zeros((3,3))
print(arr)

# 빈 값으로 만들어진 배열

arr = np.empty((4,4))
print(arr)

# 1로 가득찬 배열 - 아쉽지만 twos, threes는 없다;
# 배열 안의 모든 수는 실수형을 기본으로 한다

arr = np.ones((3,3))
print(arr)

# 배열의 생성

arr = np.arange(10)
print(arr)

# ndarray 배열의 모양, 차수, 데이터 타입 확인

arr = np.array([[1,2,3], [4,5,6]])
print(arr)

print(arr.shape)

print(arr.ndim)

print(arr.dtype)

arr_float = arr.astype(np.float64)
print(arr_float.dtype)

arr_str = np.array(['1','2','3'])
print(arr_str.dtype)

arr_int = arr_str.astype(np.int64)
print(arr_int.dtype)

# ndarray 배열의 연산

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

arr1 + arr2
np.add(arr1, arr2)

arr1 * arr2
np.multiply(arr1, arr2)

# ndarray 배열 슬라이싱 하기

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

arr_1 = arr[:2, 1:3]
print(arr_1)

arr_2=arr[:2, 1:]
print(arr_2)

print(arr[[0,1,2],[2,0,1]])

idx = arr > 3
print(idx)

print(arr[idx])

# 레드와인 정보를 이용한 활용

redwine = np.loadtxt(fname='winequality-red.csv',delimiter=';', skiprows=1)
print(redwine)

# 합계

print(redwine.sum())

# 평균

print(redwine.mean())

# 축(axis)

print(redwine.sum(axis=0))
print(redwine.mean(axis=0))

print(redwine[:,0].mean())

print(redwine.max(axis=0))
print(redwine.min(axis=0))