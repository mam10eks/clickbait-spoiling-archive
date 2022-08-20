IMAGE_VERSION=0.0.34

build-tira-git-docker:
	cp -r /home/maik/workspace/tira/host/src/tira_host src
	docker build -t webis/tira-git:${IMAGE_VERSION} src

publish-tira-git-docker:
	docker push webis/tira-git:${IMAGE_VERSION}

dev-environment:
	docker run --rm -ti -w=/app-in-progress -v ${PWD}/src:/app-in-progress webis/tira-git:${IMAGE_VERSION}

