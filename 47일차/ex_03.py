import cv2

large_img = cv2.imread('../Top3.png')
watermark = cv2.imread('../GOAT.png')

small_img = cv2.resize(watermark, (300, 300))

x_offset = 365
y_offset = 200

x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0]
# crop = large_img[y_offset:y_end, x_offset:x_end]
large_img[y_offset:y_end, x_offset:x_end] = small_img

cv2.imshow('img', large_img)
cv2.waitKey(0)