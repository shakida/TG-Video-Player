FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN mkdir /shakida/
WORKDIR /shakida/
COPY . /shakida/
RUN pip3 install -U -r requirements.txt
CMD python3 main.py
