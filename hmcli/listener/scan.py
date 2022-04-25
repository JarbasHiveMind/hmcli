import click
from rich.console import Console
from rich.table import Table

from .cmd_group import listener_cmds



@click.command("scan", help="scan for Hives")
def scan_and_print():
    from HiveMind_presence import LocalDiscovery
    table = Table(title="HiveMind Devices")

    table.add_column("Name", justify="center")
    table.add_column("Protocol", justify="center")
    table.add_column("Host", justify="center")
    table.add_column("Port", justify="center")

    console = Console()
    console.print("Scanning....")
    for device in LocalDiscovery().scan(timeout=10):
        proto = "wss" if device.ssl else "ws"
        table.add_row(device.friendly_name, proto, device.host, str(device.port))
        console.print(table)


listener_cmds.add_command(scan_and_print)
