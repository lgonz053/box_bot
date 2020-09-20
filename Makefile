ENV = $(CURDIR)/env
PIP = $(ENV)/bin/pip
PYTHON = $(ENV)/bin/python

HONCHO_RUN = $(ENV)/bin/honcho -e .env run

$(ENV):
		python -m venv $(ENV)

deps: $(ENV)
		$(PIP) install -r requirements/base.txt

test-deps: deps
		$(PIP) install -r requirements/base.txt

start:
		$(HONCHO_RUN) python box_bot.py

format:
		$(ENV)/bin/black fantasy_sports/fantasy_basketball.py

check-format:
		$(ENV)/bin/black fantasy_sports/fantasy_basketball.py --check

test: test-deps
		$(PYTHON) -m unittest -v test/test_fantasy_basketball

clean:
		rm -rf $(ENV)