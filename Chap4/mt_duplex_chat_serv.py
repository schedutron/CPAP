#!usr/bin/env python
from __future__ import print_function
from socket import *
import sys
from threading import Thread

class ChatServer():
    def __init__(self, host, port, bufsiz):
        self.HOST = host
        self.PORT = port
        self.BUFSIZ = bufsiz
        self.ADDR = (host, port)

        self.chatServSock = socket(AF_INET, SOCK_STREAM)
        self.chatServSock.bind(self.ADDR)
        self.msg = ""
        self.your_msg = ""
        self.connected = False
        self.recv_thread = Thread(target=self.get_msg, args=tuple())
        self.raw_input_thread = Thread(target=self.get_your_msg)

    def get_msg(self):
        while 1:
            self.msg = self.chatCliSock.recv(self.BUFSIZ)
            if self.msg == "quit()":
                print("\t\tClient left the chat.\n")
                self.connected = False
                break

            print("\r\t\tClient:", self.msg)
            print("-|")


    def get_your_msg(self):
        while self.connected:
            while self.your_msg == "":
                self.your_msg = raw_input("-|\n")

            self.chatCliSock.send(self.your_msg)
            if self.your_msg == 'quit()':
                self.connected = False
                break
            self.your_msg = ""

    def run(self):
        self.chatServSock.listen(1) # num can be passed to __init__

        while True:
            print("Waiting for connection...")
            self.chatCliSock, self.cliAddr = self.chatServSock.accept()
            self.chatCliSock.send('Connection established. Now we can chat!')

            self.connected = True
            print("Connected to:", self.cliAddr)
            self.recv_thread.start()
            self.raw_input_thread.start()
            self.recv_thread.join()
            self.raw_input_thread.join()
            '''
            while self.connected:
                if self.msg:
                    if self.msg == "quit()":
                        print("Client left the chat.\n")
                        self.connected = False
                        break

                    print("\rClient:", self.msg)
                    #sys.stdout.write("-|-> ")
                    self.recv_lock.acquire()
                    self.msg = ""
                    self.recv_lock.release()

                if self.your_msg:
                    self.chatCliSock.send(self.your_msg)
                    if self.your_msg == 'quit()':
                        self.connected = False
                        break
                    self.lock.acquire()
                    self.your_msg = ""
                    self.lock.release()
            '''

        self.chatServSock.close() #not really used

if __name__ == '__main__':
    chatServer = ChatServer('', 33000, 1024)
    chatServer.run()
