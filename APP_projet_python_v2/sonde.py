import os
import random
from lire_fichier import lire_fichier_txt
from ecrire_fichier import ecrire_fichier_txt

class sonde():
    def __init__(self):
        self.temperature=0
        self.home =  os.getcwd()

    def tempo_change_save(self):
        #temporaire : à changer une fois connecter à vrais sonde
        self.temperature=30+round(random.uniform(-1, 1, 2))
        ecrire_fichier_txt("save/degree", self.temperature)

    