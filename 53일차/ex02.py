# 이미지 사이즈에 따라서 바인딩 위치 조절하기

import cv2
try:
    from cv2 import cv2
except ImportError:
    pass
import numpy as np


def cvTest():
    image = cv2.imread('./catNdog.png')
    y_ = image.shape[0]
    x_ = image.shape[1]

    target_size = 256
    x_scale = target_size / x_
    y_scale = target_size / y_
    print('x_scale >> ', x_scale, '\ny_scale >> ', y_scale)

    img = cv2.resize(image, (target_size, target_size))
    bboxes = [[3.96, 183.38, 200.88, 214.03], [468.94, 92.01, 171.06, 248.45]]
    for boxes in bboxes:
        x_min, y_min, w, h = boxes

        x1 = int(np.round(x_min * x_scale))
        y1 = int(np.round(y_min * y_scale))
        x2 = int(np.round((x_min+w) * x_scale))
        y2 = int(np.round((y_min+h) * y_scale))

        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 1)

    cv2.imshow('test', img)
    cv2.waitKey(0)



if __name__ == '__main__':
    cvTest()