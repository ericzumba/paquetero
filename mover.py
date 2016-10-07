import boto
import boto.s3
import click
from os import environ 

aws_id = environ['AWS_ACCESS_KEY_ID']
aws_secret = environ['AWS_SECRET_ACCESS_KEY']

def s3(region):
  conn = boto.connect_s3(aws_id, aws_secret)
  def store(source):
    click.echo('starting copy of {0} to s3'.format(source))

  return dict(store=store) 
