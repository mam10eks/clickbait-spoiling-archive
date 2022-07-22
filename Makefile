IMAGE_VERSION=0.0.3

build-tira-git-docker:
	docker build -t webis/tira-git:${IMAGE_VERSION} src

publish-tira-git-docker:
	docker push webis/tira-git:${IMAGE_VERSION}

