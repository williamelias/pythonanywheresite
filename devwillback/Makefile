#TODO fix this
venv:
	source .venv/bin/activate

migrate:
	python3 manage.py migrate

makmigrations:
	python3 manage.py makemigrations

findstatic:
	python manage.py findstatic ${path}

start:
	python3 manage.py runserver

static:
	python3 manage.py collectstatic

clean_git:
	git rm --cached -r .