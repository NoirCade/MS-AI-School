import cv2
import numpy as np
from PIL import ImageGrab

def reg_of_interest(image) :
    image_height = image.shape[0]
    polygons = np.array( [[ (200, image_height) , (1100, image_height), (550, 250) ]] )
    image_mask = np.zeros_like(image)
    cv2.fillPoly(image_mask, polygons, 255)
    masking_image = cv2.bitwise_and(image, image_mask)
    return masking_image

# 6. 케니에지 처리하는 함수
def canny_edge(image) :
    gray_conversion = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_conversion = cv2.GaussianBlur(gray_conversion, (5,5), 0)
    canny_conversion = cv2.Canny(blur_conversion, 50, 150)
    return canny_conversion

def show_lines(image, lines) :
    lines_image = np.zeros_like(image)
    if lines is not None :
        for i in range(len(lines)):
            for x1,y1,x2,y2 in lines[i]:
                cv2.line(lines_image,(x1,y1),(x2,y2),(255,0,0), 10)
    return lines_image

# 여러 선을, 하나의 선으로 만들어 주는 함수.
# 기울기와 y절편을 평균으로 해서 하나의 기울기와 y절편을 갖도록 만드는 방법.
def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1- intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameter = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameter[0]
        intercept = parameter[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    left_fit_average =np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis =0)
    left_line =make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)

    return np.array([[left_line, right_line]])

#이미지 가져오기
while(True):
    image = np.array(ImageGrab.grab(bbox=(0, 40, 1280, 720)))
    lanelines_image = image.copy()

    cv2.imshow('gta5', cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
