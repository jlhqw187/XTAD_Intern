import os
import re

# 定义文件名正则表达式模式
filename_pattern = r'fra831.*frame.*\.txt'

# 要写入的新数据
new_data = "1 0.512333 0.499083 0.860667 0.935780"

# 获取当前目录

current_dir = r"f:\xtad\lushan\labels\val\sth"

# 获取所有TXT文件并匹配文件名
txt_files = [f for f in os.listdir(current_dir) if f.endswith('.txt') and re.match(filename_pattern, f)]

# 遍历匹配的文件并修改内容
for txt_file in txt_files:
    file_path = os.path.join(current_dir, txt_file)
    
    # 打开文件以修改内容
    with open(file_path, 'w') as file:
        file.write(new_data + "\n")
