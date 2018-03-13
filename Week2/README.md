# SCSC
Swinburne Cyber Security Club

## Week 1: Linux Buffer Overflow
###	Challenge:
		- SwinBuf2 : Without Shellcode
			- SwinBuf2.c
		- Temporary disable ASLR:
			- echo 0 > /proc/sys/kernel/randomize_va_space
		- Compile with:
			- gcc -g -static --no-pie -o SwinBuf2 SwinBuf2.c

		- SwinBuf3 : With Shellcode
			- SwinBuf3.c
		- Temporary disable ASLR:
			- echo 0 > /proc/sys/kernel/randomize_va_space
		- Compile with:
			- gcc -g -z execstack -no-pie -o SwinBuf3 SwinBuf3.c