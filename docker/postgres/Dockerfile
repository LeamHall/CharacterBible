# postgres docker file
FROM postgres:16.1-alpine3.18

RUN apk add shadow && /usr/sbin/groupadd -g 500 syseng 
RUN /usr/sbin/usermod -u 1000 -g 500 postgres

