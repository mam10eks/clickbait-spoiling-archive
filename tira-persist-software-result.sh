#!/bin/bash -e

SRC_DIR=${TIRA_OUTPUT_DIR}
TARGET_DIR=/mnt/ceph/tira/data/runs/${TIRA_OUTPUT_DIR}

TIRA_EVALUATION_OUTPUT_DIR="${TARGET_DIR}/../$(date +'%Y-%m-%d-%I-%M-%S')/output"
echo "TIRA_EVALUATION_INPUT_DIR=${TARGET_DIR}" >> ${JOB_DIR}/job-to-execute.txt
echo "TIRA_EVALUATION_OUTPUT_DIR=${TIRA_EVALUATION_OUTPUT_DIR}" >> ${JOB_DIR}/job-to-execute.txt

echo "TIRA_EVALUATION_INPUT_DIR=${TARGET_DIR}" >> task.env
echo "TIRA_EVALUATION_OUTPUT_DIR=${TIRA_EVALUATION_OUTPUT_DIR}" >> task.env

echo "TIRA_EVALUATION_IMAGE_TO_EXECUTE=ubuntu:18.04" >> ${JOB_DIR}/job-to-execute.txt
echo "TIRA_EVALUATION_COMMAND_TO_EXECUTE=echo '{\"key\":\"value\"}' >> \${TIRA_ECALUATION_OUTPUT_DIR}/evaluation-results.json" >> ${JOB_DIR}/job-to-execute.txt

echo "TIRA_EVALUATION_IMAGE_TO_EXECUTE=ubuntu:18.04" >> task.env
echo "TIRA_EVALUATION_COMMAND_TO_EXECUTE=echo '{\"key\":\"value\"}' >> \${TIRA_ECALUATION_OUTPUT_DIR}/evaluation-results.json" >> task.env

if [ -f "$TARGET_DIR" ]; then
    echo "$TARGET_DIR exists already. Exit."
    exit 0
fi

if [ -d "$TARGET_DIR" ]; then
    echo "$TARGET_DIR exists already. Exit."
    exit 0
fi

mkdir -p ${TARGET_DIR}/..
cp -r ${SRC_DIR} ${TARGET_DIR}
env|grep 'TIRA' >> task.env

