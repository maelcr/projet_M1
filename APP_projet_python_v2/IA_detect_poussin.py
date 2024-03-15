import os
import ultralytics
from ultralytics import YOLO




class IA_detect_poussin():

    def __init__(self):
        self.HOME = os.getcwd()
        #mettre vrais chemins
        #from ultralytics import YOLO

        # Load a model
        #model = YOLO('yolov8n.pt')  # load an official model
        #model = YOLO('path/to/best.pt')  # load a custom trained model

        # Export the model
        #model.export(format='onnx')
        self.model=YOLO(f'{self.HOME}/../yolov8n.pt')
    
    def predict_image(self, file_name):
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, file_name)
        self.model.predict(abs_file_path, save=True, imgsz=800, conf=0.25)
