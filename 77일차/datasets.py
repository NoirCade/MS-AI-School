import torch
import cv2
import numpy as np
import os
import glob

from xml.etree import ElementTree as et
from config import CLASSES, RESIZE_TO, TRAIN_DIR, VALID_DIR, BATCH_SIZE
from torch.utils.data import Dataset, DataLoader
from utils import collate_fn, get_train_transform, get_valid_transform


# dataset class
class MicrocontrollerDataset(Dataset):
    def __init__(self, dir_path, width, height, classes, transform=None):
        self.dir_path = dir_path
        self.width = width
        self.height = height
        self.classes = classes
        self.transform = transform

        # get all image paths in sorted order
        self.image_paths = glob.glob(f'{self.dir_path}/*.jpg')
        self.all_images = [image_path.split('/')[-1]
                           for image_path in self.image_paths]
        self.all_images = sorted(self.all_images)

    def __getitem__(self, idx):
        # capture image name and full image path
        image_name = self.all_images[idx]
        image_path = os.path.join(self.dir_path, image_name)

        # read image
        image = cv2.imread(image_path)

        # convert BGR2RGB & resize
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
        image_resized = cv2.resize(image, (self.width, self.height))
        image_resized /= 255.0

        # capture corresponding xml file for getting annotations
        annot_filename = image_name[:-4] + '.xml'
        annot_file_path = os.path.join(self.dir_path, annot_filename)

        boxes = []
        labels = []
        tree = et.parse(annot_file_path)
        root = tree.getroot()

        # get width and height data
        image_width = image.shape[1]
        image_height = image.shape[0]

        for member in root.findall('object'):
            labels.append(self.classes.index(member.find('name').text))

            # xmin
            xmin = int(member.find('boundbox').find('xmin').text)
            # xmax
            xmax = int(member.find('boundbox').find('xmax').text)
            # ymin
            ymin = int(member.find('boundbox').find('ymin').text)
            # ymax
            ymax = int(member.find('boundbox').find('ymax').text)

            # resize bounding boxes
            xmin_final = (xmin / image_width)*self.width
            xmax_final = (xmax / image_width)*self.width
            ymin_final = (ymin / image_height)*self.height
            ymax_final = (ymin / image_height)*self.height

            boxes.append([xmin_final, ymin_final, xmax_final, ymax_final])

    def __len__(self):
        pass