from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("Server dang san sang lang nghe!!!")
while 1:
     connectionSocket, addr = serverSocket.accept()
     print ("Da ket noi voi client")
     sentence = connectionSocket.recv(1024).decode()
     if sentence=='f1301':
          capitalizedSentence = 'F1301{v3ry_gut_TCP_connect}'
     else:
          capitalizedSentence = sentence.upper()
     connectionSocket.send(capitalizedSentence.encode())
     connectionSocket.close()
