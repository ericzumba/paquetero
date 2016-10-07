import click
from os import listdir
import requests
import time

def find_backup_file(folder_name):
 return listdir(folder_name) 

def solr(host, port, core):
  def backup(location, retries, sleep_time):
    core_location = "{0}/{1}".format(location, core)

    def request_backup():
      click.echo('Requesting backup')
      url = 'http://{0}:{1}/solr/{2}/replication?command=backup&location={3}&wt=json'.format(host, port, core, core_location)
      return 'exception' not in requests.get(url).json()

    def check(retries):
      if retries > 0:
        click.echo('Checking if backup is ready')
        url = 'http://{0}:{1}/solr/{2}/replication?command=restorestatus&wt=json'.format(host, port, core)
        status = requests.get(url).json()['restorestatus']['status']
        return "No restore actions in progress" in status 
      else:
        time.sleep(sleep_time)
        return check(retries - 1) 

    if request_backup():
      click.echo('Backup requested')
      if check(retries):
        return find_backup_file(core_location)

  return dict(backup=backup)
