from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Hello, what your name:")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024).decode()
print ( "Hello:", modifiedSentence )
clientSocket.close()
