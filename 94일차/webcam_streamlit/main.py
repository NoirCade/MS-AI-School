import streamlit as st
import numpy as np
import pandas as pd
import io
import os
from PIL import Image
import cv2
import torch
import glob
import sys
from yolov5_master.hubconf import custom

sys.path.insert(0, './yolov5_master')

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
    #
    # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    #
    # model = custom(path="./yolov5_master/wild_animal_v5L.pt")
    #
    # model.conf = 0.6  # NMS confidence threshold
    # model.iou = 0.45  # NMS IoU threshold
    #
    # model.to(device)
    # image_path = picture
    #
    # for path in image_path:
    #     image = cv2.imread(path)
    #     outputs = model(image, size=640)
    #
    #     bbox = outputs.xyxy[0]
    #
    #     for box in bbox:
    #         x1 = box[0].item()
    #         y1 = box[1].item()
    #         x2 = box[2].item()
    #         y2 = box[3].item()
    #
    #         score = box[4].item()
    #         class_number = box[5].item()
    #
    #         cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 0), 2)
    #
    #     cv2.imshow("test", image)
    #     cv2.waitKey(0)

#실행   streamlit run main.py