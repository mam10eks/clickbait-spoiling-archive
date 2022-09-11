# Run evaluator

./tira-git run-evaluate --task_id clickbait-spoiling --vm_id princess-knight --run_id 2022-07-20-12-54-28 --dataset_id clickbait-spoiling-task-01-validation-dataset-2022-08-01 --transaction_id XXXX



confirm_run_evaluate: https://github.com/tira-io/tira/blob/7c0027533547d5c1304023b30ea52fd2b7deedab/host/src/tira_host/grpc_client.py#L83


# Brainstorming

- run-software
  - get all the metadata
  - copy current directory to tmp
  - create new branch
  - commit, push, 


- Evaluator image und das baseline image über github workflow bauen Clickbait spoiling



docker run \
	-v ${PWD}/src/python/tira-persist-software-result.py:/usr/local/bin/tira-persist-software-result.py \
	-v ${PWD}/src/:/tira/application/src/tira-git:ro \
	-v /mnt/ceph/tira/:/mnt/ceph/tira/:ro \
	-w /tira/application/src/tira-git \
	--rm -ti webis/tira-git:0.0.13

TIRA_TASK_ID=clickbait-spoiling TIRA_OUTPUT_DIR=. TIRA_VM_ID=princess-knight TIRA_DATASET_ID=clickbait-spoiling-task-01-validation-dataset-2022-08-01 TIRA_RUN_ID=2022-07-20-12-54-28 /usr/local/bin/tira-persist-software-result.py


# TODO:
# - Start evaluation: https://github.com/tira-io/tira/blob/30a79e39f13aee88daf77e5774ee50dac29e7242/application/src/tira/grpc_client.py#L131
# - Callback is finished: https://github.com/tira-io/tira/blob/30a79e39f13aee88daf77e5774ee50dac29e7242/application/src/tira/grpc/grpc_server.py#L106


# TIRA over Git: Evaluation-as-a-Service on Confidential Data With tira-git

The TIRA protocoll implemented in standard git workflows.

# Setup

Webis specific kubernetes installation in https://git.webis.de/code-generic/code-admin-knowledge-base/-/tree/master/services/tira/tira-gitlab

# Old

Create directory to execute, e.g., `scai-qrecc22-dataset-20220607-training/hal9000-default/2022-06-28-21-03-37/job-to-execute.txt`:

```
TIRA_IMAGE_TO_EXECUTE=ubuntu:16.04
TIRA_COMMAND_TO_EXECUTE=bash -c 'ls /mnt/ceph/tira/data/; ls /mnt/ceph/tira/data/runs/; ls /mnt/ceph/tira/data/datasets/test-datasets-truth/; echo \"\${TIRA_INPUT_RUN}\"; echo \"\${TIRA_OUTPUT_DIR}\"; touch dummy-result-01.jsonl; touch \${TIRA_OUTPUT_DIR}/dummy-result-02.jsonl'
```


