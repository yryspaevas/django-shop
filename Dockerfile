FROM ubuntu

WORKDIR /

COPY . .

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install wheel gunicorn
RUN pip install -r req.txt


ENV SECRET_KEY=0n15ke2^4k26*!zfe&^^v@&a3rr8%7f901g80zm1tc4#d0a6e(
ENV DB_NAME=railway
ENV DB_USER=postgres
ENV DB_PASSWORD=2O6Q6tLWUc9KfCEsI5Dy
ENV DB_HOST=containers-us-west-79.railway.app
ENV DB_PORT=5707
ENV DEBUG=1
ENV ALLOWED_HOSTS=127.0.0.1,


CMD gunicorn --bind 0.0.0.0:8000 config.wsgi:application
