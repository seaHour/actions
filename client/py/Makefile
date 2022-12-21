export BUILD_MAJOR = 1
export BUILD_MINOR = 0
export BUILD_PATCH = 0
export BUILD_NUMBER = 1

all: build

build: clean
	pipenv sync --dev
	pipenv run python -m grpc_tools.protoc -I../../protos \
		--python_out=./src/series/ \
		--pyi_out=./src/series/ \
		--grpc_python_out=./src/series/ \
		../../protos/fib.proto
	pipenv run pipenv-setup sync
	pipenv run python setup.py sdist bdist_wheel --build-number ${BUILD_NUMBER}

clean:
	@rm -rf dist build src/*.egg-info

test:
	(rm -rf venv; python3 -m venv venv; source venv/bin/activate; pip install pytest; \
	pip install dist/series-${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH}-${BUILD_NUMBER}-py3-none-any.whl; \
	pytest -v tests/unit/)
	@rm -rf venv

.PHONY: all build clean test
