FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 python3-pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN mkdir app

WORKDIR /opt/app
COPY . /opt/app
ENTRYPOINT FLASK_APP=/opt/app/app.py flask run --host 0.0.0.0 
    