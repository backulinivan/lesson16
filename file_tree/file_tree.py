import argparse
import os
import sys

parser = argparse.ArgumentParser(
    description= 'outputs file tree of a catalogue'
    )

parser.add_argument(
    'f_dir',
    metavar = 'FILE OR DIRECTORY',
    type = str,
    nargs = 1,
    help = 'print file or directory path'
    )

parser.add_argument(
    '-f',
    '--folders_only',
    action = 'store_true',
    help = 'show only folders'
    )

parser.add_argument(
    '-i',
    '--include',
    action = 'store',
    help = 'show only those files or folders which contain included text'
    )

parser.add_argument(
    '-e',
    '--exclude',
    action = 'store',
    help = 'show only those files or folders which do not contain included text'
    )

args = parser.parse_args()

print(os.path.abspath(args.f_dir[0]))

'''недостаток программы в невыборочности методов -i и -e,
то есть исключаем или выбираем и папки и файлы одновременно
что может не привести к желаемому результату'''

def tree(path, n):
    files = os.listdir(path)

    if args.include:
        files = {obj for obj in files if args.include in obj}

    if args.exclude:
        files = {obj for obj in files if args.exclude not in obj}

    for obj in files:
        if os.path.isdir(path + '/' + obj):
            print('    '*n + obj)
            tree(path + '/' + obj, n+1)
        elif not args.folders_only:
            print('    '*n + obj)

tree(args.f_dir[0], 0)

