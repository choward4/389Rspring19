# Crypto I Writeup

Name: Christopher Howard
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Christopher Howard

## Assignment Writeup

### Part 1 (70 Pts)
The first step in cracking the hashes present in the hashes.txt is to read and parse them into a list so you are able to compare your results later on. Then, do the same thing with the passwords from passwords.txt. Now, I needed to cycle through every variation of a lowercase character prepended to the passwords in passwords.txt, as per the specification. In every variation, I took the combination and hashed it using the sha256 hashing algorithm, and then checked to see if the resulting hash was in the list I had parsssed from hashes.txt. If it was, I printed out the required information in the format required.

### Part 2 (30 Pts)
Now that we have the core code to crack hashes, we can take the skeleton of that code and make some modifications to crack a particular hash given to us by the server three times to get the flag. I opened up a connection to the server and set up a while loop that would repeat three times. First, I read the output from m the server and parsed the hash from it, then I did the same combination and hashing process I used in Part 1, but I checked if the hash matched the hash given to me by the server. Once I the corresponding combination, I sent that back to the server (with a newline to terminate). After the third hash was cracked, the loop exited and I recieved one more time from the server to see the flag.

flag: h@ash1ng_@nd_sl@ash1ng


