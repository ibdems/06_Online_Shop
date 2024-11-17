.PHONY: install_dev
install_dev:
	python -m pip install -r requirements.txt
	pre-commit install

.PHONY: runserver
runserver:
	python manage.py runserver 8006


.PHONY: makemigrations
makemigrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: superuser
superuser:
	python manage createsuperuser


