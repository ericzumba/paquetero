import click
from os import listdir
from os import path
import requests
import time

def find_backup_file(old_backups, folder_name):
  found_backups = set(listdir(folder_name)) - old_backups
  if len(found_backups) == 1:
    return path.join(folder_name, found_backups.pop())
  else:
    raise Exception('too many backup files found')

def list_existing_backup_files(folder_name):
  return set(listdir(folder_name))

def solr(host, port, core):
  def backup(location, retries, sleep_time):
    core_location = "{0}/{1}".format(location, core)

    def request_backup():
      click.echo('Requesting backup')
      url = 'http://{0}:{1}/solr/{2}/replication?command=backup&location={3}&wt=json'.format(host, port, core, core_location)
      resp = requests.get(url).json()
      if 'exception' not in resp:
        return True
      else:
        click.echo('Could not request backup: {0}'.format(resp['exception']))

    def check(retries):
      if retries > 0:
        click.echo('Checking if backup is ready')
        url = 'http://{0}:{1}/solr/{2}/replication?command=restorestatus&wt=json'.format(host, port, core)
        status = requests.get(url).json()['restorestatus']['status']
        return "No restore actions in progress" in status 
      else:
        time.sleep(sleep_time)
        return check(retries - 1) 
    
    existing_backups = list_existing_backup_files(core_location)
    click.echo(existing_backups)
    if request_backup():
      click.echo('Backup requested')
      if check(retries):
        return find_backup_file(existing_backups, core_location)

  return dict(backup=backup)
