import json
import sys
import random

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

for line in fin:
    json_dict = json.loads(line)
    codes = json_dict["codes"].values()

    country_codes = codes.get("bip:countries:1.0", [])
    topic_codes = codes.get("bip:topics:1.0", [])
    industry_codes = codes.get("bip:industries:1.0", [])

    country_code_text = "CODECOUNTRY " + '/ '.join(["RCV" + t for t in country_codes])
    topic_code_text = "CODETOPIC " + '/ '.join(["RCV" + t for t in random.shuffle(topic_codes)])
    industry_code_text = "CODEINDUSTRY " + '/ '.join(["RCV" + t for t in random.shuffle(industry_codes)])

    title = json_dict.get('headline', "")
    if not title:
        title = ""
    body = json_dict.get('body', "")
    doc = title + body
    doc = doc.replace('\n', ' ')
    doc = ' '.join(doc.split(' ')[0:200])

    sents = []

    if industry_codes and not topic_codes:
        sents.append(industry_codes)
    if topic_codes and not industry_codes:
        sents.append(topic_code_text)
    elif topic_codes and industry_codes:
        r = random.random()
        if r < 0.4:
            sents.append(topic_codes)
        elif 0.4 <= r < 0.8:
            sents.append(industry_codes)
        elif 0.8 <= r:
            sents.append(topic_codes)
            sents.append(industry_codes)

    if random.random() < 0.01 and country_codes:
        sents.append(country_code_text)

    random.shuffle(sents)
    for sent in sents:
        fout.write(sent.strip())
        fout.write("\n")
    fout.write("\n")
