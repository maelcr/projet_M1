import socket
from ecrire_fichier import ecrire_fichier_txt

def recoit_temperature_serveur():
    #on essaye de se connecter sur le port ouver par le serveur
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect(('10.10.42.231', 2222))
    print(f"Connected to server!")

    client.settimeout(5) 

    cmd=str(1).encode('utf-8')
    client.sendall(cmd)
    
    #comme le message de la temperature est un texte relativement petit, on le reçoit juste et on le sauvegarde dans un fichier sans gros probleme
    data = client.recv(1024)
    temperature=data.decode("utf-8")
    print("temperature reçu !")
    ecrire_fichier_txt("save/degree.txt", str(temperature))
    client.close()
