#include <string.h>
#include <stdio.h>

/* 
*  Temporary disable ASLR:
*		echo 0 > /proc/sys/kernel/randomize_va_space
*  Compile with:
*		gcc -g -z execstack -no-pie -o SwinBuf3 SwinBuf3.c
*/

void main(int argc, char *argv[]) {
	copier(argv[1]);
	printf("Done!\n");
}
int copier(char *str) {
	char buffer[100];
	strcpy(buffer, str);
}