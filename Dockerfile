# LobsterBot Dockerfile

FROM python:3.8-slim
LABEL maintainer="Romanov Alexey"

ENV PYTHONBUFFERED 1

COPY ./cfg /cfg
RUN python3 -m pip install -r /cfg/requirements.txt

RUN mkdir bot
COPY ./bot bot

RUN useradd -ms /bin/bash alexey
USER alexey
