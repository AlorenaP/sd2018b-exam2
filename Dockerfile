FROM ubuntu:16.04

RUN apt-get update -y && apt-get install postgresql -y

EXPOSE 5432
CMD postgresql -m http.server 5432
