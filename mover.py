import click
def mover():
  def replace(source, target):
    click.echo('moving {0} to {1}'.format(source, target))
  
  return dict(replace=replace)
