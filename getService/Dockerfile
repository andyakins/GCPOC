FROM python:3.4.6-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /gcpoc
WORKDIR /gcpoc
ADD . /gcpoc/

RUN apk add --no-cache --virtual .build-deps  \
    gnupg \
    openssl \
    tar \
    xz \
	  bzip2-dev \
		coreutils \
		dpkg-dev dpkg \
		expat-dev \
		gcc \
		gdbm-dev \
		libc-dev \
		libffi-dev \
		linux-headers \
		make \
		ncurses-dev \
		openssl \
		openssl-dev \
		pax-utils \
		readline-dev \
		sqlite-dev \
		tcl-dev \
		tk \
		tk-dev \
		xz-dev \
		zlib-dev \
    && gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
    && pip install -r requirements.txt \
    && apk del .build-deps

EXPOSE 8080
CMD ["python3","app/getService.py"]
