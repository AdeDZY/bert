import json
import sys
import spacy

nlp = spacy.load('en') 

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

for line in fin:
    json_dict = json.loads(line)
    title = json_dict.get('.T', "")
    body = json_dict.get('.W', "")
    doc = nlp(title + '\n' + body)
    sentences = [sent.string.strip() for sent in doc.sents]
    for sent in sentences:
        fout.write(sent)
        fout.write("\n")
    fout.write("\n")
    
