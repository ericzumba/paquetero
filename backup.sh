#! /bin/bash
HOST=$1
CORE=$2
LOCATION=$3
SSH_KEY=$4
SSH_USER=$5
CORE_DUMP=$LOCATION/$CORE

AWS_BIN="docker run -i --entrypoint aws ericzumba/awscli -c help"

curl -X GET "http://$HOST:8983/solr/$CORE/replication?command=backup&location=$CORE_DUMP"
ssh -i $SSH_KEY $SSH_USER@$HOST "$AWS_BIN"
