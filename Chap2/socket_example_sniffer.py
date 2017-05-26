import socket

#the public network interface
HOST = socket.gethostbyname(socket.gethostname())

#create a raw socket and bind it to the public network interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

#include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

#receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

#receive a package
print(s.recvfrom(65535))

#disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
