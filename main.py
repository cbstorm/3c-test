import cv2
from ultralytics import YOLO
import time

model = YOLO("best_n.pt")

cap = cv2.VideoCapture('asset/output0.mp4')

COLORS = dict()
COLORS["white"] = (255, 255, 255)
COLORS["yellow"] = (255, 255, 0)
COLORS["red"] = (255, 0, 0)
COLORS["table"] = (0, 0, 255)

new_frame_time = 0
prev_frame_time = 0
while (True):
    ret, frame = cap.read()
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    fps = "{:.2f}".format(fps)
    # s = time.time() * 1000
    results = model.predict(frame, save=False, verbose=False)
    # e = (time.time() * 1000) - s
    # print(e)
    # print(results[0].boxes.xyxy)
    # print(results[0].boxes.cls)
    # print(results[0].names)
    for idx, c in enumerate(results[0].boxes.cls):
        label = results[0].names[int(c)]
        xy = results[0].boxes.xyxy[int(idx)]
        xmin, ymin, xmax, ymax = int(xy[0]), int(xy[1]), int(xy[2]), int(xy[3])
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), COLORS[label], 1)
        # print(label, xmin, ymin, xmax, ymax)

    cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX,
                2, (100, 255, 0), 3, cv2.LINE_AA)
    # break
    cv2.imshow('frame', frame)
    prev_frame_time = new_frame_time
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
