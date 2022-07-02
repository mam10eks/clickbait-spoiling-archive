#!/bin/sh

echo "TIRA_INPUT_RUN=dummy-input-run"
echo "TIRA_OUTPUT_DIR=/tmp/tira-output-dir-tmp-07-22-2022/"
echo "TIRA_IMAGE_TO_EXECUTE=ubuntu:16.04"
echo "TIRA_COMMAND_TO_EXECUTE=bash -c 'ls /mnt/ceph/tira/data/; ls /mnt/ceph/tira/data/runs/; ls /mnt/ceph/tira/data/datasets/test-datasets-truth/; echo \"\${TIRA_INPUT_RUN}\"; echo \"\${TIRA_OUTPUT_DIR}\"; touch dummy-result-01.jsonl; touch \${TIRA_OUTPUT_DIR}/dummy-result-02.jsonl'"

