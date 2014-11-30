#! /usr/bin/python

import socket
import random

HOST = "python.easyctf.com"
PORT = 10661

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    while (True):
        random.seed() # Server is dumb and sets the seed every time... so if we set our seed every time we connect to it, maybe our times will sync up??
        secret = random.random()
        sock.sendall(str(secret));
        received = sock.recv(1024)
        if received != "Nope!": # Only exits from while loop when server gives us the flag
            print received
            break

    sock.close()

main()
