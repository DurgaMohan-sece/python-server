# A simple Flask app container.
FROM python:3.5
LABEL maintainer="me"

# Place app in container.
COPY . /opt/www
WORKDIR /opt/www

# Install dependencies.
RUN pip3 install -r requirements.txt

EXPOSE 80
CMD python server.py
