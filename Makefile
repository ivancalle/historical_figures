.PHONY: clean
clean:
	@find . -name '__pycache__' -exec rm --force --recursive {} +
	@find . -name '.pytest_cache' -exec rm --force --recursive {} +
	@find . -name '.coverage' -exec rm --force --recursive {} +
	@find . -name '.eggs' -exec rm --force --recursive {} +
	@find . -name '*.egg-info' -exec rm --force --recursive {} +

.PHONY: requirements
requirements:
	pip-compile requirements/install.in
	pip-compile requirements/test.in

.PHONY: test
test: clean
	./setup.py pytest

.PHONY: wip
wip: clean
	./setup.py pytest -m wip

.PHONY: develop
develop: clean
	pip install -r requirements/test.txt -r requirements/install.txt -e .

.PHONY: build-docker
build-docker: clean
	docker build -t python-test .

.PHONY: run-docker
run-docker: clean
	docker run -it -p 8080:8080 python-test
