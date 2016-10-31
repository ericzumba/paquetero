import tinys3
import click
import shutil
from os import environ 
import boto
from boto.s3.connection import S3Connection

aws_id = environ['AWS_ACCESS_KEY_ID']
aws_secret = environ['AWS_SECRET_ACCESS_KEY']

def s3(region):
  conn = S3Connection(aws_id, aws_secret) 
  
  def store(bucket_name, source):
    tar = '{0}.tar'.format(source)
    shutil.make_archive(source, 'tar', source)
    click.echo('Starting copy of {0} to s3 {1}'.format(tar, bucket_name))
    bucket = conn.get_bucket(bucket_name)
    key = boto.s3.key.Key(bucket, 'teste.tar')
    with open(tar, 'rb') as f:
      key.set_contents_from_file(f)
    click.echo('Copy completed')

  return dict(store=store) 
