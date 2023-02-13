import os
import glob
import random
import shutil

all_path = glob.glob(os.path.join('C:/Users/user/Downloads/175.야생동물 활동 영상 데이터/01. 데이터/2.Validation/원천데이터/VS_08.멧토끼', '*.jpg'))

random.seed(345)
sel_list = random.sample(all_path, 1400)
print(sel_list)

os.makedirs('./selected_images/sibirica', exist_ok=True)

for path in sel_list:
    file_name = path.split('\\')[1]
    shutil.move(path, f'./selected_images/sibirica/{file_name}')
