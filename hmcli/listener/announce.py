import time

import click

from .cmd_group import listener_cmds


@click.command(help="advertise this node's presence in the local network")
@click.option("--ssl", help="use wss://", is_flag=True)
@click.option("--port", help="HiveMind port number (default: 5678)", default=5678, required=False)
@click.option("--name", default="HiveMind-Node", help="friendly device name (default: HiveMind-Node)")
@click.option("--service", default="HiveMind-websocket", help="HiveMind service type (default: HiveMind-websocket)")
def presence(port: int, ssl: bool, name: str, service: str):
    from HiveMind_presence import LocalPresence

    pre = LocalPresence(port=port, ssl=ssl, service_type=service, name=name)
    pre.start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
    pre.stop()


listener_cmds.add_command(presence)
