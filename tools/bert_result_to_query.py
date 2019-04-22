import argparse
import json
import numpy as np

stopwords = set([line.strip() for line in open("/bos/usr0/zhuyund/query_reweight/stopwords2")] + ["information", "looking", "find"]) 
#stopwords = set([line.strip() for line in open("/bos/usr0/zhuyund/query_reweight/stopwords_robust04")] + ["information", "looking", "find"]) 

thred = 0
print("weights < {} will be filetered!".format(thred))
def subword_weight_to_word_weight(subword_weight_str):
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
    visited = set()
    for token, w in zip(fulltokens, weights):
        if '[' in token or token in stopwords or not token.isalnum():
            continue
        if w < thred or token in visited:
            continue
        fulltokens_filtered.append(token)
        weights_filtered.append(w)
        visited.add(token)
    #weights_filtered = np.exp(weights_filtered)/sum(np.exp(weights_filtered))
    if len(fulltokens_filtered) == 0:
        tmp = sorted(zip(weights, fulltokens), reverse=True)
        fulltokens_filtered = [t[1] for t in tmp[0:3]]
        weights_filtered = [t[0] for t in tmp[0:3]]
    return fulltokens_filtered, weights_filtered
         
def json_to_trec(dataset_file_path: str,
                 prediction_file_path: str,
                 output_file_path: str,
                 run_name: str="",
                 dataset_format: str = "trec",
                 max_depth: int = 1000) -> None:
    """

    :param dataset_file_path: json file
    :param prediction_file_path: json file of predictions
    :param run_name: run name
    :return: None
    """
    dataset = []
    predictions = []
    with open(dataset_file_path) as dataset_file:
        for line in dataset_file:
            dataset.append(json.loads(line))

    with open(prediction_file_path) as prediction_file:
        for line in prediction_file:
            fulltokens, weights = subword_weight_to_word_weight(line)
            predictions.append(' '.join(["{} {}".format(v, t) for v, t in zip(weights, fulltokens)]))
    
    assert len(dataset) == len(predictions)
    output_file = open(output_file_path, 'w') 
    for qjson, qw in zip(dataset, predictions):
        output_file.write(qjson["qid"] + '\t' +  qw + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset_file', help='Dataset json file')
    parser.add_argument('prediction_file', help='Prediction json File')
    parser.add_argument('output_file', help='Output File')
    args = parser.parse_args()

    json_to_trec(args.dataset_file,
                 args.prediction_file,
                 args.output_file)


