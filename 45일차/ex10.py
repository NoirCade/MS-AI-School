import cv2
from utils import image_show
import numpy as np

image_path = './cat.png'
image = cv2. imread(image_path)

# 10x10 픽셀로 변환
image_color_10x10 = cv2.resize(image, (10, 10))
image_color_10x10.flatten()
# image_show(image_color_10x10)

# image 225x225 픽셀로 변환
image_color_255x255 = cv2.resize(image, (255, 255))
image_color_255x255.flatten()
# image_show(image_color_255x255)

x = np.array([[51, 40], [14, 19], [10, 7]])
x = x.flatten()
print(x)
# 예상 = [51, 40, 14, 19, 10, 7]
