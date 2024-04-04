import customtkinter
import tkinter.messagebox
from tkinter import *
import os
import platform   
import subprocess
from PIL import ImageTk, Image  
import subprocess
import time
from lire_fichier import lire_fichier_txt
from ecrire_fichier import ecrire_fichier_txt
from IA_detect_poussin import IA_detect_poussin
from client_temperature import recoit_temperature_serveur

home= os.getcwd()
instance_ia=IA_detect_poussin()

#instance_ia.predict_image('poussin1.jpg')

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# démarons la class principale
class App(customtkinter.CTk):
    # la class de graphisme
    def __init__(self):
        super().__init__()
        self.real_home = home.replace('\\', '/')
        
        

        #gérer la fenêtre
        self.title("Projet S8") #titre
        self.geometry("800x950") #taille de la fenêtre
        self.check_var = tkinter.StringVar(value="on") #créer des variables qui sont des sortes de conteneur 
        self.check_chauffage_var = tkinter.StringVar(value="on") 
        self.check_ouvert_var = tkinter.StringVar(value="on")

        #titre
        self.label = customtkinter.CTkLabel(master = self ,text="Projet S8") #créer le titre
        self.label.pack(pady=12, padx=10) #affiche le titre

        # ----- initialisation des variables de départ -----
        
        self.degree_variable = tkinter.StringVar(value=lire_fichier_txt("save/degree.txt")) # On initialise les variables comme des conteneur,
        self.detection_cam_variable = tkinter.StringVar(value= self.ping("google.fr")) #  un peut comme précédemment
        self.etat_enclot_variable = tkinter.StringVar(value=self.check_etat_enclot())
        self.mort_variable = tkinter.StringVar(value=lire_fichier_txt("save/death_note.txt"))
        self.dangerosite_degree = tkinter.StringVar(value=self.temperature_dangerosite())
        

        #  ----- le tabview -----
        self.tabview = customtkinter.CTkTabview(self,width=900,height=700) # créer le cadre intérieur de l'application, le sorte de cube en arrière plan gris
        self.tabview.pack(pady=10) # affiche ce cadre
        self.tab_cam = self.tabview.add("Camera_1") #créer des tab, pour trier ce qui est affiché
        self.tab_notif = self.tabview.add("Notification")
        self.tab_info = self.tabview.add("Information")
        self.tab_temps_reel = self.tabview.add("temp réel")
        
        # ----- tab de la camera -----
        
        #bouton d'actualisation des variable
        self.bouton_degree = customtkinter.CTkButton(self.tab_cam,text="actualisation",command=self.reinit_variable)#création d'un bouton avec CTkButton
        self.bouton_degree.pack(pady=0)#affichage de ce bouton avec .pack

        #affichage caméra connecté
        self.label_titre1 = customtkinter.CTkLabel(self.tab_cam,text= "CAMERA connecté? :")#création d'une ligne de texte avec CTkLabel
        self.label_titre1.pack(pady=0)# affichage de ce texte
        self.connecte_label = customtkinter.CTkLabel( self.tab_cam, textvariable=self.detection_cam_variable)#idem mais avec la variable detection_cam_variable en tant que texte
        self.connecte_label.pack(pady=0)#affichage

        #affichage etat enclot
        self.connecte_titre = customtkinter.CTkLabel(self.tab_cam,text= "Etat:")#création d'une ligne de texte avec CTkLabel
        self.connecte_titre.pack(pady=0)# affichage de ce texte
        self.connecte_label = customtkinter.CTkLabel( self.tab_cam, textvariable=self.etat_enclot_variable)#idem mais avec la variable detection_cam_variable en tant que texte
        self.connecte_label.pack(pady=0)# affichage de ce texte

        #affichage nb mort
        self.mort_titre = customtkinter.CTkLabel(self.tab_cam,text= "mort détecté:")#création d'une ligne de texte avec CTkLabel
        self.mort_titre.pack(pady=0)# affichage de ce texte
        self.mort_label = customtkinter.CTkLabel( self.tab_cam, textvariable=self.mort_variable)#idem mais avec la variable detection_cam_variable en tant que texte
        self.mort_label.pack(pady=0)# affichage de ce texte

        #affichage degrée enclot
        self.degree_titre = customtkinter.CTkLabel(self.tab_cam,text= "degree dans l'enclot:")#création d'une ligne de texte avec CTkLabel
        self.degree_titre.pack(pady=0)# affichage de ce texte
        self.degree_label = customtkinter.CTkLabel( self.tab_cam, textvariable=self.degree_variable)#idem mais avec la variable detection_cam_variable en tant que texte
        self.degree_label.pack(pady=0)# affichage de ce texte

        #degrée enclot dangerosité
        self.degree_dangerosite_titre = customtkinter.CTkLabel(self.tab_cam,text= "dangerosité temperature : ")#création d'une ligne de texte avec CTkLabel
        self.degree_dangerosite_titre.pack(pady=0)# affichage de ce texte
        self.degree_dangerosite_label = customtkinter.CTkLabel( self.tab_cam, textvariable=self.dangerosite_degree)#idem mais avec la variable detection_cam_variable en tant que texte
        self.degree_dangerosite_label.pack(pady=0)# affichage de ce texte

        #chauffage présent ou non
        #création du checkbox avec CTkCheckbox, qui va avoir deux états, 1 et 0, 1 quand il est checked, 0 quand il ne l'es pas.
        self.checkbox_chauffage_present = customtkinter.CTkCheckBox(self.tab_cam,text="chauffage present.",command=self.checkbox_chauffage_ecriture_present, variable=self.check_chauffage_var,onvalue="on",offvalue="off")
        self.checkbox_chauffage_present.pack(pady=5,padx=10)#affichage du checkbox
        self.checkbox_chauffage_apply("save/chauffage_activation.txt") #appelle une fonction qui va enregistrer l'état de la checkbox dans un fichier de sauveguarde.
        
        #enclot ouvert ou non
        #création du checkbox avec CTkCheckbox, qui va avoir deux états, 1 et 0, 1 quand il est checked, 0 quand il ne l'es pas.
        self.checkbox_enclot_ouvert = customtkinter.CTkCheckBox(self.tab_cam,text="enclot ouvert ou non",command=self.checkbox_enclot_ouvert_ecriture, variable=self.check_ouvert_var,onvalue="on",offvalue="off")
        self.checkbox_enclot_ouvert.pack(pady=5,padx=10)#affichage du checkbox
        self.checkbox_ouvert_apply("save/enclot_ouvert.txt")#appelle une fonction qui va enregistrer l'état de la checkbox dans un fichier de sauveguarde.
        
        #bouton vue
         #création d'un bouton avec CTkButton, qui va apeller une fonction "command" quand elle seras appuyée
        self.bouton = customtkinter.CTkButton(self.tab_cam,text="vue",command=self.reponse_vue)#dans ce cas, elle apelle self.reponse_vue (même si c'est une fonction, ne pas mettre de () à la fin)
        self.bouton.pack(pady=15)#affichage

        #affichage de l'enclot
        script_dir = os.path.dirname(__file__)#demande à l'ordinateur le filepath brut du fichier
        abs_file_path = os.path.join(script_dir, 'images\\enclot.jpg')#crée le filepath brut de l'image
        self.image_enclot1 = Image.open(abs_file_path)# ouvre l'image du filepath
        self.image_enclot2= ImageTk.PhotoImage(self.image_enclot1.resize((200,150))) #créer la variable qui stoque l'image avec la taille de celle cis
        self.enclot = customtkinter.CTkLabel(self.tab_cam, text="", image=self.image_enclot2) # création de l'image avec ce qui as été stoqué
        self.enclot.pack(pady=10) #affichage de l'image

        
        
        # ----- tab des notif -----

        #notification chauffage
        #création du checkbox avec CTkCheckbox, qui va avoir deux états, 1 et 0, 1 quand il est checked, 0 quand il ne l'es pas.
        self.checkbox_chauffage = customtkinter.CTkCheckBox(self.tab_notif,text="chauffage",command=self.checkbox_chauffage_ecriture, variable=self.check_var,onvalue="on",offvalue="off")
        self.checkbox_chauffage.pack(pady=12,padx=10)#affichage checkbox
        self.checkbox_apply("save/sauveguarde_checkbox_chauffage.txt")#appelle une fonction qui va enregistrer l'état de la checkbox dans un fichier de sauveguarde.

        #script_dir = os.path.dirname(__file__)#demande à l'ordinateur le filepath brut du fichier
        abs_file_path1 = os.path.join(script_dir, 'img_save\\enclot.jpg')#crée le filepath brut de l'image
        self.image_derniere_RGB1 = Image.open(abs_file_path1)# ouvre l'image du filepath
        self.image__derniere_RGB2= ImageTk.PhotoImage(self.image_derniere_RGB1.resize((200,150)))#créer la variable qui stoque l'image avec la taille de celle cis
        self.enclot_RGB = customtkinter.CTkLabel(self.tab_notif, text="", image=self.image__derniere_RGB2)# création de l'image avec ce qui as été stoqué
        self.enclot_RGB.pack(pady=10) #affiche image

        #script_dir = os.path.dirname(__file__)#demande à l'ordinateur le filepath brut du fichier
        abs_file_path2 = os.path.join(script_dir, 'img_save\\enclot_therm.jpg')#crée le filepath brut de l'image
        self.image_thermique1 = Image.open(abs_file_path2)# ouvre l'image du filepath
        self.image_thermique2= ImageTk.PhotoImage(self.image_thermique1.resize((200,150)))#créer la variable qui stoque l'image avec la taille de celle cis
        self.enclot_thermique = customtkinter.CTkLabel(self.tab_notif, text="", image=self.image_thermique2)# création de l'image avec ce qui as été stoqué
        self.enclot_thermique.pack(pady=10) #affiche image


        

        # ----- tab information -----

        #image isen
        abs_file_path = os.path.join(script_dir, 'images/isen.png')#crée le filepath brut de l'image
        self.logo_isen = Image.open(abs_file_path)# ouvre l'image du filepath
        self.image_isen = ImageTk.PhotoImage(self.logo_isen.resize((200,150)))#créer la variable qui stoque l'image avec la taille de celle cis
        self.le_label = customtkinter.CTkLabel(self.tab_info, text="", image=self.image_isen)# création de l'image avec ce qui as été stoqué
        self.le_label.pack(pady=10)#affiche image

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.tab_info)#création d'un textbox avec CTkTextbox (un stoquage de txt scrollable)
        self.textbox.configure(state = NORMAL) #on démare l'écriture
        self.textbox.insert('end','tesg \n retour a la ligne \n trop bi1') #le texte qu'il y as dans le document, ( \n sert à passer une ligne )
        self.textbox.configure(state=DISABLED) #on stop l'écriture
        self.textbox.pack(pady=30, padx=20) #affichage textbox

        
        

        # ----- tab temps réel -----

        #nous réaffichons les différentes images de l'enclot dans un nouveau tab
        self.enclot_temp = customtkinter.CTkLabel(self.tab_temps_reel, text="", image=self.image_enclot2)# création de l'image avec ce qui as été stoqué
        self.enclot_temp.pack(pady=10) #affiche l'image

        self.enclot_RGB_temp = customtkinter.CTkLabel(self.tab_temps_reel, text="", image=self.image__derniere_RGB2)# création de l'image avec ce qui as été stoqué
        self.enclot_RGB_temp.pack(pady=10)#affiche l'image

        self.enclot_thermique_temp = customtkinter.CTkLabel(self.tab_temps_reel, text="", image=self.image_thermique2)# création de l'image avec ce qui as été stoqué
        self.enclot_thermique_temp.pack(pady=10)#affiche l'image
        
        self.update_label() #apelle la fonction update_label, qui va actualiser les variables et photos toutes les secondes.

        

        
    #Fonction permettant de rafraichir l'affichage et d'apeller d'autres fonctions toutes les n temps.
    #elle rafraichit aussi l'heure, juste une indication si l'aplication à freeze ou non.
    def update_label(self):
        now = time.strftime("%H:%M:%S") #récupère l'heure actuelle
        self.label.configure(text=now) #actualise la valeur qui stoque l'heure
        self.reinit_variable() #apelle reinit_variable
        self.after(1000, self.update_label) #rapelle la fonction toute les n fonctions

    #va détecter et retourner le résultat d'une comparaison de température, par raport aux paramètres  donnée à l'appel de la fonction
    #les paramètres minimum sont degree1 et maximum sont degree2
    def test_check_degree(self,degree1,degree2):
        value_degree = lire_fichier_txt("save/degree.txt")#lis le contenus de degree.txt qui contient la température de l'enclot
        if (value_degree <= degree1): #si la température est plus basse que degree1, alors
            return "temperature trop basse" #retourne en résultat "temperature trop basse"
        elif (value_degree >= degree2): #si la température est plus haute que degree2, alors
            return "temperature trop haute" #retourne en résultat "temperature trop haute"
        else: #si température est entre degree1 et degree 2, alors
            return "bonne temperature" #retourne "bonne temperature"


    #va apeller 
        
        
    def temperature_dangerosite(self):
            value_chauffage = lire_fichier_txt("save/chauffage_activation.txt") #lis l'état enregistrée du checkbox chauffage_activation
            value_ouvert = lire_fichier_txt("save/enclot_ouvert.txt") #lis l'état enregistrée du checkbox enclot_ouvert
            if (value_chauffage=="0" and value_ouvert=="0"): #va apeller test_check_degree() avec différents paramètres en fonction des checkbox.
                value_final = self.test_check_degree("20","30")
            elif (value_chauffage=="1" and value_ouvert=="0"):
                value_final = self.test_check_degree("25","30")
            else:
                value_final = "fenetre ouverte"
            
            
            return value_final #retourne la valeur char donnée par test_check_chauffage

    #détecte si le ckeckbox à été touché et lis sa value, puis enregistre le changement, je ne peut pas plus l'optimiser sinon beug
    def checkbox_chauffage_ecriture(self):
        if (self.check_var.get() == "on"): 
            ecrire_fichier_txt("save/sauveguarde_checkbox_chauffage.txt","1")
        elif (self.check_var.get() == "off"):
            ecrire_fichier_txt("save/sauveguarde_checkbox_chauffage.txt","0")

    def checkbox_chauffage_ecriture_present(self):
        if (self.check_chauffage_var.get() == "on"):
            ecrire_fichier_txt("save/chauffage_activation.txt","1")
        elif (self.check_chauffage_var.get() == "off"):
            ecrire_fichier_txt("save/chauffage_activation.txt","0")

    def checkbox_enclot_ouvert_ecriture(self):
        if (self.check_ouvert_var.get() == "on"):
            ecrire_fichier_txt("save/enclot_ouvert.txt","1")
        elif (self.check_ouvert_var.get() == "off"):
            ecrire_fichier_txt("save/enclot_ouvert.txt","0")
    

    #initialise les checkbox par raport aux sauveguardes lors du démarage de l'application
    def checkbox_apply(self, mon_fichier):
        value_checkbox = lire_fichier_txt(mon_fichier)
        if (value_checkbox == "0"):
            self.checkbox_chauffage.deselect()
        elif (value_checkbox == "1"):
            self.checkbox_chauffage.select()

    def checkbox_chauffage_apply(self, mon_fichier):
        value_checkbox = lire_fichier_txt(mon_fichier)
        if (value_checkbox == "0"):
            self.checkbox_chauffage_present.deselect()
        elif (value_checkbox == "1"):
            self.checkbox_chauffage_present.select()

    def checkbox_ouvert_apply(self, mon_fichier):
        value_checkbox = lire_fichier_txt(mon_fichier)
        if (value_checkbox == "0"):
            self.checkbox_enclot_ouvert.deselect()
        elif (value_checkbox == "1"):
            self.checkbox_enclot_ouvert.select()

    
    #permet de réinitialiser les variables affiché
    #et d'apeller l'IA et d'autres programmes
    def reinit_variable(self):

        recoit_temperature_serveur()
        #degree_enclot
        # va permettre de lire le fichier degree.txt, stoquant la température de l'enclot, et l'afficher
        i = lire_fichier_txt("save/degree.txt") + " degrée" #apelle lire_fichier_txt qui retourneras la valeurs inscrite dans le fichier degree.txt
        self.degree_variable.set(i) #va actualiser la variable degree_variable, qui va servir d'affichage

        #connection cam
        # va pinger l'adresse (par exemple google.fr) et reguarde si il y as un retour de ping, si oui alors la ou amène l'adresse est connecté
        #si il ne reçoit pas de retour de ping, alors il n'y as pas de connection.
        j = self.ping("google.fr") # apelle le programme ping() qui envoit le ping à l'adresse et enregistre la réponse
        self.detection_cam_variable.set(j) #va actualiser la variable detection_cam_variable, servant pour l'affichage

        #etat enclot
        #va apeller le programme check_etat_enclot() et changer la variable etat_enclot_variable pour l'affichage.
        #se référer a la description du programme apellé pour plus de détail
        self.etat_enclot_variable.set(self.check_etat_enclot())

        #dangerosite temperature
        #va apeller le programme temperature_dangerosite() et changer la variable dangerosite_degree pour l'affichage, 
        #se référer a la description du programme apellé pour plus de détail
        self.dangerosite_degree.set(self.temperature_dangerosite())

        #affichage nb morts détecté
        #va apeller le programme lire_fichier_txt() pour lire ce que contient death_note,
        #ce fichier stoque le nombre de mort détecté par l'IA.
        #il va ensuite actualiser la variable pour l'affichage en continue
        self.mort_variable.set(lire_fichier_txt("save/death_note.txt") )

        #détruit l'image enclot affiché
        self.enclot.destroy()
        self.enclot_temp.destroy()

        if(int(self.mort_variable.get())>0):
            instance_ia.predict_image('poussin1.jpg')
            self.change_dernier_image()
        else:
            self.enclot_RGB.destroy()
            self.enclot_thermique.destroy()

            
    
    def change_dernier_image (self):
        self.enclot_RGB.destroy()
        self.enclot_thermique.destroy()
        self.enclot_RGB_temp.destroy()
        self.enclot_thermique_temp.destroy()

        script_dir = os.path.dirname(__file__)
        abs_file_path1 = os.path.join(script_dir, 'images\\poussin1.jpg')
        try:
            self.image_derniere_RGB1 = Image.open(abs_file_path1)
            self.image__derniere_RGB2= ImageTk.PhotoImage(self.image_derniere_RGB1.resize((450,370)))
            self.enclot_RGB = customtkinter.CTkLabel(self.tab_notif, text="", image=self.image__derniere_RGB2)
            self.enclot_RGB.pack(pady=10)
            self.enclot_RGB_temp = customtkinter.CTkLabel(self.tab_notif, text="", image=self.image__derniere_RGB2)
            self.enclot_RGB_temp.pack(pady=10)
        
        except :
            print("probleme transfer image")
        

        
        abs_file_path2 = os.path.join(script_dir, 'images\\poussin1_pred.jpg')
        try:
            self.image_thermique1 = Image.open(abs_file_path2)
            self.image_thermique2= ImageTk.PhotoImage(self.image_thermique1.resize((450,370)))
            self.enclot_thermique = customtkinter.CTkLabel(self.tab_notif, text="", image=self.image_thermique2)
            self.enclot_thermique.pack(pady=10)
        
        except:
            print("probleme transfer image")

        try : 
            self.enclot_RGB_temp = customtkinter.CTkLabel(self.tab_temps_reel, text="", image=self.image__derniere_RGB2)
            self.enclot_RGB_temp.pack(pady=10)

            self.enclot_thermique_temp = customtkinter.CTkLabel(self.tab_temps_reel, text="", image=self.image_thermique2)
            self.enclot_thermique_temp.pack(pady=10)
        except : 
            print("probleme transfer image")
            
    

    #lis le fichier etat_de_lenclot.txt et retourne l'état de l'enclot
    #l'état de l'enclot varie selon le chiffre retrouvé dans le fichier.
    #si 0, le programme retourneras "rien à signaler"
    #si 1, il retourneras "morts détecté"
    #si 2, il retourneras "anomalie détecté"
    def check_etat_enclot(self):
        etat = lire_fichier_txt("save/etat_de_lenclot.txt") #lis le fichier et sauveguarde la valeur
        if (etat == "0"):#si la valeur est "0"
            resultat = "rien à signaler"
        elif (etat == "1"): #si la valeur est "1"
            resultat = "morts détecté"
        elif (etat ==  "2"): #si la valeur est "2"
            resultat = "anomalie détecté"
        return resultat #donner le résultat
    
    #programme apellé par un bouton, va réinitialiser les fichiers etat_de_lenclot.txt et death_note.txt en "O" et 
    #réinitialiser les variables etat_enclot_variable et mort_variable
    def reponse_vue(self):
        ecrire_fichier_txt("save/etat_de_lenclot.txt","0") #apelle la fonction ecrire_fichier_txt() pour changer en 0 la valeurs stoqué dans etat_de_lenclot.txt 
        self.etat_enclot_variable.set(self.check_etat_enclot()) #réinitialise la variable avec la nouvelle valeur
        ecrire_fichier_txt("save/death_note.txt","0") #apelle la fonction ecrire_fichier_txt() pour changer en 0 la valeurs stoqué dans death_note.txt 
        self.mort_variable.set(lire_fichier_txt("save/death_note.txt")) #réinitialise la variable avec la nouvelle valeur

    
    def ping(self,host):
        param = '-n' if platform.system().lower()=='windows' else '-c'

        command = ['ping', param, '1', host]
        value = "non connecté"
        
        if (subprocess.call(command) == 0):
            value = "connecté"
        #elif(subprocess.call(command) != 0):
        #    value = "non connecté"
        return value
    
        


#loop
if __name__ == "__main__":
    app = App()
    
    app.mainloop()
