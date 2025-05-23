Create a file named .python-version in your repo to pin the exact Python version.

cd .
sudo apt install python3-tk
pyenv install 3.11.4
pyenv local 3.11.4



poetry init
poetry add django
poetry install --no-root


Task 1/1
django-admin startproject CVProject .
poetry run python manage.py migrate
poetry run python manage.py runserver


Task 1/2
poetry run python manage.py startapp main
poetry run python manage.py makemigrations
poetry run python manage.py migrate

Task 1/3
++ main/fixtures/cv.json
++ main/fixtures/projects.json
++ main/fixtures/skills.json
poetry run python manage.py loaddata main/fixtures/cv.json
poetry run python manage.py loaddata main/fixtures/projects.json
poetry run python manage.py loaddata main/fixtures/skills.json


Task 1/4
wire project urls.py with main urls.py
wire controllers to URLs 

Task 1/5
wire project urls.py with main urls.py
wire controllers to URLs 