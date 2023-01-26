import torch
import cv2
import numpy as np
import os
import glob

from xml.etree import ElementTree as et
from config import CLASSES, RESIZE_TO, TRAIN_DIR, VALID_DIR, BATCH_SIZE
from torch.utils.data import Dataset, DataLoader
from utils import collate_fn, get_train_transform, get_valid_transform


# the dataset class
class MicrocontrollerDataset(Dataset):
    def __init__(self, dir_path, width, height, classes, transform=None):
        self.dir_path = dir_path
