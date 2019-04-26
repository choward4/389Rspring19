#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    f = open("hashes.txt", 'r')
    hashes = f.read().split('\n')
    hashes.pop()
    f.close()

    f = open("passwords.txt", 'r')
    passwords = f.read().split('\n')
    passwords.pop()
    f.close()
    
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    
    times = 0
    while times < 3:
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(times)
        # s.connect((server_ip, server_port))
        data = s.recv(1024)
        print("data:", data)
        data = data.decode().split('\n')
        crackHash = data[2]
        answer = ''
        for c in characters:
            for p in passwords:
                inputStr = c + p
                to_hash = inputStr.encode('utf-8')
                cpHash = hashlib.sha256(to_hash)
                hex_dig = cpHash.hexdigest()

                if hex_dig == crackHash:
                    print("hex dig matched hash")
                    answer = to_hash
                   
        
        s.send(answer)
        s.send("\n".encode("utf-8"))
        print(answer)
        times += 1
    
    # crack 3 times
    flag = s.recv(1024)
    flag = flag.decode()
    print(flag)

if __name__ == "__main__":
    server_crack()
