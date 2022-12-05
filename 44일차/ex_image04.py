import cv2
# from ex_image03 import image_show 형식으로 다른 파일의 함수를 가져올 수 있다
def image_show(image):
    cv2.imshow('show', image)
    cv2.waitKey(0)


image_path = './cat.png'

# 이미지 읽기
image = cv2.imread(image_path)

# 이미지 블러
image_blury = cv2.blur(image, (10, 10))
image_show(image_blury)