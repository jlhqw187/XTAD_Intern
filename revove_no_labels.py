import glob
import os
images_path = r"F:\xtad\debug_1103\job1"
labels_path = r"F:\xtad\debug_1103\job1_by"
images_list = os.listdir(images_path)

for img_path in images_list:
    label_path = img_path.replace(".jpg",".txt")
    if not os.path.exists(os.path.join(labels_path,label_path)):
        # print(img_path)

        os.remove(os.path.join(images_path,img_path))
        continue
    with open(os.path.join(labels_path,label_path), "r") as f:
        lines = f.read().splitlines()
        f.close()

        if len(lines) == 0:
            # print(img_path)
            # print(label_path)
            os.remove(os.path.join(images_path,img_path))
            os.remove(os.path.join(labels_path,label_path))
