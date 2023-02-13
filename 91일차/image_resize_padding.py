from utils import *
from PIL import Image

all_path = image_file_list('./selected_images/coreanus')

for image_path in all_path:
    label = image_path.split('\\')[0].split('/')[2]
    file = image_path.split('\\')[2].split('.')
    file_name = file[0] + '.' + file[1]
    folder_name = image_path.split('\\')[1]

    image = Image.open(image_path)
    image = expand2square(image, (0, 0, 0)).resize((640, 640))
    save_folder = './data/resized_' + label + '/' + folder_name + '/'
    os.makedirs(save_folder, exist_ok=True)
    image.save(save_folder + file_name + '.png', 'png')
