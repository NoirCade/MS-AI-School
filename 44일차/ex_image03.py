import cv2

def image_show(image):
    cv2.imshow('show', image)
    cv2.waitKey(0)

image_path = './cat.png'

# 이미지 읽기
image = cv2.imread(image_path)

# 이미지 크롭 [시작 : 끝 : 단계]
# image_crop = image[10:, : 300]

# 반절된 고냥이를 볼 수 있다.
# image_show(image_crop)

# 좀 더 예쁘게 잘라보자
image_crop = image[30:360, 100:435]
image_show(image_crop)