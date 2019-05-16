FROM python:alpine
LABEL Name=mail2telegram Version=0.0.1

EXPOSE 8025

WORKDIR /app
ADD . /app

RUN python3 -m pip install -r requirements.txt
CMD ["python3", "Mail2Telegram.py"]