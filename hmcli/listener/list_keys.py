import click
from rich.console import Console
from rich.table import Table

from .cmd_group import listener_cmds


@click.command(help="list devices and keys", name="list-keys")
def list_keys():
    from jarbas_hive_mind.database import ClientDatabase
    console = Console()
    table = Table(title="HiveMind Credentials:")
    table.add_column("ID", justify="center")
    table.add_column("Name", justify="center")
    table.add_column("Access Key", justify="center")
    table.add_column("Crypto Key", justify="center")

    with ClientDatabase() as db:
        for x in db:
            if x["client_id"] != -1:
                table.add_row(str(x["client_id"]), x["name"], x["api_key"], x["crypto_key"])

    console.print(table)


listener_cmds.add_command(list_keys)
