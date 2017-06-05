#!usr/bin/env python

from socket import *

class ChatServer():
    def __init__(self, host, port, bufsiz):
        self.HOST = host
        self.PORT = port
        self.BUFSIZ = bufsiz
        self.ADDR = (host, port)

        self.chatServSock = socket(AF_INET, SOCK_STREAM)
        self.chatServSock.bind(self.ADDR)

    def run(self):
        self.chatServSock.listen(1) # num can be passed to __init__

        while True:
            print "Waiting for connection..."
            self.chatCliSock, self.cliAddr = self.chatServSock.accept()
            self.chatCliSock.send('Connection established. Now we can chat!')

            print "Connected to:", self.cliAddr

            while True:
                msg = self.chatCliSock.recv(self.BUFSIZ)

                if msg == 'quit()':
                    print "Client left the chat.\n"
                    break
                
                print "Client:", msg

                msg = ""
                while msg == "":
                    msg = raw_input("-|-> ")

                if msg == 'quit()':
                    self.chatCliSock.send(msg)
                    break
                    
                self.chatCliSock.send(msg)
        self.chatServSock.close() #not really used

if __name__ == '__main__':
    chatServer = ChatServer('', 33000, 1024)
    chatServer.run()
    
