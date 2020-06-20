FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

# # create root directory for our project in the container
WORKDIR /CC-PROJECT

COPY ./requirements.txt ./

RUN apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev jpeg-dev zlib-dev\
    && pip install --no-cache-dir -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && apk --purge del .build-deps  

# # Copy the current directory contents into the container at /backend
ADD . ./