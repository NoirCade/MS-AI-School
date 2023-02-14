import glob
import os

label_list = glob.glob(os.path.join('C:/Users/user/Downloads/dataset', '*', 'labels', '*.txt'))
print(len(label_list))

for label in label_list:
    new_str = ''
    with open(label, 'r', encoding='UTF-8') as txt:
        lines = txt.readlines()
        for line in lines:
            non_normal_list = line.split(' ')
            non_normal_list[1] = round(float(non_normal_list[1])/640, 6)
            non_normal_list[2] = round(float(non_normal_list[2])/640, 6)
            non_normal_list[3] = round(float(non_normal_list[3])/640, 6)
            non_normal_list[4] = round(float(non_normal_list[4])/640, 6)
            normal_str = non_normal_list[0] + ' ' + str(non_normal_list[1]) + ' ' + str(non_normal_list[2]) + ' ' + \
                          str(non_normal_list[3]) + ' ' + str(non_normal_list[4])
            new_str = normal_str + '\n' + new_str

            with open(label, 'w', encoding='UTF-8') as txt:
                txt.write(new_str)
