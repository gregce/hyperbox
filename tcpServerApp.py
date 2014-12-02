
#import moduels
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
#maximum number of incoming conection requests before connections are turned away
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '... connected from:', addr
    
    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))
    tcpCliSock.close()
tcpCliSock.close()
  