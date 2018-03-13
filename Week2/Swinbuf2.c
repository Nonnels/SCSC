#include <stdio.h>

/* 
*  Temporary disable ASLR:
*		echo 0 > /proc/sys/kernel/randomize_va_space
*  Compile with:
*		gcc -g -static --no-pie -o SwinBuf2 SwinBuf2.c
*/

int check_pin()
{
	char pin[10];
	int x = 15, i;
	printf("Enter password: ");
	gets(pin);
	for (i = 0; i<10; i += 2) x = (x & pin[i]) | pin[i + 1];
	if (x == 48) return 0;
	else return 1;
}

void main()
{
	if (check_pin()) printf("Fail!\n");
	else printf("You win!\n");
}