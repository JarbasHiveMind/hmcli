from rich.console import Console
from rich.table import Table

from jarbas_hive_mind.database import ClientDatabase


def list_db():
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


def main():
    list_db()


if __name__ == '__main__':
    main()
