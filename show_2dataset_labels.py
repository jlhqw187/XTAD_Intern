import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np


folder_path_1 = 'F:/xtad/数据标注/0824-花筐/labels/'
folder_path_2 = 'f:/xtad/b1b2_labels/train/'
default_values_1 = [0] * 34
default_values_2 = [0] * 34
label_name_list = [
 'pen',
 'phone',
 'key',
 'teapot',
 'ticket',
 'Id_card',
 'Bank_card',
 'Business_card',
 'Power_bank',
 'airpods',
 'wallet',
 'bracelet',
 'watch',
 'Head_rope',
 'Rubber_band',
 'ring',
 'comb',
 'other',
 'bag',
 'laptop',
 'Paper_money',
 'lipstick',
 'Ear_stud',
 'coin',
 'cigarette',
 'passport',
 'mouse',
 'charger',
 'Udisk',
  'cable',
 'suitcase',
 'water_bottle',
  'lighter',
 'hat'
 ]
class_count_1 = dict(zip(label_name_list, default_values_1))
class_count_2 = dict(zip(label_name_list, default_values_2))


for filename in os.listdir(folder_path_1):
    if filename.endswith('.txt'):
        if filename == "classes.txt":
            continue
        with open(os.path.join(folder_path_1, filename), 'r') as file:
            lines = file.readlines()
            for line in lines:
                class_label = int(line.strip().split(' ')[0])
                # print(class_label)
                # print(filename)
                class_count_1[label_name_list[class_label]] += 1

for filename in os.listdir(folder_path_2):
    if filename.endswith('.txt'):
        if filename == "classes.txt":
            continue
        with open(os.path.join(folder_path_2, filename), 'r') as file:
            lines = file.readlines()
            for line in lines:
                class_label = int(line.strip().split(' ')[0])
                # print(class_label)
                # print(filename)
                class_count_2[label_name_list[class_label]] += 1

labels_1 = list(class_count_1.keys())
counts_1 = list(class_count_1.values())

labels_2 = list(class_count_2.keys())
counts_2 = list(class_count_2.values())


font = FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
plt.rcParams['font.family'] = font.get_name()
plt.figure(figsize=(20, 10))  

bar_width = 0.35
x = np.arange(len(label_name_list))
plt.bar(x - bar_width / 2, counts_1, bar_width, label="0824")
plt.bar(x + bar_width / 2, counts_2, bar_width, label="b1b2")

for i in range(len(label_name_list)):
    plt.text(x[i] - bar_width / 2, counts_1[i] + 1, str(counts_1[i]), ha='center', va='bottom')
    plt.text(x[i] + bar_width / 2, counts_2[i] + 1, str(counts_2[i]), ha='center', va='bottom')

plt.xlabel('标签')
plt.ylabel('数量')
plt.title('每个种类的出现次数')
plt.xticks(x, label_name_list, rotation=45)
plt.legend()
plt.savefig('0824与b1b2比较.png')

plt.show()
