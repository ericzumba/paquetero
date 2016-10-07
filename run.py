import click

from solr import solr
from mover import s3 

@click.group()
def cli():
  pass

@click.command()
@click.option('--host', help='Solr host to be backed up')
@click.option('--port', default=8983, help='Solr port')
@click.option('--core', help='Solr core to be backed up')
@click.option('--location', help='Disk location to which solr will dump the backup ')
@click.option('--max-retries', default=30, help='Maximum times paquetero checks if backup is ready')
@click.option('--time-between-retries', default=5, help='Time in seconds between each "backup is ready?" request')
@click.option('--aws-region', default="sa-east-1", help='AWS region in which s3 bucket is located')
def backup(host, port, core, location, max_retries, time_between_retries, aws_region):
  backup = solr(host, port, core)['backup'](location, max_retries, time_between_retries)
  s3(aws_region)['store'](backup) 

@click.command()
def restore():
  click.echo('Initializing restore')

def move_backup(source, target):
  click.echo('Moving backup to go')

cli.add_command(backup)
cli.add_command(restore)

if __name__ == '__main__':
  cli()
