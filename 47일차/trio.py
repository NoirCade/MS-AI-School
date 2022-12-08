import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('../face01/haarcascade_frontalface_default.xml')

# 이미지 로드
img = cv2.imread('../trio.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 감지
faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

crop = []
for (x, y, w, h) in faces:
    crop.append(img[y:(y+h), x:(x+w)])
# print(len(crop))

# 마스킹
mask = np.zeros((683, 1024, 3), dtype='uint8')
cv2.rectangle(mask, (60, 50), (280, 280), (255, 255, 255), -1)
cv2.rectangle(mask, (420, 50), (550, 230), (255, 255, 255), -1)
cv2.rectangle(mask, (750, 50), (920, 280), (255, 255, 255), -1)

x_offset = [60, 420, 750]
y_offset = [50, 50, 50]

x_end = [280, 550, 920]
y_end = [280, 230, 280]

# 리사이징 및 마스킹
crop_resize = []

for i in range(3):
    crop_resize.append(cv2.resize(crop[i], (x_end[i] - x_offset[i], y_end[i] - y_offset[i])))
    mask[y_offset[i]:y_end[i], x_offset[i]:x_end[i]] = crop_resize[i]
# print(len(crop_resize))




cv2.imshow('original', img)
cv2.imshow('masked', mask)
cv2.waitKey(0)




