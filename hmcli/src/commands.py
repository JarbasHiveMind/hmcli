import click
from click_default_group import DefaultGroup

#@click.group(cls=DefaultGroup, default='\0', no_args_is_help=True, invoke_without_command=True)
@click.group()
def hmcli_cmds():
    pass

#@hmcli_cmds.command("\0", hidden=True)
#@click.option("--version", required=False, is_flag=True, help="Print current version and exit")
#def hmcli(version:bool=False):
#    print(version)

from importlib import import_module
from pkgutil import iter_modules

import hmcli
from src.commands import hmcli_cmds


def main():
  for plugin in iter_modules(hmcli.__path__, hmcli.__name__ + "."):
    import_module(plugin.name)
  hmcli_cmds()
