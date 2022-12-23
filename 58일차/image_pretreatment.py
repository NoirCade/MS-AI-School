import argparse
import os
import glob
from PIL import Image
from sklearn.model_selection import train_test_split
import natsort


def expand2square(img, background_color):
    width_temp, height_temp = img.size
    if width_temp == height_temp:
        return img
    elif width_temp > height_temp:
        result = Image.new(
            img.mode, (width_temp, width_temp), background_color)
        result.paste(img, (0, (width_temp - height_temp)//2))
    elif width_temp < height_temp:
        result = Image.new(
            img.mode, (height_temp, height_temp), background_color)
        result.paste(img, (((height_temp - width_temp)//2), 0))

    return result


def image_processing(orange_data, grapefruit_data, kanpei_data, dekopon_data):
    orange = orange_data
    grapefruit = grapefruit_data
    kanpei = kanpei_data
    dekopon = dekopon_data

    fruits = [orange, grapefruit, kanpei, dekopon]
    for fruit in fruits:
        for i in fruit:
            # 이미지를 읽어서 expand2square 함수로 던진다
            fruit_name = i.split('\\')[1]
            file_name = i.split('\\')[2]
            resized_file_name = file_name.replace('.jpg', '.png')
            fruit_image = Image.open(i)
            resized_fruit = expand2square(
                fruit_image, (0, 0, 0)).resize((400, 400))

            # 전처리 파일 각각 폴더 생성 및 정렬하여 저장
            os.makedirs('./dataset/image/' + fruit_name + '/', exist_ok=True)
            resized_fruit.save('./dataset/image/' + fruit_name + f'/{resized_file_name}')

        # 리사이징 완료된 이미지를 train, val, test 데이터로 분리하여 저장
        resized_fruit_path = './dataset/image/' + fruit_name + '/'
        full_fruit_path = natsort.natsorted(glob.glob(os.path.join(resized_fruit_path, '*.png')))

        fruit_train, fruit_temp = train_test_split(full_fruit_path, test_size=0.1, random_state=77)
        print('===== ', fruit_name, ' train data >> ', len(fruit_train))
        fruit_val, fruit_test = train_test_split(fruit_temp, test_size=0.5, random_state=77)
        print(fruit_name, ' val data >> ', len(fruit_val))
        print(fruit_name, ' test data >> ', len(fruit_test))

        for i in range(len(fruit_train)):
            fruit_train_path = fruit_train[i]
            fruit_img_train = Image.open(fruit_train_path)
            fruit_train_name = os.path.basename(fruit_train_path)
            os.makedirs('./dataset/train/' + fruit_name, exist_ok=True)
            fruit_img_train.save('./dataset/train/' + fruit_name + f'/{fruit_train_name}')

        for i in range(len(fruit_val)):
            fruit_val_path = fruit_val[i]
            fruit_img_val = Image.open(fruit_val_path)
            fruit_val_name = os.path.basename(fruit_val_path)
            os.makedirs('./dataset/val/' + fruit_name, exist_ok=True)
            fruit_img_val.save('./dataset/val/' + fruit_name + f'/{fruit_val_name}')

        for i in range(len(fruit_test)):
            fruit_test_path = fruit_test[i]
            fruit_img_test = Image.open(fruit_test_path)
            fruit_test_name = os.path.basename(fruit_test_path)
            os.makedirs('./dataset/test/' + fruit_name, exist_ok=True)
            fruit_img_test.save('./dataset/test/' + fruit_name + f'/{fruit_test_name}')

    train_data = glob.glob(os.path.join('./dataset/train', '*', '*.png'))
    print('===== 분리 후 훈련 데이터 수 ', len(train_data))
    val_data = glob.glob(os.path.join('./dataset/val', '*', '*.png'))
    print('분리 후 검증 데이터 수 ', len(val_data))
    test_data = glob.glob(os.path.join('./dataset/test', '*', '*.png'))
    print('분리 후 테스트 데이터 수 ', len(test_data))


def image_file_check(opt):
    # 각 폴더별 데이터 양 체크
    '''
    image
        - 자몽
            - 자몽x.jpg
        -레드향
        -한라봉
        image_path -> ./image/자몽/*.jpg
    '''

    image_path = opt.image_folder_path

    # 전체 데이터 수
    all_data = glob.glob(os.path.join(image_path, '*', '*.jpg'))
    print('===== 전체 샘플 데이터 수 ', len(all_data))

    # 오렌지
    orange_data = glob.glob(os.path.join(image_path, '오렌지', '*.jpg'))
    print('오렌지 샘플 >> ', len(orange_data))

    # 자몽
    grapefruit_data = glob.glob(os.path.join(image_path, '자몽', '*.jpg'))
    print('자몽 샘플 >> ', len(grapefruit_data))

    # 레드향
    kanpei_data = glob.glob(os.path.join(image_path, '레드향', '*.jpg'))
    print('레드향 샘플 >> ', len(kanpei_data))

    # 한라봉
    dekopon_data = glob.glob(os.path.join(image_path, '한라봉', '*.jpg'))
    print('한라봉 샘플 >> ', len(dekopon_data))

    return orange_data, grapefruit_data, kanpei_data, dekopon_data


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image-folder-path', type=str, default='./image')
    opt = parser.parse_args()

    return opt


###   실행   ###
if __name__ == '__main__':
    opt = parse_opt()
    orange_data, grapefruit_data, kanpei_data, dekopon_data = image_file_check(opt)
    image_processing(orange_data, grapefruit_data, kanpei_data, dekopon_data)
