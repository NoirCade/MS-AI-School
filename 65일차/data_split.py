import glob
from PIL import Image
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split


def data_show(data_dir):

    x_plt = []
    y_plt = []
    for directory in os.listdir(data_dir):
        x_plt.append(directory)
        y_plt.append(len(os.listdir(os.path.join(data_dir, directory))))

    # creating the bar plot
    flg, ax = plt.subplots(figsize=(16, 16))
    plt.barh(x_plt, y_plt, color='maroon')

    # remove x,y ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # add padding between axis and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # show top values
    ax.invert_yaxis()

    plt.ylabel('Bark types')
    plt.xlabel('Num of images')
    plt.title('Bark texture dataset')
    plt.show()


def data_split(data_dir):
    each_path = []
    label_list = os.listdir(data_dir)

    for i in range(len(label_list)):
        # each_path[i]에 각 라벨의 전체 이미지 경로 저장
        each_label = label_list[i]
        each_path.append(glob.glob(os.path.join(data_dir, each_label, '*.jpg')))
        # print(len(each_path[i]))  # check each image amount

        each_train_data, each_val_list = train_test_split(each_path[i], test_size=0.2, random_state=99)
        each_val_data, each_test_data = train_test_split(each_val_list, test_size=0.5, random_state=99)

        count = 1
        for j in range(len(each_train_data)):
            train_image = Image.open(each_train_data[j])
            image_name = each_label + f'_{count}'
            os.makedirs('./data/train/' + each_label, exist_ok=True)
            train_image.save('./data/train/' + each_label + f'/{image_name}.png')
            count += 1

        for j in range(len(each_val_data)):
            val_image = Image.open(each_val_data[j])
            image_name = each_label + f'_{count}'
            os.makedirs('./data/val/' + each_label, exist_ok=True)
            val_image.save('./data/val/' + each_label + f'/{image_name}.png')
            count += 1

        for j in range(len(each_test_data)):
            test_image = Image.open(each_test_data[j])
            image_name = each_label + f'_{count}'
            os.makedirs('./data/test/' + each_label, exist_ok=True)
            test_image.save('./data/test/' + each_label + f'/{image_name}.png')
            count += 1


data_dir = 'D:/dataset'
# data_show(data_dir)
# data_split(data_dir)
