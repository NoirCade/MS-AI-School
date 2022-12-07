import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('../face01/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../face01/haarcascade_eye.xml')

face_img = cv2.imread('../face01/face.png')

face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(face_gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(face_img, (x, y), (x+w, y+h), (0, 255, 0), 3)

# cv2.imshow('face box', face_img)
# cv2.waitKey(0)

roi_img = face_img[y:y+h, x:x+w]
roi_gray = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY)
# cv2. imshow('roi', roi_img)
# cv2.waitKey(0)

eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)

for (x, y, w, h) in eyes:
    cv2.rectangle(roi_img, (x, y), (x+w, y+h), (0, 0, 255), 3)

# cv2.imshow('face box', face_img)
# cv2.waitKey(0)

# eyes 내부 정보를 바로 변수에 입력
eye_1 = eyes[0]
eye_2 = eyes[1]

eye_1_center = ((eye_1[0] + eye_1[2]/2), (eye_1[1] + eye_1[3]/2))
eye_2_center = ((eye_2[0] + eye_2[2]/2), (eye_2[1] + eye_2[3]/2))

# 입력 정보 확인
# print(eye_1_center, eye_2_center)

delta_x, delta_y = (eye_2_center[0] - eye_1_center[0],
                    eye_2_center[1] - eye_1_center[1])
# print(delta_x, delta_y)

theta = np.arctan(delta_y/delta_x)
angle = (theta * 180) / np.pi

# 이미지 중심 확인
(img_h, img_w) = face_img.shape[:2]
img_center = (img_w//2, img_h//2)

M = cv2.getRotationMatrix2D(img_center, angle, 1.0)

rotated_image = cv2.warpAffine(face_img, M, (img_w, img_h))
cv2.imshow('rotated', rotated_image)
# cv2.imwrite('rotated_woman.png', rotated_image)
cv2.waitKey(0)
