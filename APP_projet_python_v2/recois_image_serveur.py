"""import socket
from echange_UDP import donne_info_ip

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
IP_rasbery ="0.10.42.231"

donne_info_ip(IPAddr, IP_rasbery)

server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((IPAddr, 2222))
server.listen()

client_socket, client_adress=server.accept()

file=open('images/image_serveur.jpg', 'wb')
image_chunk=client_socket.recv(2048)

while image_chunk:
    file.write(image_chunk)
    image_chunk=client_socket.recv(2048)
file.close
client_socket.close


"""

import socket

UDPClient=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerAdress=('10.10.42.231', 2222)
UDPClient.connect(ServerAdress)
#bufferSize=1024
#UDPClient=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True :
    cmd_origin=input('si vous voulez recevoir une image serveur, taper IMAGE \n')
    cmd=cmd_origin.encode('utf-8')
    UDPClient.sendto(cmd, ServerAdress)
    if (cmd_origin=="IMAGE"):
        file=open('APP_projet_python_v2/images/image_serveur.jpg', 'wb')
        print("continu")
        image_chunk=UDPClient.recv(32768)
        print("continu")
        while image_chunk:
            file.write(image_chunk)
            if (len(image_chunk)<=32768):
               break
            image_chunk=UDPClient.recv(32768)
            print("continu_while")
            print(len(image_chunk))

        file.close
        print("reçu")
