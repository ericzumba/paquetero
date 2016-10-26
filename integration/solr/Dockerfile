FROM solr:6.2-alpine

RUN mkdir -p /opt/solr/server/solr/books 
COPY books/* /opt/solr/server/solr/books/

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["solr"]
