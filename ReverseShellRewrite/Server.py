from socket import socket, AF_INET, SOCK_STREAM
from functools import partial

s = socket(AF_INET,SOCK_STREAM)
s.bind(("0.0.0.0",1338))

cs, clientId = s.accept()

for msg in iter(partial(cs.read,1024),"quit()"):
    print(msg)
