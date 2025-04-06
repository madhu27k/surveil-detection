import cv2
from ultralytics import YOLO
from transformers import CLIPProcessor, CLIPModel
from fiftyone import ViewField as F
from ultralytics import YOLO
def modelrun(vidpath_1):
    model = YOLO('/mnt/D810F06910F0504C/cctv_model/test/runs/detect/train4/weights/best.pt')
    results = model(vidpath_1, save=True)  # Outputs annotated video

modelrun('/home/engimo/Downloads/youtube_xm5YYY-4Dp8_720x1280_h264.mp4')

#python train.py --img 640 --batch 16 --epochs 50 --data /mnt/D810F06910F0504C/cctv_model/test/yolov9/Surveillance.v3-new_version.yolov9/data.yaml --weights yolov9c.pt --cache
#python train.py --workers 8 --device 0 --batch 32 --data /mnt/D810F06910F0504C/cctv_model/test/yolov9/Surveillance.v3-new_version.yolov9/data.yaml --img 640 --cfg /mnt/D810F06910F0504C/cctv_model/test/yolov9/models/detect/gelan-c.yaml --weights '' --name gelan-c-det --hyp /mnt/D810F06910F0504C/cctv_model/test/yolov9/data/hyps/hyp.scratch-high.yaml --min-items 0 --epochs 300 --close-mosaic 10
#python train.py --img 640 --batch 16 --epochs 50 --data Surveillance.v3-new_version.yolov5pytorch/data.yaml --weights yolov5s.pt --cache
#python train.py --img 640 --batch 16 --epochs 50 --data /mnt/D810F06910F0504C/cctv_model/test/Surveillance.v3-new_version.yolov9/data.yaml --weights yolov5s.pt
#python train.py --cfg /mnt/D810F06910F0504C/cctv_model/test/lib/python3.13/site-packages/ultralytics/cfg/models/v9/yolov9c.yaml --data /mnt/D810F06910F0504C/cctv_model/test/lib/python3.13/site-packages/ultralytics/cfg/datasets/coco.yaml
#python train.py --workers 8 --device 0 --batch 32 --data /mnt/D810F06910F0504C/cctv_model/test/yolov9/Surveillance.v3-new_version.yolov9/data.yaml --img 640 --cfg /mnt/D810F06910F0504C/cctv_model/test/yolov9/models/detect/gelan-c.yaml --weights '' --name gelan-c-det --hyp /mnt/D810F06910F0504C/cctv_model/test/yolov9/data/hyps/hyp.scratch-high.yaml --min-items 0 --epochs 300 --close-mosaic 10
#python train.py --cfg /mnt/D810F06910F0504C/cctv_model/test/lib/python3.13/site-packages/ultralytics/cfg/models/v9/yolov9c.yaml --data /mnt/D810F06910F0504C/cctv_model/test/yolov9/Surveillance.v3-new_version.yolov9/data.yaml


#python train.py --weights yolov9-c.pt --data /mnt/D810F06910F0504C/cctv_model/test/yolov9/data.yaml --hyp /mnt/D810F06910F0504C/cctv_model/test/yolov9/runs/train/gelan-c-det10/hyp.yaml --epochs 100 --batch-size 2 --imgsz 640

#wanna fucking kill the person who wrote that train.py script
#I'm better off with yolo command than this vague ass script

#yolo task=detect mode=train epochs=100 data="/mnt/D810F06910F0504C/cctv_model/test/weapon detection.v7-personnweapongreygenx2v2.yolov9/data.yaml" model=yolov9c.pt imgsz=640 batch=4