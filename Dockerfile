FROM python:2.7-alpine

RUN \
  mkdir -p /aws && \
  apk -Uuv add groff less && \
  pip install awscli && \
  pip install click && \
  apk --purge -v del py-pip && \
  rm /var/cache/apk/*

WORKDIR /project
COPY run.py /project/run.py

ENTRYPOINT ["python", "/project/run.py"]
