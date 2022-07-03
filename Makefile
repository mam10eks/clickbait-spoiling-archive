IMAGE_VERSION=0.0.1

build-tira-git-docker:
	docker build -t webis/tira-git:${IMAGE_VERSION} .

publish-tira-git-docker:
	docker push webis/tira-git:${IMAGE_VERSION}

