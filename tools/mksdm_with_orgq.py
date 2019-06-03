#!/usr/bin/env python
import argparse
import sys, os

parser = argparse.ArgumentParser()
parser.add_argument("queryFile", type=argparse.FileType('r'))
parser.add_argument("orgQueryFile", type=argparse.FileType('r'))
parser.add_argument("w1", type=float)
parser.add_argument("w2", type=float)
parser.add_argument("w3", type=float)
parser.add_argument("outFile", type=argparse.FileType('w'))
args = parser.parse_args()

stopwords = set([line.strip() for line in open("/bos/usr0/zhuyund/query_reweight/stopwords2")] + ["information", "looking", "find"]) 

n = 0
args.outFile.write("<parameters>\n")
args.outFile.write("<index>/bos/tmp11/zhuyund/buildIndex_robust04/robust04_index/</index>\n")
args.outFile.write("<trecFormat>true</trecFormat>\n")
args.outFile.write("<count>1000</count>\n")

qid2bi = {}
qid2w = {}
for line in args.orgQueryFile:
    line = line.strip()
    n, q = line.strip().split('\t')
    q_tokens = [t for t in q.split(' ') if t.strip() if t.lower() not in stopwords]
    bigram_str = " ".join(["#1({} {})".format(q_tokens[i], q_tokens[i + 1]) for i in range(len(q_tokens) - 1) ])
    window_str = " ".join(["#uw8({} {})".format(q_tokens[i], q_tokens[i + 1]) for i in range(len(q_tokens) - 1) ])
    qid2bi[int(n)] = bigram_str
    qid2w[int(n)] = window_str 
    
    
for line in args.queryFile:
    line = line.strip()
    #n += 1
    n, q = line.strip().split('\t')
    items = q.split(' ')
    n = int(n)
    
    bow_str = q 
    bigram_str = qid2bi[n]
    window_str = qid2w[n]
    q_str = "#weight( {0} #weight({1}) {2} #combine({3}) {4} #combine({5}))".format(args.w1, bow_str, args.w2, bigram_str, args.w3, window_str)

    args.outFile.write("<query><number>{0}</number><text>{1}</text></query>\n".format(n, q_str))

args.outFile.write("</parameters>")
