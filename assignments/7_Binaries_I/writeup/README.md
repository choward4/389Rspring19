# Writeup 7 - Binaries I

Name: Christopher Howard
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Christopher Howard

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
#include <stdio.h>
int main(int argc, char * argv[]) {

	int num1 = 4277009102;
	int num2 = 485163226;

	printf("%d\n%d\n", num1, num2);

	int temp = num2;
	num2 = num1;
	num1 =  temp;

	printf("%d\n%d\n", num1, num2);

	return 0;
}
```

### Part 2 (10 Pts)

The program first creates two numbers ints. In decimal, they are 4277009102 andd 485163226. The program then prints the first and the second number with new lines separating them. Then, the program uses xors to essentially swap the two numbers in memory. Then, the program prints out the numbers again in the same way. Then it exits.
