FROM ericzumba/paquetero

RUN apk update 
RUN apk upgrade 
RUN apk add curl wget bash
RUN apk add build-base libffi-dev
RUN apk add ruby-bundler ruby-dev ruby-rdoc ruby-irb

RUN rm -rf /var/cache/apk/*

RUN gem install cucumber

RUN mkdir /usr/app 
WORKDIR /usr/app
