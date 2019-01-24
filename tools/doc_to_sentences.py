import spacy
import argparse
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_doc_file")
    parser.add_argument("output_file")
    parser.add_argument("--truncate_rate", '-r', type=float, default=0.02)
    args = parser.parse_args()

    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load('en_core_web_sm')

    # Process whole documents
    with open(args.input_doc_file) as fin, open(args.output_file) as fout:
        text = fin.readline()
        doc = nlp(text)
        for sent in doc.sents:
            sent = sent.string.strip()
            if random.random() < args.truncate_rate:
                words = sent.split(' ')
                t = random.randint(len(words)-1)
                sent = ' '.join(words[0:t])
            fout.write(sent)
            fout.write('\n')
        fout.write('\n')


