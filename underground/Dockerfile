FROM python:3.9.6-alpine

WORKDIR /usr/src/underground
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
# RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# update DB migrations
RUN python manage.py makemigrations
RUN python manage.py migrate