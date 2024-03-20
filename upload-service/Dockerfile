FROM python:3.8-slim-buster

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV PYTHONPATH=$PYTHONPATH:.

CMD ["python3", "api/v1/app.py"]