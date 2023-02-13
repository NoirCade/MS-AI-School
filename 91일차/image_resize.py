from utils import *
from PIL import Image
import json

all_path = image_file_list('./selected_images/sibirica')
count = 1

for image_path in all_path:
    label = image_path.split('\\')[0].split('/')[2]
    file = image_path.split('\\')[2].split('.')
    file_name = file[0] + '.' + file[1]
    folder_name = image_path.split('\\')[1]

    image = Image.open(image_path)
    image = image.resize((640, 640))
    save_folder = './data/resized_' + label + '/' + folder_name + '/'
    os.makedirs(save_folder, exist_ok=True)
    image.save(save_folder + file_name + '.png', 'png')

    json_name = image_path.split('/')[2].split('.')
    json_path = json_name[0] + '.' + json_name[1]
    read_json_path = './selected_json/' + json_path + '.json'

    with open(read_json_path, 'r', encoding='UTF-8') as json_file:
        json_txt = json.load(json_file)
        img_data = json_txt['images']
        annot_data = json_txt['annotations']

        for img_datum in img_data:
            x_ratio = 640/img_datum['width']
            y_ratio = 640/img_datum['height']
            for annot_datum in annot_data:
                label_num = annot_datum['category_id']
                label_name = annot_datum['category_name']
                x1 = annot_datum['bbox'][0][0]
                y1 = annot_datum['bbox'][0][1]
                x2 = annot_datum['bbox'][1][0]
                y2 = annot_datum['bbox'][1][1]

                yolox = ((x1 + x2) / 2) * x_ratio
                yoloy = ((y1 + y2) / 2) * y_ratio
                yolow = (x2 - x1) * x_ratio
                yoloh = (y2 - y1) * y_ratio

    resized_txt_path = './data/resized_' + label + '/' + folder_name + '/' + json_name[0].split('\\')[2] +'.' + json_name[1] + '.txt'
    # ./data/resized_coreanus/test/A08_F03_C074_C_211122_3005_30S_000003.023.txt
    with open(resized_txt_path, 'a', encoding='UTF-8') as txt:
        txt.write(str(label_num) + ' ' + str(round(yolox, 6)) + ' ' + str(round(yoloy, 6)) + ' ' + str(round(yolow, 6))
                  + ' ' + str(round(yoloh, 6)))

    print(count, read_json_path)
    count += 1
