#import pybk
#from pyb import *
#import os
import struct
program = None

with open("out.bin", "rb") as f:
    program = f.read()
if(((program[1] & 0b10000000)) != 0):
	print ("8th bit is 1")
else:
	print ("8th bit is 0")
	
#not totally sure how reading binary files works in python but this was my original idea
for i in program:
	if i & 0b10000000 == 1:
		print(f"bit {i} is 1")
	else:
		print(f"bit {i} is 0")
