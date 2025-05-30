import click


@click.group()
@click.version_option()
def cli():
    "A quick and dirty scheduler."


@cli.command(name="command")
@click.argument( "example")
@click.option( "-o", "--option", help="An example option",)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")
    click.echo( f"option is {option}" )
    click.echo( f"example is {example}" )
