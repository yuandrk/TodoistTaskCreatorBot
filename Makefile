.ONESHELL:

DATE_ID := $(shell date +"%y.%m.%d")

.DEFAULT_GOAL := help

# Variables 
REGISTRY ?= ghcr.io/yuandrk
DOCKER_IMAGE = $(shell basename $(CURDIR))-$(shell git describe --tags --always)-$(ARCH)
APP=$(shell basename -s .git $(shell git remote get-url origin))
VENV := $(shell basename -s .git $(shell git remote get-url origin)_venv)
VERSION=$(shell git describe --tags --abbrev=0)-$(shell git rev-parse --short HEAD)
TARGETOS ?= linux
TARGETARCH ?= arm64
PYTHON := $(shell which python3)


setup-system: 
	@sudo apt-get update && sudo apt-get install -y python3-venv python3-pi

test: 
	@echo Using Python at: $(PYTHON)

build-image: 
	@docker build . --build-arg ARCH=$(TARGETARCH) -t $(REGISTRY)/$(APP):$(VERSION)-$(TARGETARCH)

push-image:
	@docker push $(REGISTRY)/$(APP):$(VERSION)-$(TARGETARCH)

# Ensures the virtual environment is only created if it doesn't exist or requirements.txt is updated
$(VENV)/.venv_stamp: requirements.txt
	@python3 -m venv $(VENV)
	@. $(VENV)/bin/activate && $(PIP) install -r requirements.txt
	@touch $(VENV)/.venv_stamp

# The .PHONY directive tells Make that 'venv' isn't a file to check for updates
.PHONY: venv
venv:
	@python3 -m venv $(VENV)
	@$(VENV)/bin/pip install -r requirements.txt
	@. $(VENV)/bin/activate

# The 'run' target depends on 'venv', ensuring the virtual environment is ready
run: venv
	@. $(VENV)/bin/activate && $(PYTHON) src/main.py

