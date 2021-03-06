import json
import sys
import re
import nltk

nltk.data.path.append("/bos/usr0/zhuyund/nltk_data/")

def to_passages(sentences):
    passages = []
    s, e = 0, 0
    target_length = 300 
    sent_lengths = [len(sent.split(' ')) for sent in sentences]
    while s < len(sentences):
        curr_p_len = sent_lengths[e] 
        while curr_p_len < target_length:
            e += 1
            if e >= len(sentences):
                break
            curr_p_len += sent_lengths[e] 
        passages.append((s, e))
        if e > s:
            s = e + 1 # one setence overlap
            e = s
        else:
            s += 1
            e = s
    return passages

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

nlines =0
for line in fin:
    nlines += 1
    if nlines % 10000 == 0:
        print("processed {} lines".format(nlines))
    json_dict = json.loads(line)
    doc_id = json_dict['id']
    body  = json_dict.get('body', "")
    title = json_dict.get('title', "").strip().lstrip()
    if not body:
        continue
    body = re.sub(r'____*', '___', body)
    body = re.sub(r'----*', '---', body)
    body = re.sub(r',,,,*', ',,,', body)
    body = re.sub(r'\.\.\.\.*', '\.\.\.', body)
    body = re.sub(r'(\W\W\W\W\W\W\W\W\W\W)\W*', r'\1', body)
    body = re.sub(r'([\W0-9]{30})[\W0-9]*', r'\1', body)
    sentences = nltk.sent_tokenize(body) 
    passage_indexes = to_passages(sentences) 
    np = 0
    for s, e in passage_indexes:
        new_json_dict = {"id": doc_id+'_passage_{}'.format(np), "body": ' '.join(sentences[s:e+1]), "title": title} 
        out_str = json.dumps(new_json_dict)
        fout.write(out_str)
        fout.write('\n')
        np += 1
