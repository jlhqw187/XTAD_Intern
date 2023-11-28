import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np


folder_path = r'f:\xtad\datasets_0905/labels/val'
default_values = [0] * 35
# default_values_2 = [0] * 34
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
 'hat',
 'hand',
 ]
class_count = dict(zip(label_name_list, default_values))


for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        if filename == "classes.txt":
            continue
        with open(os.path.join(folder_path, filename), 'r') as file:
            lines = file.readlines()
            for line in lines:
                class_label = int(line.strip().split(' ')[0])
                # print(class_label)
                # print(filename)
                class_count[label_name_list[class_label]] += 1


labels = list(class_count.keys())
counts = list(class_count.values())


font = FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
plt.rcParams['font.family'] = font.get_name()
plt.figure(figsize=(20, 10))  

bar_width = 0.35
# x = np.arange(len(label_name_list))
plt.bar(labels, counts)

for i, count in enumerate(counts):
    plt.text(i, count + 1, str(count), ha='center', va='bottom')
plt.xlabel('标签')
plt.ylabel('数量')
plt.title('每个种类的出现次数')
plt.xticks(rotation=45) 
plt.savefig('0905.png')

plt.show()
