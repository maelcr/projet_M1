import socket
from ecrire_fichier import ecrire_fichier_txt

def recoit_temperature_serveur():
    #initiate connection
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #server_addr = (socket.gethostname(), 2019)  #change here for sending to another machine in LAN 
    client.connect(('10.10.42.231', 2222))
    print(f"Connected to server!")

    client.settimeout(5) #limit each communication time to 5s

    cmd=str(1).encode('utf-8')
    client.sendall(cmd)
    
    data = client.recv(1024)
    temperature=data.decode("utf-8")
    print("temperature reçu !")
    ecrire_fichier_txt("save/degree.txt", str(temperature))
    client.close()
