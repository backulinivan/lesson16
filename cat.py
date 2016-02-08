import sys
import os

for i in range(1, len(sys.argv)):
	fl = open(sys.argv[i], 'r')
	print(''.join(map(str, fl.readlines())))

