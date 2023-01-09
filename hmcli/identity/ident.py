import click
from json_database import JsonConfigXDG

from .cmd_group import identity_cmds

BASE_FOLDER = "jarbasHiveMind"
IDENTITY = JsonConfigXDG("identity", subfolder=BASE_FOLDER)


@click.command("set-name", help="set human readable node name")
@click.argument('name', type=str)
def set_name(name):
    IDENTITY["name"] = name
    IDENTITY.store()


@click.command("set-password", help="set hive password")
@click.argument('password', type=str)
def set_password(password):
    IDENTITY["password"] = password
    IDENTITY.store()


@click.command("set-file", help="set identity file location, full path to .asc secret PGP key")
@click.argument('path', type=str)
def set_keyfile(path):
    IDENTITY["key"] = path
    IDENTITY.store()


identity_cmds.add_command(set_name)
identity_cmds.add_command(set_password)
identity_cmds.add_command(set_keyfile)

