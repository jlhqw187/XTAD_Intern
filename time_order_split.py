import os
import shutil
from tqdm import tqdm

# 源文件夹路径
source_folder = r"F:\xtad\debug_class_1103"

subfolders = [os.path.join(source_folder, d) for d in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, d))]
# print(subfolders)

train_ratio = 0.7
val_ratio = 1 - train_ratio

# 输出文件夹路径
output_folder = r"./output"
train_folder = os.path.join(output_folder, "train")
val_folder = os.path.join(output_folder, "val")

for subfolder in tqdm(subfolders):
    
    sub_train_folder = os.path.join(train_folder, subfolder.split("\\")[-1])
    sub_val_folder = os.path.join(val_folder, subfolder.split("\\")[-1])
    os.makedirs(sub_train_folder, exist_ok=True)
    os.makedirs(sub_val_folder, exist_ok=True)

    # 计算划分比例
    image_files = sorted([f for f in os.listdir(subfolder) if f.endswith('.jpg')])

    train_list = []
    val_list = []
    train_code, val_code = 0, 0

    for file in image_files:
        if val_code <= train_code:
            val_list.append(file)
            val_code += train_ratio
        else:
            train_list.append(file)
            train_code += val_ratio

    # 创建新文件夹



    # 复制文件到新文件夹
    for filename in tqdm(train_list):
        source_path = os.path.join(subfolder, filename)
        destination_path = os.path.join(sub_train_folder, filename)
        shutil.copy(source_path, destination_path)

    for filename in tqdm(val_list):
        source_path = os.path.join(subfolder, filename)
        destination_path = os.path.join(sub_val_folder, filename)
        shutil.copy(source_path, destination_path)
