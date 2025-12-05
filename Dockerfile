FROM alpine

WORKDIR /app

COPY index.js /app/index.js

RUN apk add --update nodejs
RUN apk add --update npm
RUN npm install express
