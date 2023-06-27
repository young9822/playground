# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/playwright/python:v1.34.0-jammy

WORKDIR /

# install the required python packages
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
