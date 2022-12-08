import numpy as np
import matplotlib.pyplot as plt
import cv2


### 그리기 위한 함수 생성
def drawhoughLinesOnImage(image, houghLine):
    for line in houghLine:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)


def draw_circle(img, circle):
    for co, i, in enumerate(circle[0, :], start=1):
        cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 255), 3)


# 1. 이미지 로드
image = cv2.imread('../OX.png')

# 2. grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Gaussian blur
image_blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)
image_edge = cv2.Canny(image_blurred, 50, 120)

# 4. 모서리 탐지
dis_repo = 1    # Distance resolution in pixels of the Hough grid
theta = np.pi / 180
threshold = 170

houghLine = cv2.HoughLines(image_edge, dis_repo, theta, threshold)
circles = cv2.HoughCircles(image_blurred, method=cv2.HOUGH_GRADIENT,
                           dp=0.7, minDist=12, param1=70, param2=80)

# 5. 빈 이미지 생성
houghImage = np.zeros_like(image)

drawhoughLinesOnImage(houghImage, houghLine)
draw_circle(houghImage, circles)

originalImageWithHough = blend_images(houghImage, image)

cv2.imshow('test', originalImageWithHough)
cv2.waitKey(0)