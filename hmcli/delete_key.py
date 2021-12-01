import argparse

from jarbas_hive_mind.database import ClientDatabase


def main():
    parser = argparse.ArgumentParser(description="Delete node from HiveMind's database")
    parser.add_argument("--node_id", help="id of node to delete")
    args = parser.parse_args()

    with ClientDatabase() as db:
        for x in db:
            if x["client_id"] == int(args.node_id):
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


if __name__ == '__main__':
    main()
