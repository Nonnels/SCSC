#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
*  Temporary disable ASLR:
*		echo 0 > /proc/sys/kernel/randomize_va_space
*  Compile with:
*		gcc -no-pie -z execstack -o SwinFor1 SwinFor1.c
*/

int main(int argc, char **argv) {
	char buf[1024];
	strcpy(buf, argv[1]);
	printf(buf);
	printf("\n");
	exit(0);
}