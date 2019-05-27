import sys
import json
import random


fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

for line in fin:
    if not line.strip():
        fout.write(line)
        continue
    r = random.random()
    if r > 0.02:
        fout.write(line)
        continue
    words = line.split(' ')
    lw = len(words)
    tl = random.randint(1, lw)
    new_line = ' '.join(words[:tl]).strip() + '\n'
    fout.write(new_line)
