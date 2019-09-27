import json
import sys
import random

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

for line in fin:
    json_dict = json.loads(line)
    title = json_dict.get('title', "")
    body = json_dict.get('paperAbstract', "")
    body = ' '.join(body.split('\n'))
    
    body_terms = body.split(' ')
    if len(body_terms)>100:
        body = ' '.join(body_terms[0:100])

    venue = json_dict.get('venue', "")
    author_list = json_dict.get('authors', "")
    if author_list:
        authors = ', '.join([t["name"] for t in author_list]) 
    else:
        authors = ""
    sents = [t for t in [title, body, venue, authors] if t]
    random.shuffle(sents)
    for sent in sents:
        fout.write(sent.strip())
        fout.write("\n")
    fout.write("\n")
    
