import socket
#msgClient="message du client au serveur"
#byteToSend=msgClient.encode('utf-8')
ServerAdress=('10.10.42.231', 2222)
bufferSize=1024
UDPClient=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#UDPClient.sendto(byteToSend, ServerAdress)
while True :
    cmd=input('vouler incrémenter ou décrémenter le compteur ? INC/DEC \n')
    cmd=cmd.encode('utf-8')
    UDPClient.sendto(cmd, ServerAdress)
    data, address=UDPClient.recvfrom(bufferSize)
    data=data.decode('utf-8')
    print('Données du serveur', data)
    print('adresse IP du serveur', address[0])
    print('adresse port serveur', address[1])