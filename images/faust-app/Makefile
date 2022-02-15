SHELL := /bin/bash
REG := quay.io
ORG := lrossett
NAME := faust-app
TAG := latest
IMAGE := ${REG}/${ORG}/${NAME}:${TAG}
CRI := docker

build:
	@${CRI} build -t ${IMAGE} .

debug: build
	@${CRI} run -it --entrypoint /bin/bash ${IMAGE}

run: build
	@${CRI} run -it ${IMAGE}

push: build
	@${CRI} push ${IMAGE}
