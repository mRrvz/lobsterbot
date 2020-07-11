# LobsterBot Dockerfile

FROM python:3.8-slim
LABEL maintainer="Romanov Alexey"

ENV PYTHONBUFFERED 1

COPY ./cfg /cfg
RUN python3 -m pip install -r /cfg/requirements.txt

RUN mkdir bot
RUN mkdir data

COPY ./bot bot
COPY ./data data

RUN useradd -ms /bin/bash alexey
USER alexey
