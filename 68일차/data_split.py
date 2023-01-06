import os
from sklearn.model_selection import train_test_split
from PIL import Image
from utils import image_file_list, expand2square


def data_split(root_path):
    label_dict = {'paper': 0, 'rock': 1, 'scissors': 2}
    paper_path = image_file_list(root_path + '/paper/')
    rock_path = image_file_list(root_path + '/rock/')
    scissors_path = image_file_list(root_path + '/scissors/')
    # print(f'Paper path: {paper_path}\nRock path: {rock_path}\nScissors path: {scissors_path}')

    # Train split
    paper_train, paper_temp = train_test_split(paper_path, test_size=0.2, random_state=99)
    rock_train, rock_temp = train_test_split(rock_path, test_size=0.2, random_state=99)
    scissors_train, scissors_temp = train_test_split(scissors_path, test_size=0.2, random_state=99)

    # Validation, Test split
    paper_val, paper_test = train_test_split(paper_temp, test_size=0.5, random_state=99)
    rock_val, rock_test = train_test_split(rock_temp, test_size=0.5, random_state=99)
    scissors_val, scissors_test = train_test_split(scissors_temp, test_size=0.5, random_state=99)

    # Data save - make label folder
    for i in label_dict.keys():
        os.makedirs('./dataset/train/' + i, exist_ok=True)
        os.makedirs('./dataset/val/' + i, exist_ok=True)
        os.makedirs('./dataset/test/' + i, exist_ok=True)

    # Train set
    i = 0
    for image_path in paper_train:
        image = Image.open(image_path)
        image = expand2square(image, (0, 0, 0)).resize((224, 224))
        image_name = str(i).zfill(3)
        i += 1
        image.save('./dataset/train/paper/train_' + image_name + '.png', 'png')

    i = 0
    for image_path in rock_train:
        image = Image.open(image_path)
        image = expand2square(image, (0, 0, 0)).resize((224, 224))
        image_name = str(i).zfill(3)
        i += 1
        image.save('./dataset/train/rock/train_' + image_name + '.png', 'png')

    i = 0
    for image_path in scissors_train:
        image = Image.open(image_path)
        image = expand2square(image, (0, 0, 0)).resize((224, 224))
        image_name = str(i).zfill(3)
        i += 1
        image.save('./dataset/train/scissors/train_' + image_name + '.png', 'png')

    # Validation set

    i = 0
    for image_path in paper_val:
        image = Image.open(image_path)
        image = expand2square(image, (0, 0, 0)).resize((224, 224))
        image_name = str(i).zfill(3)
        i += 1
        image.save('./dataset/val/paper/val_' + image_name + '.png', 'png')

    i = 0
    for image_path in rock_val:
        image = Image.open(image_path)
        image = expand2square(image, (0, 0, 0)).resize((224, 224))
        image_name = str(i).zfill(3)
        i += 1
        image.save('./dataset/val/rock/val_' + image_name + '.png', 'png')

    i = 0
    for image_path in scissors_val:
        image = Image.open(image_path)
        image = expand2square(image, (0, 0, 0)).resize((224, 224))
        image_name = str(i).zfill(3)
        i += 1
        image.save('./dataset/val/scissors/val_' + image_name + '.png', 'png')

    # Test set
    i = 0
    for image_path in paper_test:
        image = Image.open(image_path)
        image = expand2square(image, (0, 0, 0)).resize((224, 224))
        image_name = str(i).zfill(3)
        i += 1
        image.save('./dataset/test/paper/test_' + image_name + '.png', 'png')

    i = 0
    for image_path in rock_test:
        image = Image.open(image_path)
        image = expand2square(image, (0, 0, 0)).resize((224, 224))
        image_name = str(i).zfill(3)
        i += 1
        image.save('./dataset/test/rock/test_' + image_name + '.png', 'png')

    i = 0
    for image_path in scissors_test:
        image = Image.open(image_path)
        image = expand2square(image, (0, 0, 0)).resize((224, 224))
        image_name = str(i).zfill(3)
        i += 1
        image.save('./dataset/test/scissors/test_' + image_name + '.png', 'png')

