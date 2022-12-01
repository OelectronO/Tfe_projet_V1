
#----- A simple TCP client program in Python using send() function -----

import socket

 

# Create a client socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 

# Connect to the server

clientSocket.connect(("192.168.1.29",5456))

 

# Send data to server

truc1 = 14
player_name = "Mathys"

data = player_name+" "+str(truc1)

clientSocket.send(data.encode())

 

# Receive data from server

dataFromServer = clientSocket.recv(1024)
print(dataFromServer.decode())

 

# Print to the console
