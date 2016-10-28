import click
from os import listdir
from os import path
from os import makedirs 
from os import chmod 
import requests
import time
import json

def find_backup_file(old_backups, folder_name):
  backups_found = set(listdir(folder_name))
  if len(backups_found) == 1:
    return path.join(folder_name, backups_found.pop())
  elif len(backups_found) == 0:
    raise Exception('no backup files found')
  else:
    raise Exception('too many backup files found')

def list_existing_backup_files(folder_name):
  if path.isdir(folder_name):
    click.echo("Directory exists {0}".format(folder_name))
    return set(listdir(folder_name))
  else:
    click.echo("Creating directory {0}".format(folder_name))
    makedirs(folder_name)
    chmod(folder_name, 0o777)
    return set()

def solr(host, port, core):
  def backup(location, retries, sleep_time, backup_name):
    core_location = "{0}/{1}".format(location, core)

    def request_backup():

      click.echo('Requesting backup')
      url = 'http://{0}:{1}/solr/{2}/replication?command=backup&location={3}&name={4}&wt=json'.format(host, port, core, core_location, backup_name)
      resp = requests.get(url).json()
      if 'exception' not in resp:
        return True
      else:
        click.echo('Could not request backup: {0}'.format(resp['exception']))

    def check(retries):
      click.echo('Checking if backup is ready')
      url = 'http://{0}:{1}/solr/{2}/replication?command=details&wt=json'.format(host, port, core)
      time.sleep(10)
      details = requests.get(url).json()['details']

      if ('backup' in details) and ("{0}/snapshot.{1}".format(core_location, backup_name) in details['backup']):
        click.echo('Backup is ready')
        return True
      else:
        if retries > 0:
          click.echo('Waiting for backup to become available')
          time.sleep(sleep_time)
          return check(retries - 1) 
        else:
          raise Exception('No backup found - maximum number of retries exceeded') 
    
    existing_backups = list_existing_backup_files(core_location)
    if request_backup():
      click.echo('Backup requested')
      if check(retries):
        return find_backup_file(existing_backups, core_location)

  return dict(backup=backup)
