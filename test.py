# import cv2
from ultralytics import YOLO
import torch
# import time
print(torch.cuda.is_available())
model = YOLO("./best_8n.pt")
model.predict("asset/1724539918.mp4", save=True, device="0")