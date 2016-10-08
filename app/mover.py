import tinys3
import click
import shutil
from os import environ 

aws_id = environ['AWS_ACCESS_KEY_ID']
aws_secret = environ['AWS_SECRET_ACCESS_KEY']

def s3(region):
  conn = tinys3.Connection(aws_id, aws_secret, tls=True, endpoint='s3-{0}.amazonaws.com'.format(region))
  
  def store(bucket_name, source):
    tar = '{0}.tar'.format(source)
    shutil.make_archive(source, 'tar', source)
    click.echo('starting copy of {0} to s3 {1}'.format(tar, bucket_name))
    conn.upload(tar, open(tar, 'rb'), bucket_name)
    click.echo('copy completed')

  return dict(store=store) 
