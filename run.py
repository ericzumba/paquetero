import click
import requests
import time

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
  click.echo('Requesting backup')
  core_location = "{0}/{1}".format(location, core)
  resp = requests.get('http://{0}:{1}/solr/{2}/replication?command=backup&location=${3}'.format(host, port, core, core_location))
  click.echo('Backup requested')

  while True and max_retries > 0:
    click.echo('Checking if backup is ready')
    r = requests.get('http://{0}:{1}/solr/{2}/replication?command=restorestatus'.format(host, port, core))
    if "No restore actions in progress" in r.content:
      click.echo('Backup is ready')
      move_backup('a', 'b')
      break
    else: 
      time.sleep(time_between_retries) 
    max_retries = max_retries - 1

def move_backup(source, target):
  click.echo('Moving backup to go')
  

@click.command()
def restore():
  click.echo('Initializing restore')


cli.add_command(backup)
cli.add_command(restore)

if __name__ == '__main__':
  cli()
