import cv2
import matplotlib.pyplot as plt

image_path = './cat.png'

# 이미지 호출
image = cv2.imread(image_path)

# RGB 형태로 컨버트 -> plt는 컨버트하지 않으면 색 반전이 발생함
# -> 종종 모델 학습이 잘 되지 않을 경우, 컨버트가 되지 않아서 문제가 될 때도 있다.
# -> 직접 이미지 출력해보고 확인해보아야 할 때가 있다.
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 사이즈 변환
image_50x50 = cv2.resize(image_rgb, (50, 50))

flg, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image_rgb)
ax[0].set_title('Original Image')
ax[1].imshow(image_50x50)
ax[1].set_title('Resized Image')
plt.show()

image_50x50 = cv2.cvtColor(image_50x50, cv2.COLOR_RGB2BGR)
cv2. imwrite('./cat_image_50x50.png', image_50x50)