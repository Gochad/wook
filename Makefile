initdb:
	python manage.py migrate

updatedb:
	python manage.py makemigrations
	python manage.py migrate

setup:
	python3 -m pip install --user virtualenv
	python3 -m venv env

requirements:
	pip install -r requirements.txt

update:
	pip install --upgrade setuptools
	pip install --upgrade -r requirements.txt

test:
	python manage.py test --verbosity 2

server:
	python manage.py runserver

porterror:
	fuser -k 8000/tcp
	python manage.py runserver
