#!/bin/bash
#SBATCH -n 1 # Number of cores
#SBATCH -N 1 # Ensure that all cores are on one machine
#SBATCH --mem=4096
#SBATCH --gres=gpu:1

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/cuda/10.0/lib64:/opt/cudnn/cuda-10.0/7.3/cuda/lib64
source activate /bos/usr0/zhuyund/tf_env 

export BERT_BASE_DIR=/bos/usr0/zhuyund/uncased_L-12_H-768_A-12
export FOLD=1

python run_term_reg.py \
  --task_name=query \
  --do_train=true \
  --do_eval=true \
  --do_predict=true \
  --data_dir=/bos/usr0/zhuyund/query_reweight/clueweb09/bert_reg/query_desc_cv/ \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length=100 \
  --train_batch_size=16 \
  --learning_rate=2e-5 \
  --num_train_epochs=10.0 \
  --fold=$FOLD \
  --recall_field=body,title \
  --output_dir=/bos/usr0/zhuyund/query_reweight/experiments/clueweb09/query_desc/bodytitle_fold${FOLD}
