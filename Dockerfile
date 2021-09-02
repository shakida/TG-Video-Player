FROM python:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y

RUN cd /
RUN git clone https://github/shakida/TG-Video-Player.git

RUN cd VP
WORKDIR /VP

RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt

CMD python3 -m handel
