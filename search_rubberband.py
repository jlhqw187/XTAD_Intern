import cv2
import os

# 定义标签文件和图像文件的路径
image_dir = r'f:\xtad\datasets_0830\images\all'
label_dir = r'f:\xtad\datasets_0830\labels\all'
save_dir = r"./save_temp"
# 获取图像文件列表
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

for image_file in image_files:
    # 构建图像文件路径
    image_path = os.path.join(image_dir, image_file)

    # 读取图像
    image = cv2.imread(image_path)

    # 构建标签文件路径（假设标签文件与图像文件同名，只是扩展名不同）
    label_file = os.path.splitext(image_file)[0] + '.txt'
    label_path = os.path.join(label_dir, label_file)

    # 打开标签文件并读取标签信息
    with open(label_path, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        # 每行标签的格式通常为：class_id x_center y_center width height
        # 将这些信息解析出来
        parts = line.strip().split()
        class_id = int(parts[0])
        x_center = float(parts[1])
        y_center = float(parts[2])
        width = float(parts[3])
        height = float(parts[4])

        # 根据YOLO标签信息绘制边界框
        # 计算边界框的左上角和右下角坐标
        x1 = int((x_center - width / 2) * image.shape[1])
        y1 = int((y_center - height / 2) * image.shape[0])
        x2 = int((x_center + width / 2) * image.shape[1])
        y2 = int((y_center + height / 2) * image.shape[0])

        if class_id == 13:
            # 绘制边界框
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # 标识类别信息
            class_name = f'Class {class_id}'
            cv2.putText(image, class_name, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # 显示图像
            # cv2.imshow('Image with Bounding Boxes', image)
            cv2.imwrite(os.path.join(save_dir, image_file), image)
            # cv2.waitKey(0)

# 关闭所有窗口
# cv2.destroyAllWindows()
