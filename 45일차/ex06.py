import cv2

# 이미지 경로
image_path = './cat.png'

# 이미지 읽기
image = cv2.imread(image_path)

# 이미지 좌우 및 상하 반전
# 1 좌우 반전, 0 상하 반전
dst_temp1 = cv2.cv2.flip(image, 1)
dst_temp2 = cv2.cv2.flip(image, 0)

cv2.imshow('dst_temp1', dst_temp1)
cv2.imshow('dst_temp2', dst_temp2)
cv2.waitKey(0)

# img90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
# img180 = cv2.rotate(image, cv2.ROTATE_180)
# img270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
#
# cv2.imshow("original image", image)
# cv2.imshow("rotate_90", img90)
# cv2.imshow('rotate_180', img180)
# cv2.imshow('rotate_270', img270)
#
# cv2.waitKey(0)