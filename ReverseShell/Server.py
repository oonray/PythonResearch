from socket import socket, AF_INET, SOCK_STREAM
from functools import partial
from subprocess import Popen,PIPE

s = socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",1338))
s.listen(5)
cs, clientId = s.accept()

s.send(input("$>").encode())
for msg in iter(partial(cs.read,1024),"quit()"):
    print(msg)
    s.send(input("$>"))
    
