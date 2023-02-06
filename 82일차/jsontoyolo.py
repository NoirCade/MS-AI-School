import json
import os
file_path = "./test.json"

dir_path = "A:/CCTV/01.data/1.Train/label/object/illegal/food_truck"
data_tag = (os.path.dirname(dir_path)).split('/')[6]
dir_name = os.path.basename(dir_path)

classes = {'garbage_bag': 0, 'sit_board': 1, 'street_vendor': 2,
           'food_truck': 3, 'banner': 4, 'tent': 5, 'smoke': 6,
           'flame': 7, 'pet': 8, 'fence': 9, 'bench': 10, 'park_pot': 11, 'trash_can': 12,
           'rest_area': 13, 'toilet': 14, 'park_headstone': 15, 'street_lamp': 16, 'park_info': 17}

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            #print(file_path)

            with open(file_path, "r", encoding='UTF-8') as json_file:
                json_data = json.load(json_file)

                #print(json_data)
                #print(json_data["images"])
                print(json_data["annotations"])
                a = json_data["images"]
                #print(a)

                for i in a:
                    name = a['ori_file_name']
                    print(name.split('.', 1)[0])
                    txt_name = name.split('.', 1)[0]+'.txt'
                    height = a['height']
                    width = a['width']
                for j in json_data['annotations']:
                    print(j['bbox'][0][0])
                    print(j['object_class'])
                    obc = j['object_class']
                    label = classes[obc]
                    x1 = round(j['bbox'][0][0], 4)
                    y1 = round(j['bbox'][0][1], 4)
                    x2 = round(j['bbox'][1][0], 4)
                    y2 = round(j['bbox'][1][1], 4)
                    os.makedirs(f"./cvt/{data_tag}/{dir_name}", exist_ok=True)

                    with open(f"./cvt/{data_tag}/{dir_name}/{txt_name}", "a") as f:
                        f.write(f"{label} {x1} {y1} {x2} {y2} \n")
