import click
from rich.console import Console
from rich.table import Table

from hmcli.src.commands import hmcli_cmds

@click.command()
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

hmcli_cmds.add_command(list_keys)

def main():
    list_keys()


if __name__ == '__main__':
    main()
