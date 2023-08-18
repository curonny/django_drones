# Docker run

    -docker-compose up --build

# Run solution without docker

## Create .env file with params

    -DB_NAME=dron
    -DB_USER=django
    -DB_PASSWORD=django

## Create db with that name and run

    -python manage.py makemigrations
    -python manage.py migrate
    -Create superuser : python manage.py createsuperuser

#### Export environment

    -export DJANGO_SETTINGS_MODULE=dron_project.settings

### Start periodic task run:

    -celery -A dron_project beat -l info
