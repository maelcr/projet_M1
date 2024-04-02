import os
import ultralytics
from ultralytics import YOLO
import shutil
from OptimizedClient import recoit_image_serveur




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
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, 'yolov8_poussin.pt')
        self.model=YOLO(abs_file_path)
    
    def predict_image(self, file_name):
        recoit_image_serveur()
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, 'images\\'+file_name)
        try :
            self.model.predict(abs_file_path, save=True, imgsz=800, conf=0.2, show_labels=False, show_conf=False)


            path='..\\runs\\detect\\predict\\'+file_name
            abs_file_path_2 = os.path.join(script_dir, path)
            abs_file_path_3 = os.path.join(script_dir, 'images\\'+file_name[:-4]+'_pred.jpg')
            shutil.copyfile(abs_file_path_2 , abs_file_path_3)

            path2='..\\runs\\detect\\predict'
            abs_file_path_4 = os.path.join(script_dir, path2)
            shutil.rmtree(abs_file_path_4)
        except :
            path2='..\\runs\\detect\\predict'
            abs_file_path_4 = os.path.join(script_dir, path2)
            shutil.rmtree(abs_file_path_4)

