# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 
# This file specifies the steps to run and their order and allows running them.
# Type `make` for instructions. Type make <command> to execute a command.
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

.DEFAULT_GOAL := help

NAME=$(shell basename `pwd`)
SAMPLES=$(shell ls data)

help:  ## Display help and quit
	@echo Makefile for the $(NAME) project/package.
	@echo Available commands:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m\
		%s\n", $$1, $$2}'

requirements:  ## Install Python requirements
	{% if cookiecutter.management == "uv" -%} uv sync --extra dev {%- else -%} pip install -r requirements.txt{%- endif %}

backup_time:
	echo "Last backup: " `date` >> _backup_time
	chmod 700 _backup_time

_sync:
	rsync --copy-links --progress -r \
	. {{ cookiecutter.username }}@login:projects/$(NAME)

sync: _sync backup_time ## [dev] Sync data/code to SCU server

interactive: ## [dev] Start an interactive IPython session
	@echo "Starting an interaction IPython session"
	{% if cookiecutter.management == "uv" -%} uv run --extra dev {%- endif %} python -m IPython -i src/analysis.py


analysis:  ## Run all analysis steps
	@echo "Running analysis!"
	# # Main analysis steps
	{% if cookiecutter.management == "uv" -%} uv run {%- endif %} python -u src/analysis.py
	# {% if cookiecutter.management == "uv" -%} uv run {%- endif %}python -u src/analysis1.py
	# {% if cookiecutter.management == "uv" -%} uv run {%- endif %}python -u src/analysis2.py
	# ...

figures:  ## Produce figures in various formats
	cd figures; bash process.sh


.PHONY : help \
	requirements \
	transfer \
	process \
	sync \
	upload_data \
	download_data \
	analysis \
	figures
