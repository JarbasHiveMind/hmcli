from jarbas_hive_mind import get_listener
from jarbas_hive_mind.configuration import CONFIGURATION


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Start HiveMind websocket listener')
    parser.add_argument("--port", help="HiveMind port number", type=int)
    parser.add_argument("--ssl", help="Listen with wss (default False)", action="store_true")
    args = parser.parse_args()
    config = CONFIGURATION
    config["ssl"]["use_ssl"] = args.ssl
    listener = get_listener()
    listener.load_config(config)
    # Replace defined values
    if args.port is not None:
        listener.port = args.port
    listener.listen()


if __name__ == '__main__':
    main()
