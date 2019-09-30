ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

VENV_DIR = $(ROOT_DIR)/venv

CMD_PYTHON = $(VENV_DIR)/bin/python
CMD_PIP = $(VENV_DIR)/bin/pip
CMD_PYTEST = $(VENV_DIR)/bin/pytest

help: _help_

_help_:
	@echo make run - run development environment
	@echo make deps - install all project deps
	@echo make test - run application tests

deps:
	if [ ! -d "$(VENV_DIR)" ] ; then \
		python3 -m venv venv ; fi

	$(CMD_PIP) install -r requirements.txt

run:
	ln -sf ./configs/local.py ./config.py

	# install deps
	make deps

	$(CMD_PYTHON) app.py

test:
	ln -sf ./configs/test.py ./config.py

	$(CMD_PYTEST) -s

