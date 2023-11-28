import cv2
import os
from PIL import Image
import numpy as np
# path = r"Image_20230831175205143.bmp"
folder_path = "./9.4空框"

# image = cv2.imread(path)
# 1500*1090
# 办公室数值
# x1, y1 = 490, 380
# x2, y2 = 1990, 1470
# 现场数值
# (500,460,2000,1550) -> x1,y1,x2,y2
x1, y1 = 500, 460
x2, y2 = 2000, 1550
print(x2-x1, y2-y1)
for file in os.listdir(folder_path):
    if file.endswith(".bmp"):
        image_file = file
        image = Image.open(os.path.join(folder_path, file))

        # image = cv2.imread(image_file)
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cropped_image = image[y1:y2, x1:x2]


        # window_size = (800, 800)
        # cv2.namedWindow('Cropped Image', cv2.WINDOW_NORMAL)  # 创建窗口并指定为可调整大小
        # cv2.resizeWindow('Cropped Image', window_size[0], window_size[1])  # 设置窗口大小


        cv2.imshow('Cropped Image', cropped_image)
        cv2.imwrite(image_file.split(".")[0] + '.jpg', cropped_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()