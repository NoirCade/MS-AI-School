import numpy as np
import cv2

# 이미지 경로
x = cv2.imread('./cat.png', 0) # 흑백 이미지
y = cv2.imread('./cat.png', 1) # 컬러 이미지
# print(x)
# print(y) # 이미지가 배열로 저장되어 있는 것을 볼 수 있음

# 이미지 열어보기
# cv2.imshow('cat image show gray ', x)
# cv2.imshow('cat image show ', y)
# img = cv2. resize(x, (200, 200))
# cv2.imshow('cat image resize show gray ', img)
# cv2.waitKey(0)

# 여러개 파일 save .npz
np.savez('./image.npz', array1=x, array2=y)

# 압축 방법
np.savez_compressed('./image_compressed.npz', array1=x, array2=y)

# 많은 수의 고용량 이미지 파일들을 로드해야하는 경우 직접 가져다 쓰다가는
# 컴퓨터가 터질... 수도 있으므로 Numpy로 바꿔서 쓰는 경우가 많다

# npz 데이터 로드
data = np.load('./image_compressed.npz')
result1 = data['array1']
result2 = data['array2']

cv2.imshow('result1', result1)
cv2.waitKey(0)
# 이미지는 waitKey(0) 이지만, 영상은 watiKey(1)을 줘야한다