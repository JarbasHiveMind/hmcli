import time

from HiveMind_presence import LocalPresence


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="HiveMind port number (default: 5678)", default=5678)
    parser.add_argument("--ssl", help="use wss://", action='store_true')
    parser.add_argument("--name", help="friendly device name (default: HiveMind-Node)",
                        default="HiveMind-Node")
    parser.add_argument("--service", help="HiveMind service type (default: HiveMind-websocket)",
                        default="HiveMind-websocket")

    args = parser.parse_args()

    presence = LocalPresence(port=args.port, ssl=args.ssl,
                             service_type=args.service, name=args.name)
    presence.start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
    presence.stop()


if __name__ == "__main__":
    main()
