import os
import ultralytics
from ultralytics import YOLO




class IA_detect_poussin():

    def __init__(self):
        self.HOME = os.getcwd()
        self.model=YOLO(f'{self.HOME}/../yolov8n.pt')
    
    def predict_image(self, file_name):
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, file_name)
        self.model.predict(abs_file_path, save=True, imgsz=800, conf=0.25)
