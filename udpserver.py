from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print ("The server is ready to receive")
while 1:
    message, clientAddress = serverSocket.recvfrom(1024).decode('utf_8')
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
