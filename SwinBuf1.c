#include <string.h>
#include <stdio.h>

// to compile
// gcc -g -fno-stack-protector -z execstack -o SwinBuf1 SwinBuf1.c

main() {
	char name[200];
	printf("What is your name?\n");
	scanf("%s", name);
	bufferoverflow(name, "uname -a");
}

int bufferoverflow(char *name, char *cmd) {
	char c[40];
	char buffer[40];
	printf("Name buffer address:    %x\n", buffer);
	printf("Command buffer address: %x\n", c);
	strcpy(c, cmd);
	strcpy(buffer, name);
	printf("Goodbye, %s!\n", buffer);
	printf("Executing command: %s\n", c);
	fflush(stdout);
	system(c);
}
