import argparse
import os

import click

from hmcli.base import hmcli_cmds

@click.command(help="add a device and keys")
@click.argument("name", required=False)
@click.argument("access_key", required=False)
@click.argument("crypto_key", required=False)
def add_keys(name, access_key, crypto_key):

    from jarbas_hive_mind.database import ClientDatabase

    key = crypto_key
    if key:
        print("WARNING: for security the encryption key should be randomly generated\n"
              "Defining your own key is discouraged")
        if len(key) != 16:
            print("Encryption key needs to be exactly 16 characters!")
            raise ValueError
    else:
        key = os.urandom(8).hex()

    access_key = access_key or os.urandom(16).hex()
    with ClientDatabase() as db:
        name = name or f"HiveMind-Node-{db.total_clients()}"
        db.add_client(name, access_key, crypto_key=key)

        # verify
        user = db.get_client_by_api_key(access_key)
        node_id = db.get_item_id(user)

        print("Credentials added to database!\n")
        print("Node ID:", node_id)
        print("Friendly Name:", name)
        print("Access Key:", access_key)
        print("Encryption Key:", key)

hmcli_cmds.add_command(add_keys)
