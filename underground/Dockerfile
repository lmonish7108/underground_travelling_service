FROM python

WORKDIR /usr/src/underground

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .
RUN cd ./underground
RUN pip install -r requirements.txt
# update DB migrations