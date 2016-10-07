import boto
import boto.s3
from boto.s3.key import Key
import click
from os import environ 

aws_id = environ['AWS_ACCESS_KEY_ID']
aws_secret = environ['AWS_SECRET_ACCESS_KEY']

def s3(region):
  conn = boto.s3.connect_to_region(region, aws_access_key_id=aws_id, aws_secret_access_key=aws_secret, is_secure=True)
  
  def create_bucket(bucket_name):
    click.echo('creating s3 bucket {0}'.format(bucket_name))
    conn.create_bucket(bucket_name, location=region)
    click.echo('s3 bucket created')

  def store(bucket_name, source):
    create_bucket(bucket_name)
    click.echo('starting copy of {0} to s3'.format(source))

  return dict(store=store) 
