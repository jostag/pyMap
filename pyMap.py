# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:25:06 2019

@author: josh
"""

import argparse
import socket

def bannerGrabber(connSock, targPort):
    try:
        if targPort == 80 or targPort == 443:
            request = "GET / HTTP/1.1\nHost: "+"\n\n"
            connSock.send(request.encode())
        else:
            request = "\n"
            connSock.send(request.encode()) 
        #Store results
        results = connSock.recv(1024)
        
        print('[+] Banner:' + str(results))
    except:
        print('[+] Banner not available\n')
  
def connectScan(targHost, targPort):
    try:
        #Create the socket object
        connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Connect to target
        connSock.connect((targHost, targPort))
        
        print('[+] %d tcp open'% targPort)
        bannerGrabber(connSock, targPort)
    except:
        print('[+] %d tcp closed'% targPort)
    finally:
        connSock.close()
        
def portScan(targHost, targPorts):
    try:
        targIP = socket.gethostbyname (targHost)
    except:
        print('Error: Host unreachable.')
        exit (0)
    
    try:
        targName = socket.gethostbyaddr (targIP)
        print("[+]- - - Results For: " + targName[0] + "- - -")
    except:
        print("[+]- - - Results For: " + targIP + "- - -")
    
    socket.setdefaulttimeout(2)
    
    for targPort in targPorts:
        connectScan (targHost, int(targPort))
    
def main():
    parser = argparse.ArgumentParser('TCP Client Scanner')
    parser.add_argument("-a", "--address", type=str, help="Target IP Address")
    parser.add_argument("-p", "--port", type=str, help="Port number to be scanned")
    args = parser.parse_args()
    #Store Arguments
    ipaddress = args.address
    portNumber = args.port.split(',')
    
    portScan(ipaddress, portNumber)

if __name__ == "__main__":
    main()
    
