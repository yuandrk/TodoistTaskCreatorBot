APP=$(shell basename -s .git $(shell git remote get-url origin))
REGISTRY ?= ghcr.io/yuandrk
VERSION=$(shell git describe --tags --abbrev=0)-$(shell git rev-parse --short HEAD)
ARCH ?= amd64


image: 
	docker build . -t ${REGISTRY}/${APP}:${VERSION}-${ARCH}


arm:
	docker build --build-arg ARCH=arm64v8 . -t ${REGISTRY}/${APP}:${VERSION}-arm64

push:
	docker push ${REGISTRY}/${APP}:${VERSION}-${ARCH}

