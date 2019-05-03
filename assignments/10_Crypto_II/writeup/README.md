# Crypto II Writeup

Name: Christopher Howard
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Christopher Howard

## Assignment Writeup

### Part 1 (70 Pts)
First, I took note that I had a secret key and and a file to decrypt it with. I then used "gpg --import key.asc" so that I could use the private key to decrypt the file. Then I used the command "gpg --decrypt message.txt.gpg" and that displayed the contents of that flag to my terminal. The flag I found was:
m3ss@g3_!n_A_b0ttl3

After reading the contents of the file, I followed the instructions by taking a screenshot and also creating the signature.txt file with the contents, "My name is Christopher Howard". I then used the command "gpg --clearsign signature.txt" to sign the file and generate the signature.txt.asc file. I deleted the signature.txt file, completing the instructions found in the file.

### Part 2 (30 Pts)

1. Both pictures are scrambled and encrypted. However, the cbc.bmp is much more scrambled than the ebc.bmp file. I am still able to make out the general shape of the orgininal picture from looking at the ebc file, while I cannot make out anything by looking at the cbc.bmp file.

2. the ecb cipher is less secure. This is because it lacks the extra layer of complexity that the cbc cipher has. This is because with cbc, each block is dependent on all previous blocks processed up to that point. 

*Your reflection goes here*
