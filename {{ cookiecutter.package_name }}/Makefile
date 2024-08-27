.PHONY: all lint test dev clean distclean

PYTHON ?= python

all: ;

lint:
	q2lint
	flake8

test: all
	py.test

dev: all
	pip install -e .

clean: distclean

distclean: ;
