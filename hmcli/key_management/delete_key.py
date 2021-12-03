import click

from jarbas_hive_mind.database import ClientDatabase
from hmcli.src.commands import hmcli_cmds

@click.command()
@click.argument("node_id", required=True)
def delete_key(node_id):
    with ClientDatabase() as db:
        for x in db:
            if x["client_id"] == int(node_id):
                item_id = db.get_item_id(x)
                db.update_item(item_id, dict(client_id=-1, api_key="revoked"))
                print(f"Revoked credentials!\n")
                print("Node ID:", x["client_id"])
                print("Friendly Name:", x["name"])
                print("Access Key:", x["api_key"])
                print("Encryption Key:", x["crypto_key"])
                break
        else:
            print("Invalid Node ID!")

hmcli_cmds.add_command(delete_key)