# You should symlink this file to project root `sudo ln -s path-to-this-file`
.PHONY: reload test syncdb migrate

ROOT_DIR = `pwd`
MANAGE=`pwd`/tic_tac/manage.py
SETTINGS='core.settings.development'

update:
	@git stash
	@git pull
	@make req
	python $(MANAGE) collectstatic --noinput
	python $(MANAGE) migrate
	touch reload_project

reload:
	@make collectstatic
	touch reload_project

run:
	DJANGO_SETTINGS_MODULE=$(SETTINGS) python $(MANAGE) runserver 0.0.0.0:8880

_makemigrations:
	DJANGO_SETTINGS_MODULE=$(SETTINGS) python $(MANAGE) makemigrations

migrate:
	DJANGO_SETTINGS_MODULE=$(SETTINGS) python $(MANAGE) migrate

collectstatic:
	DJANGO_SETTINGS_MODULE=$(SETTINGS) python $(MANAGE) collectstatic --noinput

req:
	@echo "Installing requirements"
	@pip install --exists-action=s -r requirements.txt

shell:
	DJANGO_SETTINGS_MODULE=$(SETTINGS) python $(MANAGE) shell
