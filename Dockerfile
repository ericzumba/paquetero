FROM alpine:latest

RUN \
  mkdir -p /aws && \
  apk -Uuv add groff less python py-pip && \
  pip install awscli && \
  apk --purge -v del py-pip && \
  rm /var/cache/apk/*

COPY run.py run.py

WORKDIR /project
ENTRYPOINT ["python /project/run.py"]
