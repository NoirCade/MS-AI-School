import glob
import os
import cv2

img_path = "A:/CCTV/01.data/1.Train/image/object/illegal/food_truck"
img_tag = os.path.dirname(img_path).split('/')[6]
img_ctgr = os.path.split(img_path)[1]
txt_path = f'./cvt/{img_tag}/{img_ctgr}'

classes = {'garbage_bag': 0, 'sit_board': 1, 'street_vendor': 2,
           'food_truck': 3, 'banner': 4, 'tent': 5, 'smoke': 6,
           'flame': 7, 'pet': 8, 'fence': 9, 'bench': 10, 'park_pot': 11, 'trash_can': 12,
           'rest_area': 13, 'toilet': 14, 'park_headstone': 15, 'street_lamp': 16, 'park_info': 17}

new_class = {}
for k, v in classes.items():
    new_class[v] = k


image_path_list = glob.glob(os.path.join(img_path, "*.jpg"))
txt_path_list = glob.glob(os.path.join(txt_path, "*.txt"))
count = 0

for i in image_path_list:
    image = cv2.imread(i)
    image_height = image.shape[0]
    image_width = image.shape[1]
    image_resize = cv2.resize(image, (image_width//2, image_height//2))
    a = i.split('\\', 1)[1]
    txt_name = a.split('.', 1)[0]+'.txt'
    print(txt_name)

    with open(f'./cvt/{img_tag}/{img_ctgr}/{txt_name}', "r") as f:
        txt_file = f.readlines()

    for bbox_info in txt_file:
        print(bbox_info.split())
        bbox = bbox_info.split()
        x1 = int(float(bbox[1]))
        y1 = int(float(bbox[2]))
        x2 = int(float(bbox[3]))
        y2 = int(float(bbox[4]))
        label_number = int(bbox[0])
        cv2.rectangle(image_resize, (x1//2, y1//2), (x2//2, y2//2), (255, 255, 255), 2)
        cv2.putText(image_resize, '{}'.format(new_class[label_number]), (x1//2, y2//2), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 255, 255), 2)

    cv2.imshow("{}".format(a), image_resize)
    # cv2.resizeWindow("{}".format(a), int(image.shape[1]*(0.7)), int(image.shape[0]*(0.7)))
    # cv2.moveWindow("{}".format(a), 0, 0)
    cv2.waitKey()
    cv2.destroyAllWindows()
    if cv2.waitKey() == ord('q'):
        exit()
