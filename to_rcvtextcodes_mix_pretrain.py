import json
import sys
import random
import nltk

fin = open(sys.argv[1])
codes_vocab_f = open(sys.argv[2])
fout = open(sys.argv[3], 'w')

codes_vocab = {}
for line in codes_vocab_f:
    c, t = line.strip().split('\t')
    codes_vocab[c] = t

for line in fin:
    json_dict = json.loads(line)
    
    if random.random() < 0.5:
        title = json_dict.get('title', "")
        body = json_dict.get('body', "")
        if not title: title = ""
        if not body: body = ""
        doc = title + '\n' + body
        sentences = nltk.sent_tokenize(doc)
        for sent in sentences:
            fout.write(sent)
            fout.write("\n")
        fout.write("\n")
        continue
    codes = json_dict["codes"]

    country_codes = codes.get("bip:countries:1.0", [])
    topic_codes = codes.get("bip:topics:1.0", [])
    industry_codes = codes.get("bip:industries:1.0", [])

    random.shuffle(country_codes)
    random.shuffle(topic_codes)
    random.shuffle(industry_codes)
    
    if country_codes:
        country_code_text = "CODECOUNTRY " + ' , '.join([codes_vocab.get(t, "") for t in country_codes])
    if topic_codes:
        topic_code_text = "CODETOPIC " + ' , '.join([ codes_vocab.get(t, "")  for t in topic_codes])
    if industry_codes:
        industry_code_text = "CODEINDUSTRY " + ' , '.join([codes_vocab.get(t, "") for t in industry_codes])

    title = json_dict.get('headline', "")
    if not title:
        title = ""
    body = json_dict.get('body', "")
    doc = title + body
    doc = doc.replace('\n', ' ')
    doc = ' '.join(doc.split(' ')[0:100])

    sents = []

    if industry_codes and not topic_codes:
        sents.append(industry_code_text)
    if topic_codes and not industry_codes:
        sents.append(topic_code_text)
    if topic_codes and industry_codes:
        r = random.random()
        if r < 0.4:
            sents.append(topic_code_text)
        elif 0.4 <= r < 0.8:
            sents.append(industry_code_text)
        elif 0.8 <= r:
            sents.append(topic_code_text)
            sents.append(industry_code_text)

    if random.random() < 0.01 and country_codes:
        sents.append(country_code_text)

    sents.append(doc)

    random.shuffle(sents)
    for sent in sents:
        fout.write(sent.strip())
        fout.write("\n")
    fout.write("\n")
