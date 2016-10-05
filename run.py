import click
import requests

@click.group()
def cli():
  pass

@click.command()
@click.option('--host', help='Solr host to be backed up')
@click.option('--port', default=8983, help='Solr port')
@click.option('--core', help='Solr core to be backed up')
@click.option('--location', help='Disk location to which solr will dump the backup ')
def backup(host, port, core, location):
  click.echo('Initializing backup')
  core_location = "{0}/{1}".format(location, core)
  resp = requests.get('http://{0}:{1}/solr/{2}/replication?command=backup&location=${3}'.format(host, port, core, core_location))
  click.echo(resp)

@click.command()
def restore():
  click.echo('Initializing restore')


cli.add_command(backup)
cli.add_command(restore)

if __name__ == '__main__':
  cli()
