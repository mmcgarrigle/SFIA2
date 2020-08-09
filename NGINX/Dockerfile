FROM nginx:latest

WORKDIR /etc/nginx/

RUN apt update -y
RUN apt install openssl -y

# COPY ./reverse_proxy.conf /etc/nginx/conf.d/

RUN rm ./conf.d/default.conf
COPY . conf.d/