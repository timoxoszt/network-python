from socket import *
serverName = "localhost"
serverPort = 12001
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input("Input lowercase sentence:")
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage = clientSocket.recvfrom(2048).decode()
print(modifiedMessage)
clientSocket.close()
