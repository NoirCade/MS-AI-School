import cv2

img_path = './cat.png'
img = cv2.imread(img_path)

h, w, _ = img.shape

print('이미지 타입: ', type(img))
print('이미지 크기: ', img.shape)
print(f'이미지 높이 {h}, 이미지 넓이 {w}')
"""
이미지 타입:  <class 'numpy.ndarray'>
이미지 크기:  (399, 600, 3) (H, W, C) C: 채널 -> rgb값을 말함, 흑백은 C가 없다?
"""

# 이미지 읽기
cv2.imshow('image show', img)
cv2.waitKey(0)
# 이 명령어가 없으면 순식간에 프로그램이 종료되어버려서 이미지를 볼 수 없다!