#!/bin/sh

JOB_DIR=$(find -iname job-to-execute.txt|head -1)
JOB_DIR=$(echo ${JOB_DIR}| awk -F 'job-to-execute' '{print $1}')
INPUT_DATA=$(echo ${JOB_DIR} |awk -F '/' '{print $2}')

[[ ! -f "${JOB_DIR}/job-to-execute.txt" ]] && exit 0

echo "TIRA_INPUT_RUN=/mnt/ceph/tira/data/datasets/${INPUT_DATA}"
echo "TIRA_OUTPUT_DIR=${JOB_DIR}/output"

cat ${JOB_DIR}/job-to-execute.txt

