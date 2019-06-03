import json
import sys
#import spacy
import re
import nltk

#nlp = spacy.load('en') 

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

for line in fin:
    json_dict = json.loads(line)
    title = json_dict.get('headline', "")
    if not title: title = ""
    body = json_dict.get('body', "")
    doc = title + '\n' + body
    #sentences = [sent.string.strip() for sent in doc.sents]
    sentences = nltk.sent_tokenize(doc) 
    for sent in sentences:
        fout.write(sent)
        fout.write("\n")
    fout.write("\n")
    
