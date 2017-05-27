#!/usr/bin/env python

from socket import *
import sys, select
from half_duplex_chat_clnt import ChatClient

class FDChatClient(ChatClient):
    def __init__(self, bufsiz):
        ChatClient.__init__(self, bufsiz)

    def run(self):
        self.chatCliSock.connect(self.hostAddr)
        #self.chatCliSock.setblocking(0) #to avoid blocking
        
        print self.chatCliSock.recv(self.BUFSIZ)
        self.inputs = [sys.stdin, self.chatCliSock]
        self.outputs = []

        while 1:
            q = 0 #quit flag
            self.readable, self.writable, self.exceptional = \
                           select.select(self.inputs, self.outputs, [])
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
                    print "Server:", msg

            if q:
                break
    
            for s in self.writable:
                self.chatCliSock.send(response)
                self.outputs.remove(self.chatCliSock) #so that resend doesn't happen
            for s in self.exceptional: #not really used
                ed
                s.close()
        self.chatCliSock.close()

fdChatClient = FDChatClient(1024)
fdChatClient.run()
