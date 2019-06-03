import json
import sys
import random

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

for line in fin:
    json_dict = json.loads(line)
    title = json_dict.get('title', "")
    body = json_dict.get('body', "")
    url = json_dict.get('url', "")
    inlink = json_dict.get('inlink', "")
    #inlink = inlink.encode('ascii', 'ignore')
    inlink = inlink.encode('ascii', 'ignore').decode('utf-8')
    inlink = '; '.join(inlink.split('\t'))
    
    docno = json_dict['docno']
    
    snippet = ' '.join(body.split()[0:100])
    
    field_token = ["titlestart", "bodystart", "urlstart", "inlinkstart"]
    sents = [field_token[i] + " " +  t for i, t in enumerate([title, snippet, url, inlink]) if t]
    random.shuffle(sents)
    for sent in sents:
        fout.write(sent.strip())
        fout.write("\n")
    fout.write("\n")
    
