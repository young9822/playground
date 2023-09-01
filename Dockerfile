# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/playwright/python:latest

# install the required python packages
WORKDIR /
COPY requirements.txt requirements.txt
COPY pytest.ini pytest.ini
RUN pip install -r requirements.txt
RUN python -m playwright install --with-deps