FROM python:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y

RUN cd /
RUN wget -q https://github.com/shakida/TG-Video-Player/archive/main.tar.gz && \
    tar xf main.tar.gz && rm main.tar.gz

WORKDIR /TG-Video-Player-main

RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt

CMD python3 -m handel
