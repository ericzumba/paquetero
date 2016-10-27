FROM alpine:3.4 

RUN apk update 
RUN apk upgrade 
RUN apk add curl wget bash
RUN apk add build-base libffi-dev
RUN apk add ruby-bundler ruby-dev ruby-rdoc ruby-irb
RUN apk add docker

RUN rm -rf /var/cache/apk/*

RUN mkdir /usr/app 
WORKDIR /usr/app

COPY Gemfile Gemfile
RUN bundle install
