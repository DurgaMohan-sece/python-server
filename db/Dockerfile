FROM mysql:5.7.15

MAINTAINER me

ENV MYSQL_DATABASE=test \
    MYSQL_ROOT_PASSWORD=dbpassword

ADD schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306