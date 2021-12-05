import click

from .cmd_group import server_cmds

@click.command(help="start listening for HiveMind connections")
@click.option("--port", help="HiveMind port number", type=int, default=5678)
def listen():
    from jarbas_hive_mind import get_listener
    from jarbas_hive_mind.configuration import CONFIGURATION

    config = CONFIGURATION
    listener = get_listener()
    listener.load_config(config)
    # Replace defined values
    if args.port is not None:
        listener.port = args.port
    listener.listen()

server_cmds.add_command(listen)
