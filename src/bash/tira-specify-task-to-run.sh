#!/bin/sh

JOB_DIR=$(find -iname job-to-execute.txt|head -1)
JOB_DIR=$(echo ${JOB_DIR}| awk -F 'job-to-execute' '{print $1}')
INPUT_DATA=$(echo ${JOB_DIR} |awk -F '/' '{print $2}')

if [[ ! -f "${JOB_DIR}/job-to-execute.txt" ]]; then
    echo "TIRA_IMAGE_TO_EXECUTE=ubuntu:16.04"
    exit 0
fi

echo "TIRA_INPUT_RUN=/mnt/ceph/tira/data/datasets/${INPUT_DATA}"
echo "TIRA_OUTPUT_DIR=${JOB_DIR}/output"

cat ${JOB_DIR}/job-to-execute.txt

