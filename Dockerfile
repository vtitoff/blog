# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .


RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN ["apt-get", "install", "-y", "curl"]
RUN ["apt-get", "install", "-y", "procps"]
RUN ["apt-get", "install", "-y", "nginx"]
RUN ["apt-get", "install", "-y", "bash-completion"]
RUN ["apt-get", "install", "-y", "sudo"]
RUN ["apt-get", "install", "-y", "nmap"]
RUN ["apt-get", "install", "-y", "htop"]
RUN ["apt-get", "install", "-y", "atop"]
