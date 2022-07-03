#!/bin/bash -e

SRC_DIR=${TIRA_EVALUATION_OUTPUT_DIR}
TARGET_DIR=/mnt/ceph/tira/data/runs/${TIRA_EVALUATION_OUTPUT_DIR}

DIR_TO_CHANGE=$(echo ${TIRA_OUTPUT_DIR}| awk -F '/output' '{print $1}')


if [ -f "${DIR_TO_CHANGE}/job-to-execute.txt" ]; then

    git remote set-url origin "https://$(cat /etc/tira-git-credentials/GITCREDENTIALUSERNAME):$(cat /etc/tira-git-credentials/GITCREDENTIALPASSWORD)@${CI_SERVER_HOST}/${CI_PROJECT_PATH}.git"

    git remote get-url origin

    git config user.email "tira-automation@tira.io"
    git config user.name "TIRA Automation"

    mv ${DIR_TO_CHANGE}/job-to-execute.txt ${DIR_TO_CHANGE}/executed-job.txt
    git rm ${DIR_TO_CHANGE}/job-to-execute.txt
    git add ${DIR_TO_CHANGE}/executed-job.txt
    git commit -m "TIRA-Automation: software was executed and evaluated." || echo "No changes to commit"

    git push -o ci.skip origin HEAD:$CI_COMMIT_BRANCH
else
    echo "The file ${DIR_TO_CHANGE}/job-to-execute.txt does not exist, I cant change it."
fi

if [ -f "$TARGET_DIR" ]; then
    echo "$TARGET_DIR exists already. Exit."
    exit 0
fi

if [ -d "$TARGET_DIR" ]; then
    echo "$TARGET_DIR exists already. Exit."
    exit 0
fi

echo "mkdir -p $(echo ${TARGET_DIR}| awk -F '/output' '{print $1}')"
mkdir -p "$(echo ${TARGET_DIR}| awk -F '/output' '{print $1}')"

echo "cp -r ${SRC_DIR} ${TARGET_DIR}"
cp -r ${SRC_DIR} ${TARGET_DIR}

env|grep 'TIRA' >> task.env

