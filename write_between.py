import os

# 起始文件名和结束文件名
start_filename = 'Video_20230904115037292__0000014000.txt'
end_filename = 'Video_20230917101008342__0002553300.txt'

# 获取当前目录
# current_dir = os.getcwd()
target_img_dir = r'F:\xtad\lushan_0906\no_bg\images\val'
target_lbl_dir = r"F:\xtad\lushan_0906\no_bg\val_labels"
new_data = "0 0.455667 0.462385 0.875333 0.922936"

# 获取所有TXT文件
img_files = [f for f in os.listdir(target_img_dir) if f.endswith('.jpg')]
# txt_files = [f for f in os.listdir(target_lbl_dir) if f.endswith('.txt')]
txt_files = [f.replace(".jpg", '.txt') for f in img_files]

# 标志，用于标识是否开始重命名
modifying = False

for img_file in img_files:
    txt_file = img_file.split('.')[0] + '.txt'
    if txt_file == start_filename:
        modifying = True
    if modifying:
        file_path = os.path.join(target_lbl_dir, txt_file)
        with open(file_path, 'w') as file:
            file.write(new_data + '\n')
    if txt_file == end_filename:
        break
