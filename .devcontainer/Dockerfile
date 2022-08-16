FROM python:3.6-slim

ENV GIT_DISCOVERY_ACROSS_FILESYSTEM=1
RUN apt-get update
RUN apt-get install git -y

RUN mkdir /root/hello-anago
WORKDIR /root/hello-anago
ADD requirements.txt /root/hello-anago/
RUN pip install -r requirements.txt