'''
opening은 erosion -> dilation 순서로 진행
샤프하게 만든 다음 부드럽게 해서 노이즈를 좀 제거 -> 작은 점 같은 노이즈를 잘 잡음
closing은 dilation -> erosion 순서로 진행
조금 더 부드럽게 만든 다음 샤프하게 해서 노이즈를 제거 -> 윤곽을 좀 더 정확하게 잘 잡음
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../pocket ball.png', cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

# datatype : int, float -> 파이썬에서는 메모리 제한이 없다
kernel = np.ones((3, 3), np.uint8)

erosion = cv2.erode(mask, kernel, iterations=1)
opening = cv2.dilate(erosion, kernel, iterations=1)
f_opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

# plt.figure(figsize=(9, 9))
# plt.subplot(1, 2, 1)
# plt.imshow(opening, 'gray')
# plt.title('manual opening')
#
# plt.subplot(1, 2, 2)
# plt.imshow(f_opening, 'gray')
# plt.title('function opening')
# plt.show()

N = 5
idx = 1
plt.figure(figsize=(9, 9))
for i in range(1, N + 1):
    erosion = cv2.erode(mask, kernel, iterations=i)
    opening = cv2.dilate(erosion, kernel, iterations=i)
    f_opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=i)

    plt.subplot(N, 2, idx)
    idx += 1
    plt.imshow(opening, 'gray')
    plt.title(f'{i} manual opening')

    plt.subplot(N, 2, idx)
    plt.imshow(f_opening, 'gray')
    plt.title(f'{i} function opening')
    idx += 1
plt.tight_layout()
plt.show()