from os import makedirs
from os.path import isdir
from pprint import pprint

import click
from json_database import JsonStorageXDG

from .cmd_group import config_cmds

CONFIGURATION = JsonStorageXDG("HivemindCore")


@click.command("set-loop", help="set event loop backend (asyncio vs twisted)")
@click.option('--backend', type=click.Choice(['asyncio', 'twisted']), required=True)
def set_loop(backend):
    if backend == "twisted":
        CONFIGURATION["twisted"] = True
    else:
        CONFIGURATION["twisted"] = False
    CONFIGURATION.store()


@click.command("set-port", help="set hivemind listener port")
@click.option('--port', type=int, required=True)
def set_port(port):
    CONFIGURATION["port"] = port
    CONFIGURATION.store()


@click.command("set-cert-path", help="set path to look for ssl certificates")
@click.option('--path', type=str, required=True)
def set_cert(path):
    CONFIGURATION["ssl"]["certificates"] = path
    if not isdir(CONFIGURATION["ssl"]["certificates"]):
        makedirs(CONFIGURATION["ssl"]["certificates"])

    CONFIGURATION.store()


@click.command("set-cert-file", help="set filename for ssl certificate, default HiveMind.crt")
@click.option('--name', type=str, required=True)
def set_cert_file(name):
    CONFIGURATION["ssl"]["certificates"]['ssl_certfile'] = name
    CONFIGURATION.store()


@click.command("set-cert-key", help="set filename for ssl certificate, default HiveMind.key")
@click.option('--name', type=str, required=True)
def set_cert_key(name):
    CONFIGURATION["ssl"]["certificates"]['ssl_keyfile'] = name
    CONFIGURATION.store()


@click.command("enable-ssl", help="Enable wss:// (secure)")
def enable_ssl():
    CONFIGURATION["ssl"]["enabled"] = True
    CONFIGURATION.store()


@click.command("disable-ssl", help="Disable wss:// (insecure)")
def disable_ssl():
    CONFIGURATION["ssl"]["enabled"] = False
    CONFIGURATION.store()


@click.command("require-crypto", help="require AES encryption, connections will be refused if key is missing")
def require_crypto():
    CONFIGURATION["crypto"]["required"] = True
    CONFIGURATION.store()


@click.command("optional-crypto", help="optional AES encryption, default to plain text messages")
def optional_crypto():
    CONFIGURATION["crypto"]["required"] = False
    CONFIGURATION.store()


@click.command("enable-handshake", help="Enable automatic crypto key negotiation")
def enable_handshakes():
    CONFIGURATION["crypto"]["handshake"] = True
    CONFIGURATION.store()


@click.command("disable-handshake", help="Disable automatic crypto key negotiation")
def disable_handshakes():
    CONFIGURATION["crypto"]["handshake"] = False
    CONFIGURATION.store()


@click.command("print", help="print json config")
def printcfg():
    CONFIGURATION["ssl"]["enabled"] = False
    pprint(CONFIGURATION)


config_cmds.add_command(printcfg)
config_cmds.add_command(set_loop)
config_cmds.add_command(set_port)
config_cmds.add_command(set_cert_file)
config_cmds.add_command(set_cert_key)
config_cmds.add_command(set_cert)
config_cmds.add_command(enable_ssl)
config_cmds.add_command(disable_ssl)
config_cmds.add_command(require_crypto)
config_cmds.add_command(optional_crypto)
config_cmds.add_command(enable_handshakes)
config_cmds.add_command(disable_handshakes)
