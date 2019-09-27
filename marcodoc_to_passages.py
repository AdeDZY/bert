import json
import sys
import re

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

nlines =0
npassages =0
passage_len = 200
for line in fin:
    nlines += 1
    if nlines % 10000 == 0:
        print("processed {} lines, {} passages/doc".format(nlines, float(npassages)/nlines))
    json_dict = json.loads(line)
    #title = json_dict.get('title', "")
    doc_body = json_dict.get('contents', "")
    doc_id = json_dict['id'] 
    words = doc_body.split(' ')
    s = 0
    while s < len(words):
        e = min(len(words), s + passage_len)
        new_json_dict = {"id": doc_id+'_passage_{}_{}'.format(s, e), "contents": ' '.join(words[s:e]), 'title': json_dict["title"], "url": json_dict["url"]} 
        out_str = json.dumps(new_json_dict)
        fout.write(out_str)
        fout.write('\n')
        s = e
        npassages += 1
