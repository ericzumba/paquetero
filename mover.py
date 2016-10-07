import click
import boto
import boto.s3

def copy_to_s3(source):
  click.echo('starting copy of {0} to s3'.format(source))
