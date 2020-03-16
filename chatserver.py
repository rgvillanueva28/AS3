"""
File: doctorserver.py
Server for providing non-directive psychotherapy.
Uses client handlers to handle clients' requests.
"""
#Edited to be chatserver.py

from socket import *
from chatclienthandler import ChatClientHandler
from codecs import decode

HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)
CODE = "ascii"
BUFSIZE = 1024

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

# The server now just waits for connections from clients
# and hands sockets off to client handlers
while True:
    print("Waiting for connection . . .")
    client, address = server.accept()
    print("... connected from: ", address)
    handler = ChatClientHandler(client)
    handler.start()
    client.send(bytes("Welcome to my chat room!", CODE))