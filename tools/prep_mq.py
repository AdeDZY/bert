#!/opt/python27/bin/python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("queryfile", type=argparse.FileType("r"))
parser.add_argument("outfile", type=argparse.FileType("w"))
parser.add_argument("--start", "-s", type=int, default=1)
args = parser.parse_args()

args.outfile.write('<parameters>\n')
args.outfile.write('<index>/bos/tmp11/zhuyund/buildIndex_robust04/robust04_index</index>\n')
args.outfile.write('<trecFormat>true</trecFormat>\n')
args.outfile.write('<count>1000</count>\n')
n = args.start
for line in args.queryfile:
	line = line.strip()
	q = line
	n, q = line.split('\t')
	args.outfile.write('<query><number>{0}</number><text>#weight({1})</text></query>\n'.format(n, q))
	#n += 1
	#if n > 100000:
	#	 break

args.outfile.write('</parameters>')	
