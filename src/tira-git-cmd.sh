#!/usr/bin/bash

docker run \
	-v ${PWD}:/repo \
	-v /mnt/ceph/tira/:/mnt/ceph/tira/:ro \
	-v ${HOME}/.ssh/id_rsa:${HOME}/.ssh/id_rsa:ro \
	-v ${HOME}/.ssh/id_rsa.pub:${HOME}/.ssh/id_rsa.pub:ro \
	-v ${HOME}/.gitconfig:${HOME}/.gitconfig:ro \
	-v /etc/passwd:/etc/passwd:ro \
	-w /repo \
	-u $(id -u ${USER}):$(id -g ${USER}) \
	--rm -ti webis/tira-git:0.0.11 ${@}




