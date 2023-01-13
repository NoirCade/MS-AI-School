import glob
import os.path
from PIL import Image
from utils import image_file_list
from sklearn.model_selection import train_test_split

all_image = image_file_list('./data')
print(all_image)

os.makedirs('./dataset', exist_ok=True)

# label
#