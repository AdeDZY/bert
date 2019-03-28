import json
import sys
import random

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

for line in fin:
    json_dict = json.loads(line)
    codes = json_dict["codes"].values()
    codes_tokens = [["RCV" + t for t in t2] for t2 in codes]
    codes_text = " ".join([" ".join(t) for t in codes_tokens])
    title = json_dict.get('headline', "")
    if not title: title=""
    body = json_dict.get('body', "")
    doc = title + body
    
    sentence1 = codes_text 
    doc = doc.replace('\n', ' ')
    sentence2 = ' '.join(doc.split(' ')[0:200])
    sents = [sentence1, sentence2]
    random.shuffle(sents)
    for sent in sents:
        fout.write(sent.strip())
        fout.write("\n")
    fout.write("\n")
