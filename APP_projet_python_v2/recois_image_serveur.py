import socket

UDPClient=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerAdress=('10.10.42.231', 2222)
UDPClient.connect(ServerAdress)
#bufferSize=1024
#UDPClient=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True :
    cmd=input('si vous voulez recevoir une image serveur, taper IMAGE \n')
    cmd=cmd.encode('utf-8')
    UDPClient.sendto(cmd, ServerAdress)
    if cmd=="IMAGE":
        file=open('image_serveur.jpg', 'wb')
        image_chunk=UDPClient.recv(2048)
        while image_chunk:
            file.write(image_chunk)
            image_chunk=UDPClient.recv(2048)

        file.closec