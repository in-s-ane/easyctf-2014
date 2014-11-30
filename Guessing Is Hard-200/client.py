#! /usr/bin/python

import socket
import random

HOST = "python.easyctf.com"
PORT = 10663

def main():
    while (True):
        random.seed()
        secret = random.random()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        received = sock.recv(1024)
        sock.sendall(str(secret));
        received = sock.recv(1024)
        if received != "NOPE\n":
            print "`" + received + "`"
            break
        sock.close()

main()
