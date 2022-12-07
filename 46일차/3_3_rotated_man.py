import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('../face01/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../face01/haarcascade_eye.xml')

# 이미지 로드 및 흑백 이미지 준비
face_img = cv2.imread('../face01/face01.png')
face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

# 로드된 이미지 확인
# cv2.imshow('face', face_img)
# cv2.waitKey(0)

# 얼굴 감지 및 범위 표시
faces = face_cascade.detectMultiScale(face_gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(face_img, (x, y), (x+w, y+h), (0, 255, 0), 3)

# 감지된 이미지 확인
# cv2.imshow('face detected', face_img)
# cv2.waitKey(0)

# roi 표시 및 확인
roi_img = face_img[y:y+h, x:x+w]
roi_gray = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('roi', roi_img)
# cv2.waitKey(0)

# 눈 감지 및 위치 표시
eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)

for (x, y, w, h) in eyes:
    cv2.rectangle(roi_img, (x, y), (x+w, y+h), (255, 0, 0), 3)

# 감지된 이미지 학인하고 저장
# cv2.imshow('eyes detected', face_img)
# cv2.imwrite('detected man.png', face_img)
# cv2.waitKey(0)

# 눈 중심 위치 수치화
eyes_1_center = ((eyes[0][0] + eyes[0][2]/2), eyes[0][1] + eyes[0][3]/2)
eyes_2_center = ((eyes[1][0] + eyes[1][2]/2), eyes[1][1] + eyes[1][3]/2)

# print(eyes_1_center, eyes_2_center)

# 각도 산출
delta_x, delta_y = (eyes_2_center[0] - eyes_1_center[0],
                   eyes_2_center[1] - eyes_1_center[1])

theta = np.arctan(delta_y/delta_x)
angle = (theta * 180) / np.pi

# 이미지 중심 산출
img_h, img_w = face_img.shape[:2]
img_center = (img_w//2, img_h//2)

M = cv2.getRotationMatrix2D(img_center, angle, 1.0)

rotated_img = cv2.warpAffine(face_img, M, (img_w, img_h))

cv2.imshow('rotated', rotated_img)
# cv2.imwrite('rotated_man.png', rotated_img)
cv2.waitKey(0)
