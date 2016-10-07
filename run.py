import click

from solr import solr

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
def backup(host, port, core, location, max_retries, time_between_retries):
  solr(host, port, core)['backup'](location, max_retries, time_between_retries)

@click.command()
def restore():
  click.echo('Initializing restore')

def move_backup(source, target):
  click.echo('Moving backup to go')

cli.add_command(backup)
cli.add_command(restore)

if __name__ == '__main__':
  cli()
