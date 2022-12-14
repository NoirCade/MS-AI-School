import os
import glob
from sklearn.model_selection import train_test_split
import cv2
import natsort
# 문자와 숫자가 섞여있다면 natsort를 사용해주는게 가장 좋다

cat_image_path = './image/image/cats'
dog_image_path = './image/image/dogs'

cat_image_full_path = natsort.natsorted(
    glob.glob(os.path.join(f'{cat_image_path}/*.jpg')))

dog_image_full_path = natsort.natsorted(
    glob.glob(os.path.join(f'{dog_image_path}/*.jpg')))

print('cat image size >> ', len(cat_image_full_path))
print('dog image size >> ', len(dog_image_full_path))

# train 80 val 20 -> val 10 test 10 으로 스플릿
cat_train_data, cat_val_data = train_test_split(
    cat_image_full_path, test_size=0.2, random_state=7777)

cat_val, cat_test = train_test_split(
    cat_val_data, test_size=0.5, random_state=7777)

print(f'cat train data :  {len(cat_train_data)}, cat val data : {len(cat_val)}, cat test data : {len(cat_test)}')

dog_train_data, dog_val_data = train_test_split(
    dog_image_full_path, test_size=0.2, random_state=7777)

dog_val, dog_test = train_test_split(
    dog_val_data, test_size=0.5, random_state=7777)

print(f'dog train data :  {len(dog_train_data)}, dog val data : {len(dog_val)}, dog test data : {len(dog_test)}')

# image cv2 imread 후 저장하는 방법
# mv coopy

flog = False
if flog:
    for cat_train_data_path, cat_val_path, cat_test_path in zip(cat_train_data, cat_val, cat_test):
        cat_img = cv2.imread(cat_train_data_path)
        cat_img_val = cv2.imread(cat_val_path)
        cat_img_test = cv2.imread(cat_test_path)
        cat_file_name = os.path.basename(cat_train_data_path)
        cat_file_name_val = os.path.basename(cat_val_path)
        cat_file_name_test = os.path.basename(cat_test_path)
        os.makedirs('./dataset/train/cat', exist_ok=True)
        os.makedirs('./dataset/val/cat/', exist_ok=True)
        os.makedirs('./dataset/test/cat/', exist_ok=True)
        cv2.imwrite(f'./dataset/train/cat/{cat_file_name}', cat_file_name)
        cv2.imwrite(f'./dataset/val/cat/{cat_file_name_val}', cat_img_val)
        cv2.imwrite(f'./dataset/test/cat/{cat_file_name_test}', cat_img_test)

for dog_train_data_path, dog_val_path, dog_test_path in zip(dog_train_data, dog_val, dog_test):
    dog_img = cv2.imread(dog_train_data_path)
    dog_img_val = cv2.imread(dog_val_path)
    dog_img_test = cv2.imread(dog_test_path)
    dog_file_name = os.path.basename(dog_train_data_path)
    dog_file_name_val = os.path.basename(dog_val_path)
    dog_file_name_test = os.path.basename(dog_test_path)
    os.makedirs('./dataset/train/dog/', exist_ok=True)
    os.makedirs('./dataset/val/dog/', exist_ok=True)
    os.makedirs('./dataset/test/dog/', exist_ok=True)
    cv2.imwrite(f'./dataset/train/dog/{dog_file_name}', dog_img)
    cv2.imwrite(f'./dataset/val/dog/{dog_file_name_val}', dog_img_val)
    cv2.imwrite(f'./dataset/test/dog/{dog_file_name_test}', dog_img_test)