"""
File: doctorclienthandler.py
Client handler for providing non-directive psychotherapy.
"""
#modified to chatclienthandler.py

from codecs import decode
from threading import Thread
from doctor import Doctor

BUFSIZE = 1024
CODE = "ascii"

class ChatClientHandler(Thread):
    """Handles a session between a doctor and a patient."""
    #Handles session between server and client
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
        self.dr = Doctor()
   
    def run(self):
        self.client.send(bytes(self.dr.greeting(),
                               CODE))
        while True:
            message = decode(self.client.recv(BUFSIZE),
                             CODE)
            if not message:
                print("Client disconnected")
                self.client.close()
                break
            else:
                self.client.send(bytes(self.dr.reply(message),
                                       CODE))


