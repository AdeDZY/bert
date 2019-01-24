import spacy
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_doc_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load('en_core_web_sm')

    # Process whole documents
    with open(args.input_doc_file) as fin, open(args.output_file) as fout:
        text = fin.readline()
        doc = nlp(text)
        for sent in doc.sents:
            sent = sent.string.strip()
            fout.write(sent)
            fout.write('\n')
        fout.write('\n')


