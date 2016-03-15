import sys
import os

if len(sys.argv) < 2:
	print('At least 1 file must be specified')
	exit(-1)
else:
	for i in range(1, len(sys.argv)):
		fl = open(sys.argv[i], 'r')
		print(''.join(map(str, fl.readlines())))

