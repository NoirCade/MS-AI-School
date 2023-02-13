import os
import glob
import shutil

img_files = glob.glob(os.path.join('./selected_images/sibirica/test', '*.jpg'))
os.makedirs('./selected_json/sibirica/test', exist_ok=True)

for img_name in img_files:
    name = os.path.basename(img_name).split('.')
    json_name = name[0] + '.' + name[1] + '.json'

    shutil.move(f'./selected_json/sibirica/{json_name}',
                f'./selected_json/sibirica/test/{json_name}')
