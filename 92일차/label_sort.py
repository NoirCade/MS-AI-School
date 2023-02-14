import glob
import os

label_list = glob.glob(os.path.join('C:/Users/user/Downloads/dataset', '*', 'labels', '*.txt'))
print(len(label_list))

for label in label_list:
    new_str = ''
    with open(label, 'r', encoding='UTF-8') as txt:
        lines = txt.readlines()
        new_line = ''
        for line in lines:
            line = line.split(' ')
            label_num = int(line[0])
            yolox = line[1]
            yoloy = line[2]
            yolow = line[3]
            yoloh = line[4]

            new_line = f'{label_num-1} {yolox} {yoloy} {yolow} {yoloh}'
            new_str = new_line + '\n' + new_str
            with open(label, 'w', encoding='UTF-8') as txt:
                txt.write(new_str)
