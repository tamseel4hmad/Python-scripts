#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()
print("------------------------------")
print("      //Network Mapper//      ")
print("------------------------------")

ip_addr = input("IP address: ")
print("IPv4: ",ip_addr)
type(ip_addr)

resp = input("""\nSelect type of Scan
1.SYN ACK Scan
2.UDP Scan
3.Comprehensive Scan \n\n""")
print("\nScan type selected: ", resp)

if resp == '1':
    print("\nNmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
    print("\nNmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
    print("\nNmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp >= '4':
    print("invalid selection\n")    
