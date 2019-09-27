import json
import sys
import random

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

for line in fin:
    if random.random() > 0.1: continue
    json_dict = json.loads(line)
    title = json_dict.get('title', "")
    body = json_dict.get('contents', "")
    url = json_dict.get('url', "")
    
    docno = json_dict['id']
    
    snippet = ' '.join(body.split()[0:100])
    
    field_token = ["titlestart", "bodystart", "urlstart"]
    sents = [field_token[i] + " " +  t for i, t in enumerate([title, snippet, url]) if t]
    random.shuffle(sents)
    for sent in sents:
        fout.write(sent.strip())
        fout.write("\n")
    fout.write("\n")
    
