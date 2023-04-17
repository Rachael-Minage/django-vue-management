#Using the official Python base image
FROM python:3.8-alpine
#Setting a current working directory within the container
#This is the default location for all subsequent instructions in the Dockerfile
WORKDIR /app
#Establishing dependancy management
COPY requirements.txt /app/requirements.txt
RUN apk add --no-cache gcc musl-dev libffi-dev mariadb-dev
RUN pip install -r /app/requirements.txt
#Getting source code and other files from the local project directory to the containers
COPY . /app
#Exposing the port that the django application will run on
EXPOSE 8000
#Defining the commands to be executed when the container is started
RUN pip install uwsgi
CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "vue.wsgi:application", "--master", "--processes", "4", "--threads", "2"]
