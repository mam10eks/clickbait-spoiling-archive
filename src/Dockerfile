FROM ubuntu:22.10

RUN apt-get update \
	&& apt-get -y install git curl npm

COPY bash/tira-persist-software-result.sh \
	bash/tira-test-runner-is-trustworthy.sh \
	bash/tira-persist-evaluation-result.sh \
	bash/tira-specify-task-to-run.sh \
	/usr/local/bin/

