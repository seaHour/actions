BUILD_MAJOR ?= 1
BUILD_MINOR ?= 0
BUILD_PATCH ?= 0
BUILD_NUMBER ?= 1

DOCKER_REGISTRY ?= docker.io
DOCKER_REPO ?= charliehou/xz

all: build

build: clean
	pipenv sync --dev
	pipenv run python -m grpc_tools.protoc -I../protos \
		--python_out=./app/ \
		--pyi_out=./app/ \
		--grpc_python_out=./app/ \
		../protos/fib.proto
	docker build -t ${DOCKER_REGISTRY}/${DOCKER_REPO}:${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH}-${BUILD_NUMBER} \
		-t ${DOCKER_REGISTRY}/${DOCKER_REPO}:latest \
		.

push:
	docker push ${DOCKER_REGISTRY}/${DOCKER_REPO}:${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH}-${BUILD_NUMBER}
	docker push ${DOCKER_REGISTRY}/${DOCKER_REPO}:latest

clean:
	@rm -rf dist build src/*.egg-info

.PHONY: all build push clean
