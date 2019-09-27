import json
import sys
import random
import nltk

random.seed(9123)

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

for line in fin:
    if random.random() > 0.1: 
        continue
    json_dict = json.loads(line)
    title = json_dict.get('title', "")
    body = json_dict.get('contents', "")
    url = json_dict.get('url', "")
    snippet = ' '.join(body.split()[0:300])
    
    if title:
        fout.write(title + '\n\n')
    
    if url:
        fout.write(url + '\n\n')
   
    if snippet:
        sents = nltk.sent_tokenize(snippet)
        fout.write('\n'.join(sents))
        fout.write('\n\n')



    
