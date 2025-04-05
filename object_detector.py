import cv2
from ultralytics import YOLO
from transformers import CLIPProcessor, CLIPModel
from fiftyone import ViewField as F
from ultralytics import YOLO

def modelrun(video_path):
    model = YOLO('/mnt/D810F06910F0504C/cctv_model/test/yolov9/runs/detect/train5/weights/best.pt')
    results = model(video_path, save=True)  # Outputs annotated video
    print("model ran and video saved")
def pre():
    print("hello")