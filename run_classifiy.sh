export BERT_BASE_DIR=/ikea/bert/models/uncased_L-12_H-768_A-12

python run_classifier.py \
  --task_name=binglogtitlesnippet \
  --do_train=true \
  --do_eval=false \
  --do_predict=true \
  --data_dir=/ikea/pytorchKNRM/experiments/toy \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length=100 \
  --train_batch_size=32 \
  --learning_rate=2e-5 \
  --num_train_epochs=1.0 \
  --output_dir=/ikea/experiments/bing/titlesnippet-bert-640000/
