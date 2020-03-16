from codecs import decode
from threading import Thread
#from chatclient import Ui_MainWindow

BUFSIZE = 1024
CODE = "ascii"

class ChatClientHandler(Thread):
    """Handles a session between a doctor and a patient."""
    #Handles session between server and client
    def __init__(self, client, address):
        Thread.__init__(self)
        self.client = client
        self.address = address
        self.ls = []
        #self.dr = Doctor()
   
    def run(self):
        self.client.send(bytes("You have connected to the server!",
                               CODE))
        while True:
            message = decode(self.client.recv(BUFSIZE),
                             CODE)
            ls = "%s: %s" % (str(self.address[1]), message)
            if not message:
                self.client.send(bytes("Client %s disconnected" % str(self.address[1]),
                               CODE))
                print("Client %s disconnected" % str(self.address[1]))
                self.client.close()
                break
            else:
                self.client.send(bytes(ls, CODE))