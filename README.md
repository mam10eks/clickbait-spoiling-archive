# Run evaluator

./tira-git run-evaluate --task_id clickbait-spoiling --vm_id princess-knight --run_id 2022-07-20-12-54-28 --dataset_id clickbait-spoiling-task-01-validation-dataset-2022-08-01


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

https://docs.gitlab.com/runner/install/kubernetes.html

For some tests, I use my own namespace: `kibi9872`.
Disable shared group runners for the project, we want that everything runs via our own runners.

Create service account for TIRA, used by the runner to create pods.

```
kubectl -n kibi9872 apply -f k8s-tira-service-account.yml
kubectl -n kibi9872 apply -f k8s-no-internet-network-policy.yml
```

Create the `tira-git-credentials` secret so that the corresponding pods can have access to the git secrets (create a git token for the group).

```
./k8s-deploy-tira-git-credentials-as-secret.sh <TOKEN-FOR-THE-GROUP>
```


To start from scratch, run:

```
helm uninstall --namespace kibi9872 gitlab-runner-tira-evaluators; \
helm uninstall --namespace kibi9872 gitlab-runner-tira-user-software; \
helm uninstall --namespace kibi9872 gitlab-runner-tira-copy
```

Then, install the runners:

```
helm install --namespace kibi9872 gitlab-runner-tira-evaluators -f ./src/k8s/k8s-gitlab-runner-tira-evaluators-config.yml gitlab/gitlab-runner; \
helm install --namespace kibi9872 gitlab-runner-tira-user-software -f ./src/k8s/k8s-gitlab-runner-tira-user-software-config.yml gitlab/gitlab-runner; \
helm install --namespace kibi9872 gitlab-runner-tira-copy -f ./src/k8s/k8s-gitlab-runner-tira-copy-config.yml gitlab/gitlab-runner
```

After this command, the runner should be available in  "Settings" -> "CI/CD Settings" -> "Runners" -> "Specific runners" section.


Create directory to execute, e.g., `scai-qrecc22-dataset-20220607-training/hal9000-default/2022-06-28-21-03-37/job-to-execute.txt`:

```
TIRA_IMAGE_TO_EXECUTE=ubuntu:16.04
TIRA_COMMAND_TO_EXECUTE=bash -c 'ls /mnt/ceph/tira/data/; ls /mnt/ceph/tira/data/runs/; ls /mnt/ceph/tira/data/datasets/test-datasets-truth/; echo \"\${TIRA_INPUT_RUN}\"; echo \"\${TIRA_OUTPUT_DIR}\"; touch dummy-result-01.jsonl; touch \${TIRA_OUTPUT_DIR}/dummy-result-02.jsonl'
```


