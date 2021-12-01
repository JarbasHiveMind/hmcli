
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
$ python hmcli/add_keys.py --help
usage: add_keys.py [-h] [--name NAME] [--access_key ACCESS_KEY] [--crypto_key CRYPTO_KEY]

Add node to HiveMind's database

optional arguments:
  -h, --help            show this help message and exit
  --name NAME           human readable name
  --access_key ACCESS_KEY
                        access key
  --crypto_key CRYPTO_KEY
                        payload encryption key
```

```
$ python hmcli/list_keys.py
                      HiveMind Credentials:                       
┏━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ ID ┃       Name        ┃     Access Key     ┃    Crypto Key    ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ 3  │ JarbasCliTerminal │ RESISTENCEisFUTILE │ resistanceISfuti │
└────┴───────────────────┴────────────────────┴──────────────────┘


```

```
$ python hmcli/delete_key.py --help
usage: delete_key.py [-h] [--node_id NODE_ID]

Delete node from HiveMind's database

optional arguments:
  -h, --help         show this help message and exit
  --node_id NODE_ID  id of node to delete
```