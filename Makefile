.PHONY: all
all: test

.PHONY: test
test:
	pytest -v
