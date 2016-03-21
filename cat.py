import sys
import os

if len(sys.argv) < 2:
	print('At least 1 file must be specified')
	exit(-1)
else:
	for fl in sys.argv[1:]:
		fl = open(sys.argv[i], 'r')
		print(''.join(fl.readlines())
