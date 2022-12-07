'''
Gradient: detect edge (dilation -> erosion)
Tophat: original - opening => (원본에서 오프닝을 뺀다) 밝은 부분 검출
Blackhat: closing - original => (클로징에서 원본을 뺀다) 엣지를 강조하는 연산 방법, 어두운 부분 검출
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../pocket ball.png', cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

op_idx = {
    'gradient' : cv2.MORPH_GRADIENT,
    'tophat' : cv2.MORPH_TOPHAT,
    'blackkhat' : cv2.MORPH_BLACKHAT
}

def onChange(k, op_name):
    if k == 0:
        cv2.imshow(op_name, mask)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k, k))
    dst = cv2.morphologyEx(mask, op_idx[op_name], kernel)
    cv2.imshow(op_name, dst)

cv2.imshow('origin', img)
cv2.imshow('gradient', mask)
cv2.imshow('tophat', mask)
cv2.imshow('blackhat', mask)

cv2.createTrackbar('k', 'gradient', 0, 300, lambda x: onChange(k=x, op_name='gradient'))
cv2.createTrackbar('k', 'gradient', 0, 300, lambda x: onChange(k=x, op_name='tophat'))
cv2.createTrackbar('k', 'gradient', 0, 300, lambda x: onChange(k=x, op_name='blackhat'))