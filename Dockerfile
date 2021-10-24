FROM python:latest

RUN apt update && apt upgrade -y

RUN cd /
RUN git clone https://github.com/shakida/TG-Video-Player.git

RUN cd VP
WORKDIR /VP

RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt

CMD python3 -m main
