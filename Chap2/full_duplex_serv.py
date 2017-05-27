#!/usr/bin/env python

import select, sys
from socket import *
from half_duplex_chat_serv import ChatServer

class FDChatServer(ChatServer):
    def __init__(self, host, port, bufsiz):
        ChatServer.__init__(self, host, port, bufsiz)
        #self.chatServSock.setblocking(0)

    def run(self):
        self.chatServSock.listen(1)
        while 1:
            self.inputs = [sys.stdin]
            self.outputs = []
            
            print "Waiting for connection..."
            self.chatCliSock, client_address = self.chatServSock.accept()
            print "Connected to %s from port %s." % client_address
            self.chatCliSock.send('Connection established. Now we can chat!\nType quit() to exit the chat.')
            
            self.inputs.append(self.chatCliSock)

            while 1:
                q = 0 #quit flag
                self.readable, self.writable, self.exceptional = \
                               select.select(self.inputs, self.outputs, self.inputs)
                for s in self.readable:
                    if s is sys.stdin:
                        response = raw_input()
                        self.outputs.append(self.chatCliSock)
                        if response == 'quit()':
                            q = 1
                            break
                    else:
                        msg = self.chatCliSock.recv(self.BUFSIZ)
                        if not msg:
                            q = 1
                            break
                        print "Client:", msg

                if q:
                    break
                
                for s in self.writable:
                    self.chatCliSock.send(response)
                    self.outputs.remove(self.chatCliSock)
                
                for s in self.exceptional: #not really used
                    s.close()
            self.chatCliSock.close()
        
        self.chatServSock.close() #not really used

fdChatServer = FDChatServer('', 3300, 1024)
fdChatServer.run()
