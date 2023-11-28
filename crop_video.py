import cv2
input_path = r"Video_20230828110515238.avi"
output_path = "0828_light_off_noback.mp4"

x1, y1 = 560, 410
x2, y2 = 1900, 1450

cap = cv2.VideoCapture(input_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(fps, width, height)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter(output_path, fourcc, fps, (x2 - x1, y2 - y1))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cropped_frame = frame[y1 : y2, x1 : x2]
        writer.write(cropped_frame)

    else:
        break

cap.release()
writer.release()
print("finished!!!!!!!!!!!!!!!!!!!!!!!!!!!!")