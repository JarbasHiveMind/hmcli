import click
from click_default_group import DefaultGroup

@click.group(cls=DefaultGroup, default='\0', no_args_is_help=True, invoke_without_command=True)
def hmcli_cmds():
    pass

@hmcli_cmds.command("\0", hidden=True)
@click.option("--version", required=False, is_flag=True, help="Print current version and exit")
def hmcli(version:bool=False):
    print(version)
