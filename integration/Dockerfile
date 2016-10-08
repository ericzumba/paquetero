FROM ericzumba/paquetero

RUN apk update 
RUN apk upgrade 
RUN apk add curl wget bash
RUN apk add build-base libffi-dev
RUN apk add ruby ruby-bundler ruby-dev

RUN rm -rf /var/cache/apk/*

RUN mkdir /usr/app 
WORKDIR /usr/app

COPY Gemfile /usr/app/ 
RUN bundle install
