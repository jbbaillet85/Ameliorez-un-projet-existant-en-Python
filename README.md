[![wakatime](https://wakatime.com/badge/user/648b0556-0c0e-4e9d-b952-2bea950dabe6/project/3d7e5dd0-2dbf-4201-9c23-318c0a21e0c9.svg)](https://wakatime.com/badge/user/648b0556-0c0e-4e9d-b952-2bea950dabe6/project/3d7e5dd0-2dbf-4201-9c23-318c0a21e0c9)
[![Build Status](https://app.travis-ci.com/jbbaillet85/Ameliorez-un-projet-existant-en-Python.svg?branch=main)](https://app.travis-ci.com/jbbaillet85/Ameliorez-un-projet-existant-en-Python)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7535f0577956403cbb2c9f4ea6f9a134)](https://www.codacy.com/gh/jbbaillet85/Ameliorez-un-projet-existant-en-Python/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jbbaillet85/Ameliorez-un-projet-existant-en-Python&amp;utm_campaign=Badge_Grade)
[![jbbaillet85](https://circleci.com/gh/jbbaillet85/Ameliorez-un-projet-existant-en-Python.svg?style=svg)](https://app.circleci.com/pipelines/github/jbbaillet85/Ameliorez-un-projet-existant-en-Python)

# Ameliorez_un_projet_existant_en_Python

[Tableau Trello de gestion agile](https://trello.com/b/Cl1dNvgv/am%C3%A9liorer-en-projet-existant-en-python)

## Environnement de developpement

### Pré-requis

- Python 3.10
- Django

### Commandes
#### Création de l'environnement virtuel
```
pip install --user pipenv
mkdir .venv
touch .env
pipenv --python 3.10
```
#### Installation des dépendances
```
pipenv install
```
#### Commandes Procédure
```
pipenv run python manage.py runserver
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py collectstatic
pipenv run python manage.py insertCategory
pipenv run python manage.py insertProduct
pipenv run pytest
pipenv run pip freeze > requirements.txt
```
# site en production:
https://purebeurre35.herokuapp.com