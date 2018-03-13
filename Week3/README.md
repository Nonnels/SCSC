# SCSC
Swinburne Cyber Security Club

## Week 3: Exploiting a Format String Vulnerability
###	Challenge:
		- Temporary disable ASLR:
			- echo 0 > /proc/sys/kernel/randomize_va_space
		- Compile with:
			- gcc -no-pie -z execstack -o SwinFor1 SwinFor1.c