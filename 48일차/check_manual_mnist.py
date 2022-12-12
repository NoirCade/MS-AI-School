import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os

print(len(mnist_data))
print(len(os.listdir('./imgs')))
img_dir = './imgs'
for i in range(5):
    file_name, label = mnist_data.iloc[i]
    img = cv2.imread(os.path.join(img_dir, file_name))
    plt.subplot(1, 5, i+1)
    plt.imshow(img, 'gray')
    plt.title(labels_map[label])