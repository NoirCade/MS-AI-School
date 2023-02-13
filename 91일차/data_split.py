import glob
import os.path
import shutil
from sklearn.model_selection import train_test_split

all_path = glob.glob(os.path.join('./selected_images/coreanus', '*.jpg'))

train_coreanus, temp_coreanus = train_test_split(all_path, test_size=4/14, shuffle=True)
valid_coreanus, test_coreanus = train_test_split(temp_coreanus, test_size=0.5, shuffle=True)

os.makedirs('./selected_images/coreanus/train', exist_ok=True)
for i in train_coreanus:
    name = i.split('\\')[1]
    shutil.move(i, f'./selected_images/coreanus/train/{name}')

os.makedirs('./selected_images/coreanus/valid', exist_ok=True)
for i in valid_coreanus:
    name = i.split('\\')[1]
    shutil.move(i, f'./selected_images/coreanus/valid/{name}')

os.makedirs('./selected_images/coreanus/test', exist_ok=True)
for i in test_coreanus:
    name = i.split('\\')[1]
    shutil.move(i, f'./selected_images/coreanus/test/{name}')
