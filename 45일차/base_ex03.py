import cv2
import numpy as np
from utils import image_show

image = cv2.imread('./nice car.png')

# Creating out sharpening filter
filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

# depth값 -1 -> 입력 영상과 같은 depth를 사용하겠다!
sharpen_img = cv2.filter2D(image, -1, filter)
# cv2.imshow('org image', image)    # 원본과 비교
image_show(sharpen_img)
cv2.waitKey(0)