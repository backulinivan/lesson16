import argparse
import sys

parser = argparse.ArgumentParser(
	description = 'Calculator'
	)

parser.add_argument(
	'values',
	metavar = 'VALUES',
	type = float,
	nargs = 2,
	help = 'input values'	
	)

parser.add_argument(
	'-a',
	'--action',
	metavar = 'ACTION',
	action = 'store',
	help = 'action you wish to perform'
	)

parser.add_argument(
	'-v',
	'--verbose',
	action = 'store_true',
	help = 'print the calculation'
	)

args = parser.parse_args()

res = 0

if args.action == '+':
	res = args.values[0] + args.values[1]
elif args.action == '-':
	res = args.values[0] - args.values[1]
elif args.action == '*':
	res = args.values[0] * args.values[1]
elif args.action == '/':
	res = args.values[0] / args.values[1]

if not args.verbose:
	print(res)
else:
	print(str(args.values[0]) + args.action + str(args.values[1]) + '=' + str(res))
	

