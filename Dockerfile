FROM python:3.7
RUN apt-get update && apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 4000

ENTRYPOINT  ["python"]

CMD ["app.py"]