import os
from lire_fichier import lire_fichier_txt
from ecrire_fichier import ecrire_fichier_txt
import shutil

class update_image():

    def __init__(self):
        self.nb_image=1
        self.home =  os.getcwd()

    def change_image(self):
        #temporaire, à changer une fois qu'on a un vrais flux vidéo

        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, 'images\\duck.jpg')
        os.remove(abs_file_path) 

        path='images\\reserve_duck\\Image'+str(self.nb_image)+'.jpg'
        abs_file_path_2 = os.path.join(script_dir, path)
        shutil.copyfile(abs_file_path_2 , abs_file_path)

        self.nb_image+=1
        if(self.nb_image==7):
            self.nb_image=1




