# Crypto II Writeup

Name: Christopher Howard
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Christopher Howard

## Assignment Writeup

### Part 1 (40 Pts)

flag: y0u_ar3_th3_SQ1_ninj@

Looking t this website, there were no text boxes to exploiut. However, clicking on the different links changed the url in a predictable way. At the end of the URL, the id changed from 0, to 1, to 2. This looked like an input that I could manipulate for a SQL injection. I first tried the input "1 OR 1 = 1 -- -". I got a notification from the server that a SQL injection was attempted. After trying other inputs, I realized that the server was probably blocking part of my input, such as the SQL "OR" command. To get around this, I changed OR to "||", and this revealed the flag. The SQL injection was successful.

### Part 2 (60 Pts)

1.
For the first level, I tried the most simple xss attack first by simply adding javascript in with a script tag. The input I went with was "<script>alert()</script>". When the query executed, it displayed an alert on the page and the challenge was completed.

2.
For the second level, I first tried entering a script tag into the message board directly. However, it seemed the website was sanitizing the input I was giving it and wouldn't allow for any script tags. This meant I needed to insert javascript without tags. To do this, I used the img html tag and set onerror to equal alert(). The input was formatted as "<img src="foo.jpg" onerror="alert()">". This allowed me to upload javascript to the browser and cause an alert.

3.
looking at the website, there is no text box to enter data into like the other challenges. Since there was no text box, I immediately was drawn to the url. As I clicked between the images, I noticed that the only thing changing in the url was the frame number. Looking at the source code, I confirmed that this could be used to inject javascript. The choose_tab(num){...} function took in whatever was entered in the url. So, I used the onerror attribute in the url. At the end of the url, I typed in "frame#3' onerror='alert()';. This inserted the onerror attribute into the img tag and sucessfully triggered an alert.

4.
This was difficult. Following the hints, I entered an apostrophe into the text box to see what would happen. After experimenting and looking at the source code, I entered this input, ');alert('  . This input ended the statement prematurely, and then started an alert which would capture the remainder of the code. This input triggered the alert.

5.
Navigating to the singup for the email, I noticed the next parameter in the url was set to confirm. I also looked at the source code in confirm.html and signup.html to notice how the next parameter was incorperated. So, I went to the signup url with next=javascript:alert(). I then entered an email, clicked next, and was able to trigger an alert

6.
Looking at the hints, I realized that the security check on the url was not case sensitive. This means I can go to a http website by simply typing it as hTTp or something of that type. To host the javascript alert, I go to pastebin.com and create an entry with just "alert();". I then link to that url after "frame#" and make sure the change the cases of http. This triggers the alert


