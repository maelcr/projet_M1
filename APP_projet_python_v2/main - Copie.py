import customtkinter
import tkinter.messagebox
from tkinter import *
import os
import platform   
import subprocess
from PIL import ImageTk, Image  
import subprocess
import time

test = os.getcwd()

os.chdir(os.path.dirname(test))

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.Home =  os.getcwd()
        self.real_home = self.Home[:-1]
        

        #gérer la fenêtre
        self.title("Projet S8")
        self.geometry("400x650")
        self.check_var = tkinter.StringVar(value="on")

        #titre
        self.label = customtkinter.CTkLabel(master = self ,text="Projet S8")
        self.label.pack(pady=12, padx=10)

        # ----- initialisation des variables de départ -----
        
        self.degree_variable = tkinter.StringVar(value=self.lire_fichier_txt(self.real_home+"degree.txt"))
        self.detection_cam_variable = tkinter.StringVar(value= self.ping("google.fr"))
        self.etat_enclot_variable = tkinter.StringVar(value=self.check_etat_enclot())
        self.mort_variable = tkinter.StringVar(value=self.lire_fichier_txt(self.real_home+"death_note.txt"))
        

        #  ----- le tabview -----
        self.tabview = customtkinter.CTkTabview(self,width=500,height=500)
        self.tabview.pack(pady=10)
        self.tab_cam = self.tabview.add("Camera_1")
        self.tab_notif = self.tabview.add("Notification")
        self.tab_info = self.tabview.add("Information")
        
        # ----- tab de la camera -----
        

        #bouton d'actualisation des variable
        self.bouton_degree = customtkinter.CTkButton(self.tab_cam,text="actualisation",command=self.reinit_variable)
        self.bouton_degree.pack(pady=0)

        #affichage caméra connecté
        self.label_titre1 = customtkinter.CTkLabel(self.tab_cam,text= "CAMERA connecté? :")
        self.label_titre1.pack(pady=0)
        self.connecte_label = customtkinter.CTkLabel( self.tab_cam, textvariable=self.detection_cam_variable)
        self.connecte_label.pack(pady=0)

        #affichage etat enclot
        self.connecte_titre = customtkinter.CTkLabel(self.tab_cam,text= "Etat:")
        self.connecte_titre.pack(pady=0)
        self.connecte_label = customtkinter.CTkLabel( self.tab_cam, textvariable=self.etat_enclot_variable)
        self.connecte_label.pack(pady=0)

        #affichage nb mort
        self.mort_titre = customtkinter.CTkLabel(self.tab_cam,text= "mort détecté:")
        self.mort_titre.pack(pady=0)
        self.mort_label = customtkinter.CTkLabel( self.tab_cam, textvariable=self.mort_variable)
        self.mort_label.pack(pady=0)

        #affichage degrée enclot
        self.degree_titre = customtkinter.CTkLabel(self.tab_cam,text= "degree dans l'enclot:")
        self.degree_titre.pack(pady=0)
        self.degree_label = customtkinter.CTkLabel( self.tab_cam, textvariable=self.degree_variable)
        self.degree_label.pack(pady=0)

        #bouton vue
        self.bouton = customtkinter.CTkButton(self.tab_cam,text="vue",command=self.reponse_vue)
        self.bouton.pack(pady=15)

        #affichage de l'enclot
        self.image_enclot1 = Image.open(self.real_home+'/APP_projet_python/images/enclot.jpg')
        self.image_enclot2= ImageTk.PhotoImage(self.image_enclot1.resize((200,150)))
        self.enclot = customtkinter.CTkLabel(self.tab_cam, text="", image=self.image_enclot2)
        self.enclot.pack(pady=10)
        
        # ----- tab des notif -----

        #notif chauffage
        self.checkbox_chauffage = customtkinter.CTkCheckBox(self.tab_notif,text="chauffage",command=self.checkbox_chauffage_ecriture, variable=self.check_var,onvalue="on",offvalue="off")
        self.checkbox_chauffage.pack(pady=12,padx=10)
        self.checkbox_apply(self.real_home+"sauveguarde_checkbox_chauffage.txt")

        # ----- tab information -----

        #image isen
        self.test8695 = Image.open(self.real_home+'/APP_projet_python/images/isen.png')
        self.image_isen = ImageTk.PhotoImage(self.test8695.resize((200,150)))
        self.le_label = customtkinter.CTkLabel(self.tab_info, text="", image=self.image_isen)
        self.le_label.pack(pady=10)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.tab_info)
        self.textbox.configure(state = NORMAL)
        self.textbox.insert('end','tesg \n retour a la ligne \n trop bi1')
        self.textbox.configure(state=DISABLED)
        self.textbox.pack(pady=30, padx=20)

        
        self.update_label()
        

        
        
    def update_label(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.reinit_variable()
        self.after(1000, self.update_label)

    #détecte si le ckeckbox à été touché et lis sa value, puis enregistre le changement, je ne peut pas plus l'optimiser sinon beug
    def checkbox_chauffage_ecriture(self):
        if (self.lire_fichier_txt(self.real_home+"semaphore.txt") == "0"): #semaphore, pour éviter que plusieurs programmes utilisent le même dossier en même temps
            self.ecrire_fichier_txt(self.real_home+"semaphore.txt","1")    #et éviter les crash
            print("checkbox toggled, current value:", self.check_var.get()) 
            if (self.check_var.get() == "on"):
                self.ecrire_fichier_txt(self.real_home+"sauveguarde_checkbox_chauffage.txt","1")
            elif (self.check_var.get() == "off"):
                self.ecrire_fichier_txt(self.real_home+"sauveguarde_checkbox_chauffage.txt","0")
            self.ecrire_fichier_txt(self.real_home+"semaphore.txt","0")


    def checkbox_apply(self, mon_fichier):
        value_checkbox = self.lire_fichier_txt(mon_fichier)
        if (value_checkbox == "0"):
            self.checkbox_chauffage.deselect()
        elif (value_checkbox == "1"):
            self.checkbox_chauffage.select()

    
    #permet de réinitialiser les variables affiché
    #je n'aie pas réhussit à le faire en temps réel
    def reinit_variable(self):
        if (self.lire_fichier_txt(self.real_home+"semaphore.txt") == "0"):
            self.ecrire_fichier_txt(self.real_home+"semaphore.txt","1")
            #degree_enclot
            i = self.lire_fichier_txt(self.real_home+"degree.txt") + " degrée"
            self.degree_variable.set(i)

            #connection cam
            j = self.ping("google.fr")
            self.detection_cam_variable.set(j)

            #etat enclot
            self.etat_enclot_variable.set(self.check_etat_enclot())

            mort = self.lire_fichier_txt(self.real_home+"death_note.txt") 
            self.mort_variable.set(mort)

       
            self.enclot.destroy()

            self.image_enclot1 = Image.open(self.real_home+'/APP_projet_python/images/duck.jpg')
            self.image_enclot2= ImageTk.PhotoImage(self.image_enclot1.resize((200,150)))
            self.enclot = customtkinter.CTkLabel(self.tab_cam, text="", image=self.image_enclot2)
            self.enclot.pack(pady=10)
            self.ecrire_fichier_txt(self.real_home+"semaphore.txt","0")

        
    

    #lis le fichier etat_de_lenclot.txt et affiche l'état de l'enclot
    def check_etat_enclot(self):
        
        #etat enclot
        etat = self.lire_fichier_txt(self.real_home+"etat_de_lenclot.txt")
        if (etat == "0"):
            resultat = "rien à signaler"
        elif (etat == "1"):
            resultat = "morts détecté"

        elif (etat ==  "2"):
            resultat = "anomalie détecté"
        
        #elif (self.lire_fichier_txt(self.real_home+"semaphore.txt") == "1"):
        #    resultat = "semaphore utilisé"    
            
        return resultat
    
    #réinitialise dans le fichier l'état de l'enclot, et affiche dans l'application "rien à signaler"
    def reponse_vue(self):
        if (self.lire_fichier_txt(self.real_home+"semaphore.txt") == "0"):
            self.ecrire_fichier_txt(self.real_home+"semaphore.txt","1")
            self.ecrire_fichier_txt(self.real_home+"etat_de_lenclot.txt","0")
            self.etat_enclot_variable.set(self.check_etat_enclot())
            self.ecrire_fichier_txt(self.real_home+"semaphore.txt","0")

    #lire le fichié spécifiée
    def lire_fichier_txt (self,file_name):
        script_dir = os.path.dirname(__file__)  # Get the directory of the current script
        save_file_path = os.path.join(script_dir, 'save', file_name)  # Construct the file path
        with open(save_file_path, 'r') as file:
            content = file.read()
        return content
    
    #écrire le fichier spécifié avec le message en str
    def ecrire_fichier_txt (self,file_name,message):
        script_dir = os.path.dirname(__file__)  # Get the directory of the current script
        save_file_path = os.path.join(script_dir, 'save', file_name)  # Construct the file path
        with open(save_file_path, 'w') as file:
            content = file.write(message)
        return content
    
    
    def ping(self,host):
        #by Ratado
        param = '-n' if platform.system().lower()=='windows' else '-c'

        command = ['ping', param, '1', host]
        
        if (subprocess.call(command) == 0):
            value = "connecté"
        elif(subprocess.call(command) != 0):
            value = "non connecté"
        return value
    
        


#loop
if __name__ == "__main__":
    app = App()
    
    app.mainloop()




""""
def login():
    print("Test")

def ischeckboxchecked():
    print("checkbox toggled, current value:", check_var.get())  


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x350")
check_var = tkinter.StringVar(value="on")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="login System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2 = customtkinter.CTkEntry(master = frame, placeholder_text="password")
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame,text="login",command=ischeckboxchecked)
button.pack(pady=12,padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame,text="rememberme",command=ischeckboxchecked, variable=check_var,onvalue="on",offvalue="off")
checkbox.pack(pady=12,padx=10)

root.mainloop()
"""
"""
    #lire le fichié spécifiée
    def lire_fichier_txt (self,file_name):
        #save_file_path = os.path.join('save', file_name)
        save_file_path = "save/" + file_name
        with open(save_file_path, 'r') as file:
            i = file.read()
        return i
    
    #écrire le fichier spécifié avec le message en str
    def ecrire_fichier_txt (self,file_name,message):
        #save_file_path = os.path.join('save', file_name)
        save_file_path = "/save/" + file_name
        with open(save_file_path, 'w') as file:
            i = file.write(message)
    """