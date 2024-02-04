APP=$(shell basename -s .git $(shell git remote get-url origin))
REGISTRY ?= ghcr.io/yuandrk
VERSION=$(shell git describe --tags --abbrev=0)-$(shell git rev-parse --short HEAD)

image: 
	docker build . -t ${REGISTRY}/${APP}:${VERSION}

push:
	docker push ${REGISTRY}/${APP}:${VERSION}