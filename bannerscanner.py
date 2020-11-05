#!/usr/bin/python3

import socket

def main():
    host = input("IPv4: ")
    port = int(input("port: "))
    banner(host,port)

def banner(host,port):
    s = socket.socket()
    s.connect((host,port))
    s.settimeout(5)
    print(s.recv(1024))

main()
