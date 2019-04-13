/*
 * Name: Christopher Howard
 *
 * Section: 0201
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Christopher Howard
 */

/* your code goes here */

#include <stdio.h>
int main(int argc, char * argv[]) {

	int num1 = 4277009102;
	int num2 = 485163226;


	printf("%d\n%d\n", num1, num2);
	
	int temp = num2;
	num2 = num1;
	num1 = temp;

	printf("%d\n%d\n", num1, num2);
	
	return 0;
}
