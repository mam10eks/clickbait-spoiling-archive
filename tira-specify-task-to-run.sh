#!/bin/sh

echo "INPUT_RUN=dummy-input-run"
echo "OUTPUT_DIR=/tmp/tira-output-dir-tmp-07-22-2022/"
echo "IMAGE_TO_EXECUTE=ubuntu:16.04"
echo "COMMAND_TO_EXECUTE=bash -c 'ls /mnt/ceph/tira/data/; ls /mnt/ceph/tira/data/runs/; ls /mnt/ceph/tira/data/datasets/test-datasets-truth/; echo \"\${INPUT_RUN}\"; echo \"\${OUTPUT_DIR}\"; touch dummy-result-01.jsonl; touch \${OUTPUT_DIR}/dummy-result-02.jsonl'"

