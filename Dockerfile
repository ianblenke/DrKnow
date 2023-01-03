FROM python:3.10-slim

WORKDIR /drknow

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

CMD python DrKnow.py

