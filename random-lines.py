#!/usr/bin/env python
import random
import argparse
import sys

parser = argparse.ArgumentParser(description='Return random lines of file')
parser.add_argument('file', type=argparse.FileType('r'), help='the input file')
parser.add_argument('-n', '--num', type=int, help='number of lines to return')
parser.add_argument('-p', '--percent', type=float, help='percent of lines to return, i.e. 0.1 for 10 percent')
parser.add_argument('-o', '--output', type=argparse.FileType('w'), help='an output file')
args = parser.parse_args()

if args.num is None and args.percent is None:
    print('Need a num or percent')
    exit(1)
elif args.num and args.percent:
    print('Only pass a num or a percent')
    exit(1)

lines_pulled = 0
num_lines = sum(1 for line in open(args.file.name))
if args.num:
    lines_pulled = args.num
elif args.percent:
    lines_pulled = int(num_lines * args.percent)

if args.output:
    output = args.output
else:
    output = sys.stdout

pull_lines = [random.randint(1, num_lines) for _ in range(lines_pulled)]

for i, line in enumerate(args.file):
    if i in pull_lines:
        output.write(line)
