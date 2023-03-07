FROM python

WORKDIR /usr/src/underground
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .
RUN cd ./underground
RUN pip install -r requirements.txt
# update DB migrations
RUN python manage.py makemigrations
RUN python manage.py migrate