#!/usr/bin/env python3

import hashlib
import string

def crack():

    f = open("hashes.txt", 'r')

    hash_data = f.read()
    hashes = hash_data.split('\n')
    hashes.pop()
    f.close()

    f = open("passwords.txt", 'r')
    
    pass_data = f.read()
    passwords = pass_data.split('\n')
    passwords.pop()
   
    f.close()

    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            inputStr = c + p
            to_hash = inputStr.encode('utf-8')
            cpHash = hashlib.sha256(to_hash)
            hex_dig = cpHash.hexdigest()
            
            if hex_dig in hashes:
                to_print = inputStr + ":" + hex_dig 
                print(to_print)
            # crack hashes

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
