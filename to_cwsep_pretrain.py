import json
import sys
import random
import nltk

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

for line in fin:
    json_dict = json.loads(line)
    title = json_dict.get('title', "")
    body = json_dict.get('body', "")
    url = json_dict.get('url', "")
    inlink = json_dict.get('inlink', "")
    #inlink = inlink.encode('ascii', 'ignore')
    inlink = inlink.split('\t')
    snippet = ' '.join(body.split()[0:100])
    
    if title:
        fout.write(title + '\n\n')
    
    if url:
        fout.write(url + '\n\n')
   
    if inlink:
        tmp = '\n'.join(inlink)
        tmp = tmp.encode('ascii', 'ignore').decode('utf-8')
        fout.write(tmp)
        fout.write('\n\n')

    if snippet:
        sents = nltk.sent_tokenize(snippet)
        fout.write('\n'.join(sents))
        fout.write('\n\n')



    
