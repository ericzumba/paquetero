FROM python:2.7-alpine

RUN \
  mkdir -p /aws && \
  apk -Uuv add groff less && \
  pip install boto click requests && \
  apk --purge -v del py-pip && \
  rm /var/cache/apk/*

WORKDIR /project
COPY *.py /project/

ENTRYPOINT ["python", "/project/run.py"]
