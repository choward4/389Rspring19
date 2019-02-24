# Writeup 2 - OSINT

Name: Christopher Howard
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Christopher Howard

## Assignment Writeup

### Part 1 (45 pts)

*Please use this space to writeup your answers and solutions (and how you found them!) for part 1.*
1.
v0idcache's real name is Elizabeth Muffet. I discovered this by going to checkusernames.com and searching the username v0idcache. from there, I was able to find out that the username was in use on twitter and searched for v0idcache on twitter. The twitter has her name.

2.
v0idcache works at Elite Banking. Their website url is 1337bank.money. I discovered this link to her website and work affiliation in her twitter bio, which was discvered through checkusernames.com.

3.
All of the following were found with checkusernames.com
- Twitter.com/v0idcache: She is a banking CEO for elite banking. She is from the Netherlands
- Github.com/v0idcache: No personal information

4.
142.93.136.81
location: Canada, ON, Ontario
history:
how: I discovered this through centralloops.net and entering the website url I discovered from her twitter. This gave the information of the IP address and the location.

5.
/secret_directory
I found this from using the /robots.txt directory within the banking website. This allowed me to to see the secret directory
flag: h1ding_fil3s_in_r0bots_L0L

I found the next flag from looking into the source code from the website by using f12. When I was looking through the source code, I was looing for comments that could contain sensitive information
flag: hi1dden_in_plain_5ight

6.
I found the following information through the website t1shopper.com using their port scan tool, scanning the IP address obtained from the banking website.
22 ssh
80 http
1337 menandmice-dns

7.
The operating system of the website is Ubuntu. I discovere this by going to Censys.io and entering the IP address.

8.



### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload yourcompleted source code to this /writeup directory as well!*

flag: brut3_f0rce_m4ster
For my solution to part 2, I scanned the open ports using the t1shopper.com and found that there were 3 open ports. From there, I nc'd into each port on the server until I had a login screen. Fro mthere, I began to write my bruteforce program which took advantage of rockyou.txt wordlist. The program read through the file, opening a connection and sending different password until it did not return "fail". The username was constant because I assumed that Elizabeth would also use v0idcache for her username. Once I gained access, I cd'd into different directoies until I found the flag.txt document.
