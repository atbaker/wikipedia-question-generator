# Dockerfile for wikipedia-question-generator

FROM python:3.4

MAINTAINER Andrew T. Baker <andrew.tork.baker@gmail.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# Install the textblob corpora before we copy the application source
# so Docker doesn't rebuild this step every time our source
# code changes
RUN python -m textblob.download_corpora

COPY . /usr/src/app
RUN pip install -e .

ENTRYPOINT ["wikitrivia"]
