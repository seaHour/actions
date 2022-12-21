export BUILD_MAJOR ?= 1
export BUILD_MINOR ?= 0
export BUILD_PATCH ?= 0
export BUILD_NUMBER ?= 3

build:
	(cd ./client/py; make build)
	(cd ./server; make build)

push:
	(cd ./server; make push)

unit-test:
	(cd ./client/py; make test)

int-test:
	(rm -rf venv; python3 -m venv venv; source venv/bin/activate; pip install pytest; \
	pip install client/py/dist/series-${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH}-${BUILD_NUMBER}-py3-none-any.whl; \
	pytest -v tests/integration/)
	@rm -rf venv

.PHONY: build push unit-test int-test
