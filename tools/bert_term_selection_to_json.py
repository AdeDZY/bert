import argparse
import json
import numpy as np


def subword_weight_to_word_weight(subword_weight_str, thred):
    fulltokens = []
    weights = []
    for item in subword_weight_str.split('\t'):
        token, weight = item.split(' ')
        weight = float(weight)
        token = token.strip()
        if token.startswith('##'):
            fulltokens[-1] += token[2:]
        else:
            fulltokens.append(token)
            weights.append(weight)
    assert len(fulltokens) == len(weights)
    fulltokens_filtered, weights_filtered = [], []
    selected_tokens = [] 
    for token, w in zip(fulltokens, weights):
        if token == '[CLS]' or token == '[SEP]':
            continue
        if w < thred:
            continue
        selected_tokens.append(token)
    return set(selected_tokens)
         
def json_to_trec(dataset_file_path,
                 prediction_file_path,
                 output_file_path,
                 thred):
    """

    :param dataset_file_path: json file
    :param prediction_file_path: json file of predictions
    :return: None
    """
    dataset = []
    predictions = []
    with open(dataset_file_path) as dataset_file, open(prediction_file_path) as prediction_file, open(output_file_path, 'w') as output_file:
        n, e, a = 0, 0, 0
        for l1, l2 in zip(dataset_file, prediction_file):
            n += 1
            if n % 10000 == 0: 
                print("processe {} lines, {} empty, avg len: {}".format(n, e, float(a)/(n - e)))
            did = l1.split('\t')[0]
            selected_tokens = subword_weight_to_word_weight(l2, thred)
            if not selected_tokens: 
                e += 1
                continue 
            dtext = ' '.join(selected_tokens)
            output_file.write(did + '\t' + dtext.strip()  + '\n')
            a += len(selected_tokens)

        assert dataset_file.readline() is None
        assert prediction_file.readline() is None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset_file', help='Dataset json file')
    parser.add_argument('prediction_file', help='Prediction json File')
    parser.add_argument('output_file', help='Output File')
    parser.add_argument('thred', type=float, help='Thred > 0')
    args = parser.parse_args()

    assert args.thred > 0

    json_to_trec(args.dataset_file,
                 args.prediction_file,
                 args.output_file, 
                 args.thred)

