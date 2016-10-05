#! /bin/bash
curl -v -X GET "http://$1:8983/solr/$2/replication?command=restore&location=$3/$2&name=le-dump"

