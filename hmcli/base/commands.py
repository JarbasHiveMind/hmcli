from importlib import import_module
from pkgutil import iter_modules

import click

import hmcli


@click.group()
def hmcli_cmds():
    pass


def main():
    for plugin in iter_modules(hmcli.__path__, hmcli.__name__ + "."):
        import_module(plugin.name)
    hmcli_cmds()
