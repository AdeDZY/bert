#!/bin/bash
#SBATCH -n 2 # Number of cores
#SBATCH -N 1 # Ensure that all cores are on one machine
#SBATCH --mem=8192
#SBATCH --gres=gpu:4
#SBATCH --time=24:00:00

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/cuda/10.0/lib64:/opt/cudnn/cuda-10.0/7.3/cuda/lib64
source activate /bos/usr0/zhuyund/tf_env 

export BERT_BASE_DIR=/bos/usr0/zhuyund/uncased_L-12_H-768_A-12

python run_pretraining.py \
  --input_file=/bos/usr0/zhuyund/robust04_corpus/pretrain/small/pretrain.tfrecord_* \
  --output_dir=/bos/usr0/zhuyund/robust04_corpus/bert_models/small-100K \
  --do_train=True \
  --do_eval=True \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --train_batch_size=32 \
  --max_seq_length=128 \
  --max_predictions_per_seq=20 \
  --num_train_steps=100000 \
  --num_warmup_steps=10 \
  --learning_rate=2e-5
