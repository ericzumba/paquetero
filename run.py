import click

@click.group()
def cli():
    pass

@click.command()
def backup():
  click.echo('Initializing backup')

@click.command()
def restore():
  click.echo('Initializing restore')


cli.add_command(backup)
cli.add_command(restore)

if __name__ == '__main__':
    cli()
