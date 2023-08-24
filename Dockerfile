FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE dron_project.settings

WORKDIR /app
COPY . .


RUN pip install -r requirements.txt
#
## Run migrations and collect static files
#RUN python manage.py makemigrations
#RUN python manage.py migrate

# Expose the port that the application will run on
EXPOSE 8000

# Run the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

