# Writeup 3 - Operational Security and Social Engineering

Name: Christopher Howard
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Christopher Howard

## Assignment Writeup

### Part 1 (40 pts)

Elizabeth's ATM number seems like the most difficult to ellicit through social engineering. So, I decided to use a phishing email to her email in order to trick her into divulging her information. It is a safe assumption that she uses her company for her banking services. 
To make the email convincing, I would first sign myself up in 1337 banking services and see what their official emails look like. What seals or symbols they use, the general tone, etc. From this information, I would create an email that resembles the official email used to communicate banking information. I would then email Elizabeth under the pretext that her ATM pin will expire in the next few days and needs to be reset. I will link to a website that appears to be 1337bank.money, except a character will be off. for example, exchanging the "1" with an "l". This website will ask her to input her old pin number and enter a new pin number. At this point, the email will website will tell her that her pin number change will come into effect within 3 business days. This will allow time to be able to use the ATM pin number without her wondering why her new pin isn't working.

As for the rest of the information, I would let Elizabeth divulge it by calling under the pretext of security professionals who have been contracted to improve the security of the banking website. 
Through a diaougue of security, I would also guide the conversation by revealing details about myself that would then prompt her to reveal specfici information about herself. For example, I would talk about password security and how many people use simple passwords based off of thee city they were born in, first pet, etc. After sharing security procedures to create safe passwords, I would tell her my password used to be set to *insert city here* that I grew up in. Throughout the conversation, I can guide it to allow her to divulge information. To help guide it, I will use my knowledge of her speaking Dutch and growing up in the Netherlands to create responses that create an avenue for her to feel comfortable revealing more personal information.
As for her browser, since I am a security consultant, I could simply say that browsers can heavily effect the security of your company and then ask what browser her company tends to use and what she personally uses.



### Part 2 (60 pts)

I have identified three unique security problems in your web server.
1. Weak password
2. Open port which allows for unlimited tries to guess a password and access your private server
3. The CEO having the same username for private and public use

I will give recommendations on how you can solve all of these security issues.

Weak passwords, while easy to remember, allow for much easier guessing on the part of malicious persons wanting to gain access to an account. Your current password is all lower case letters with no numbers and no special symbols. You should have a different password for every account and they should all be complex and strong passwords. 

https://techcrunch.com/2018/12/25/cybersecurity-101-guide-password-manager/

This website will allow you to understand the utility of a password manager, which will allow you to keep track of all the different and complex passwords you will need as you secure your server.

Open ports can also be an issue. The way I was able to access your server was essentially by "guessing" your password over and over again through a program accessing your open port. There are many ways to prevent attackers from doing this type of attack, which is called a "brute force" login attack.

https://www.computerweekly.com/answer/Techniques-for-preventing-a-brute-force-login-attack

This website will help you understand some of the measures that can be taken to prevent these attacks. My personal reccommendation, which is mentioned on the website, is to lockout an account after an arbitrary amounts of tries. Let’s say 10 tries. From there, an admin will have to come and unlock the account so it can be used again.

Lastly, there is the issue of easily accessible usernames. For example, the username we used to gain access to your account was also the same on your twitter. Usernames are not typically thought of something that needs to be kept secret, but they are 50% of what an attacker needs to gain access to an account. This security tip is simple to implement. Do not allow yoursef or your employees to use usernames which are publically used elsewhere. It may even be best to assign randomly generated usernames to their work accounts.

