.PHONY: test
test:
	pip install -r requirements-dev.txt
	pytest -q
