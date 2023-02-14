import os
import glob

infected_gorani = glob.glob(os.path.join('C:/Users/user/Downloads/dataset', '*', 'labels', 'A01*.txt'))
# print(infected_gorani)
# exit()

for good_gorani in infected_gorani:
    with open(good_gorani, 'r', encoding='UTF-8') as txt:
        lines = txt.readlines()
        lines = lines[0]

    with open(good_gorani, 'w', encoding='UTF-8') as txt:
        txt.write(lines)
