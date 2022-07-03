FROM ubuntu:22.10

RUN apt-get update \
	&& apt-get -y install git curl npm

RUN git clone https://github.com/petemill/git-credential-envvar.git \
	&& npm install -g git-credential-envvar \
	&& git config --global credential.helper envvar

