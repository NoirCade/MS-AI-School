import glob
import os
from PIL import Image
import json


class data_spliter():
    def __init__(self, root_path):
        self.root_path = root_path

    def split_data(self):
        all_image_paths = glob.glob(os.path.join(root_path, '*', '*.jpg'))
        for image_path in all_image_paths:
            image_tag = image_path.split('\\')[5]
            image_name = image_path.split('\\')[6]
            os.makedirs(f'./yolov5-master/dataset/{image_tag}/images', exist_ok=True)
            img = Image.open(image_path)
            img.save(f'./yolov5-master/dataset/{image_tag}/images/{image_name}.jpg')

    def label_json_to_list(self):
        all_label_paths = glob.glob(os.path.join(root_path, '*', '*.json'))
        test_file_data = list()
        test_annot_data = list()
        train_file_data = list()
        train_annot_data = list()
        valid_file_data = list()
        valid_annot_data = list()

        for json_path in all_label_paths:
            json_tag = json_path.split('\\')[5]
            os.makedirs(f'./yolov5-master/dataset/{json_tag}/labels', exist_ok=True)

            # open each json file
            f = open(f'{json_path}')
            json_data = json.load(f)

            if json_tag == 'test':
                image_names = json_data['images']
                for image_name in image_names:
                    file_id = image_name['id']
                    file_name = image_name['file_name']
                    file_height = image_name['height']
                    file_width = image_name['width']

                    annot_data = json_data['annotations']
                    for annot in annot_data:
                        bbox_id = annot['id']
                        img_id = annot['image_id']
                        ctgr_id = annot['category_id']
                        bbox = annot['bbox']

                        json_x = bbox[0]
                        json_y = bbox[1]




            elif json_tag == 'train':
                image_names = json_data['images']
                for image_name in image_names:
                    file_id = image_name['id']
                    file_name = image_name['file_name']
                    file_height = image_name['height']
                    file_width = image_name['width']

                    train_file_data.append([file_id, file_name, file_height, file_width])

                annot_data = json_data['annotations']
                for annot in annot_data:
                    bbox_id = annot['id']
                    img_id = annot['image_id']
                    ctgr_id = annot['category_id']
                    bbox = annot['bbox']

                    train_annot_data.append([bbox_id, img_id, ctgr_id, bbox])

            elif json_tag == 'valid':
                image_names = json_data['images']
                for image_name in image_names:
                    file_id = image_name['id']
                    file_name = image_name['file_name']
                    file_height = image_name['height']
                    file_width = image_name['width']

                    valid_file_data.append([file_id, file_name, file_height, file_width])

                annot_data = json_data['annotations']
                for annot in annot_data:
                    bbox_id = annot['id']
                    img_id = annot['image_id']
                    ctgr_id = annot['category_id']
                    bbox = annot['bbox']

                    valid_annot_data.append([bbox_id, img_id, ctgr_id, bbox])

        return test_file_data, test_annot_data, train_file_data, train_annot_data, valid_file_data, valid_annot_data


def make_dict(img_data_list, annot_data_list):
    temp_dict = {img_info_dict['id']: img_info_dict for img_info_dict in img_data_list}
    print(temp_dict)


if __name__ == '__main__':
    root_path = 'C:\\Users\\labadmin\\Downloads\\animals.v2-release.coco'
    a = data_spliter(root_path)
    a.label_json_to_list()
    # test_file_list, test_annot_list, train_file_list, train_annot_list, valid_file_list, valid_annot_list = a.label_json_to_list()
    # make_dict(test_file_list, test_annot_list)

