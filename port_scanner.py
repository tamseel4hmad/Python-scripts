#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
host = input("IPv4: ")
port = int(input("port: "))

def portScanner(port):
    if s.connect_ex((host,port)):
        print("port is closed")
    else:
        print("port "+str(port)+ " is open")

portScanner(port)