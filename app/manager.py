import click

@click.group()
def cli():
    pass


@cli.command()
@click.pass_context
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default=5000)
def runserver(ctx, host, port):
    """The default method to run the flask application"""
    app = ctx.obj['app']
    app.run(host, port)
