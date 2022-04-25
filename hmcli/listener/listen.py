import click

from .cmd_group import listener_cmds


@click.command(help="start listening for HiveMind connections")
@click.option("--port", help="HiveMind port number", type=int, default=5678)
@click.option("--ssl", help="use wss://", is_flag=True)
def listen(port: int, ssl: bool):
    from jarbas_hive_mind import get_listener
    from jarbas_hive_mind.configuration import CONFIGURATION

    config = CONFIGURATION
    config["ssl"]["use_ssl"] = ssl
    listener = get_listener()
    listener.load_config(config)
    # Replace defined values
    if port is not None:
        listener.port = port
    listener.listen()


listener_cmds.add_command(listen)
