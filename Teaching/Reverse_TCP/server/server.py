import socket

version = socket.AF_INET # IPV4
proto   = socket.SOCK_STREAM #TCP

sock = socket.socket(version,proto)# Our Socket

sock.bind(("127.0.0.1",31338)) # Bind to a port
sock.listen()   #Listen For connections
while True:    #infinete loop
    con,addr = sock.accept() #Accept Connection
    print("Connecion from: {}".format(addr[0])) #Print name

    command = ""            # empty command
    while "!exit" not in command: # wait for exit
        command = input("{}:$".format(addr[0])) #ask for command
        con.send(command.encode()) #send command

        data = con.recv(1024)
        out = data.decode()
        if len(data) >= 1024:
            data = con.recv(1024)
            out += data.decode()
        print(out)
    break


