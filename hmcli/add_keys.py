import argparse
import os

from jarbas_hive_mind.database import ClientDatabase


def main():
    parser = argparse.ArgumentParser(description="Add node to HiveMind's database")
    parser.add_argument("--name", help="human readable name")
    parser.add_argument("--access_key", help="access key")
    parser.add_argument("--crypto_key", help="payload encryption key")
    args = parser.parse_args()

    key = args.crypto_key
    if key:
        print("WARNING: for security the encryption key should be randomly generated\n"
              "Defining your own key is discouraged")
        if len(key) != 16:
            print("Encryption key needs to be exactly 16 characters!")
            raise ValueError
    else:
        key = os.urandom(8).hex()

    access_key = args.access_key or os.urandom(16).hex()
    with ClientDatabase() as db:
        name = args.name or f"HiveMind-Node-{db.total_clients()}"
        db.add_client(name, access_key, crypto_key=key)

        # verify
        user = db.get_client_by_api_key(access_key)
        node_id = db.get_item_id(user)

        print("Credentials added to database!\n")
        print("Node ID:", node_id)
        print("Friendly Name:", name)
        print("Access Key:", access_key)
        print("Encryption Key:", key)


if __name__ == '__main__':
    main()
