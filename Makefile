MANAGE = python core/manage.py

run:
	$(MANAGE) runserver

freeze:
	pip freeze > requirements.txt

make-migrate:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate