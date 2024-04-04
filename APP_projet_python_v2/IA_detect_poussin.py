import os
import ultralytics
from ultralytics import YOLO
import shutil
from demarage_client import recoit_image_serveur




class IA_detect_poussin():

    def __init__(self):
        self.HOME = os.getcwd()
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, 'yolov8_poussin.pt') #On vient charger le modéle d'IA entrainner à l'avance
        self.model=YOLO(abs_file_path)
    
    def predict_image(self, file_name):
        #On vient demander au serveur de nous envoyer la toute derniere image prise par la camera
        recoit_image_serveur()
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, 'images\\'+file_name)
        #La partie suivante est mise entre try et except. Cela est du au fait que le protole de transfere d'image peux parfoit donner des images
        #incomplete qui ne sont pas exploitable par l'IA. Pour ce prémunir de tout probleme, on demande à l'IA de détruire le dossier de
        #prediction (quel créera même si l'image ne donne aucun résultat) pour éviter tout probleme lors de la prochaine prédiction de l'IA
        try :
            #Code de yoloV8 pour effectuer une prédiction sur une image :
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

