IMAGE_VERSION=0.0.11

build-tira-git-docker:
	docker build -t webis/tira-git:${IMAGE_VERSION} src

publish-tira-git-docker:
	docker push webis/tira-git:${IMAGE_VERSION}

dev-environment:
	docker run --rm -ti -w=/app-in-progress -v ${PWD}/src:/app-in-progress webis/tira-git:${IMAGE_VERSION}

