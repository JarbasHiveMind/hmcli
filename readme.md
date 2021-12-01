
```
$ python hmcli/scan.py
Scanning....
                 HiveMind Devices                  
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━┓
┃     Name      ┃ Protocol ┃     Host      ┃ Port ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━┩
│ HiveMind Node │   wss    │ 192.168.1.112 │ 5678 │
└───────────────┴──────────┴───────────────┴──────┘
```

```
$ python hmcli/announce.py --help
usage: announce.py [-h] [--port PORT] [--ssl] [--zeroconf] [--name NAME] [--service SERVICE]

optional arguments:
  -h, --help         show this help message and exit
  --port PORT        HiveMind port number (default: 5678)
  --ssl              use wss://
  --zeroconf         use zeroconf
  --name NAME        friendly device name (default: HiveMind-Node)
  --service SERVICE  HiveMind service type (default: HiveMind-websocket)

```

```     
$ python hmcli/add_keys.py --name Mark1
Credentials added to database!

Node ID: 6
Friendly Name: Mark1
Access Key: 645df537c65caacb9a009a5ba1535d30
Encryption Key: ab8363672d6e7e89
```

```
$ python hmcli/list_keys.py
                      HiveMind Credentials:                       
┏━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ ID ┃ Name  ┃            Access Key            ┃    Crypto Key    ┃
┡━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ 8  │ Mark1 │ 41c544ecd8f939c2b7125858ce903a08 │ 57f89a205d4d7685 │
└────┴───────┴──────────────────────────────────┴──────────────────┘
```

```
$ python hmcli/delete_key.py --node_id 8
Revoked credentials!

Node ID: 8
Friendly Name: Mark1
Access Key: 41c544ecd8f939c2b7125858ce903a08
Encryption Key: 57f89a205d4d7685
```