#!/bin/bash -e

if [ "$#" -ne 1 ]; then
    echo "Usage: pass the Token to this script."
    exit 1
fi


BASE_64_ENCODED_TOKEN=$(echo "${1}"|base64 -w 0)
BASE_64_ENCODED_USER=$(echo "tira-automation-bot"|base64 -w 0)
API_KEY_SECRET_DEFINITION="{\"apiVersion\": \"v1\", \"kind\": \"Secret\", \"metadata\": {\"name\": \"tira-git-credentials\"}, \"data\": {\"GITCREDENTIALPASSWORD\": \"${BASE_64_ENCODED_TOKEN}\", \"GITCREDENTIALUSERNAME\": \"${BASE_64_ENCODED_USER}\"}}"

echo "Create tira-git-credentials in kubernetes."
echo ${API_KEY_SECRET_DEFINITION}|kubectl -n kibi9872 apply -f -

