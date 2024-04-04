import socket

def wait_for_acknowledge(client,reponse):
    """
    Ce code permet d'attendre les retours du serveur en fonction de ce qu'on s'attend à recevoir
    """
    donnee_recu = 0
    donnee_attendu= len(reponse)
    
    message = str()
    while donnee_recu < donnee_attendu:
        data = client.recv(16)
        donnee_recu+= len(data)
        message += data.decode("utf-8")
    return message


def recoit_image_serveur():
    #on essaye de se connecter sur le port ouver par le serveur
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect(('10.10.42.231', 2222))
    print(f"Client connecté au serveur")

    client.settimeout(5) 

    cmd=str(2).encode('utf-8')
    client.sendall(cmd)


    print("Le client attend maintenant la commande du serveur")
    cmd_from_server = wait_for_acknowledge(client,"debut transfer image")


    if cmd_from_server == "debut transfer image":
        print("commande recu du serveur : \"debut transfer image\"")
        print("ACK...")
        client.sendall(bytes("ACK","utf-8"))

    print(f"Le client s'apprête maintenant à recevoir l'image du serveur")


    file = f"APP_projet_python_V2\\images\\poussin1.jpg" #emplacement où on veux que soit sauvegarder l'image
    try: #On essaye de crée le fichier de l'image
        f = open(file, "x")           
        f.close()
    except:#si sa ne marche pas c'est que image déjà crée, on passe à la suite
        pass
    finally: #on vient remplacer ce qu'il y a sur le fichier par notre nouvelle image en provenance du serveur
        f = open(file, "wb")
    print(f"\treception de l'image")
    #très important : on veux savoir de quel taille sera l'image recu
    imgsize = int(wait_for_acknowledge(client,str(3)))
    print(f"\tune image de {imgsize}B vas être reçu par le client")
    print("ACK...")
    client.sendall(bytes("ACK","utf-8"))  
    buff = client.recv(imgsize)
    #On vient recevoir la capacité maximal de recv() puis on met les données dans l'image.
    #On fait sa jusqu'à être arriver au bout de l'image dont on connait déjà la taille 
    while buff :
        f.write(buff)
        buff = client.recv(imgsize)
    f.close()
    print(f"Image reçu !")

    print("Fermeture de la connection client/serveur")
    client.close()
