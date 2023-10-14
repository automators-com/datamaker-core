import click
from datamaker import __version__


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.version_option(__version__, message="%(version)s")
@click.pass_context
def cli(ctx):
    """Welcome to the datamaker CLI"""
    pass
