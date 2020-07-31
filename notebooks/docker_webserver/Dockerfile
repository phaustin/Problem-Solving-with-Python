FROM nginx:alpine


ENV HOME=/static
RUN mkdir $HOME
COPY _build/html $HOME/
WORKDIR $HOME
COPY docker_webserver/nginx.conf /etc/nginx/nginx.conf
RUN ls -la /static/*

CMD ["nginx", "-g", "daemon off;"]

