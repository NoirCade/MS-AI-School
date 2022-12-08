# 이미지 블렌딩 및 붙여넣기

import numpy as np
import cv2
import matplotlib.pyplot as plt

large_img = cv2.imread('../Top3.png')
watermark = cv2.imread('../GOAT.png')

# print(large_img.shape)
# print(watermark.shape)

img1 = cv2.resize(large_img, (800, 600))
img2 = cv2.resize(watermark, (800, 600))

# print('img1 >>> ', img1.shape)
# print('img2 >>> ', img2.shape)

# 혼합 진행
# blended = cv2.addWeighted(img1, 0.78, img2, 0.22, 0)
# cv2.imshow('image show', blended)
# cv2.waitKey(0)

# 1:1
blended = cv2.addWeighted(img1, 1, img2, 1, 0)
cv2.imshow('1:1', blended)
cv2.waitKey(0)

