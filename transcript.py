#transcript.py

class Transcript:
    chats = []

    def __init__(self, address, chatsss):
        self.address = address
        self.chats.append([self.address, chatsss])
        
    def __str__(self):
        return self.address + "\n"
        return self.chats + "\n"

    def getAddress(self):
        return self.address

    def addChat(self, message):
        self.chats.append(message)

    def getChats(self):
        return self.chats