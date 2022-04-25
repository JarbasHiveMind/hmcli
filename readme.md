
## Usage

```bash
$ hmcli --help

Usage: hmcli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  local   LocalHive controls
  listener  HiveMind server controls
  setup   HiveMind service configuration - Valid options: 'all', 'ovos',...
```

### Setup

```bash
$ hmcli setup --help

Usage: hmcli setup [OPTIONS] COMMAND [ARGS]...

  HiveMind service configuration  -  Valid options: 'all', 'ovos', 'master', 'local', 'voice', 'cli', 'announce'

Options:
  --help  Show this message and exit.

Commands:
  disable  disable named service for hivemind
  enable   enable named service for hivemind
  install  install named service for hivemind
  restart  restart named service for hivemind
  start    start named service for hivemind
  stop     stop named service for hivemind

```

### LocalHive

```bash
$ hmcli local --help

Usage: hmcli local [OPTIONS] COMMAND [ARGS]...

  LocalHive controls

Options:
  --help  Show this message and exit.

Commands:
  connect-skill    connect a skill to LocalHive
  load-skills-dir  connect a directory containing skills to LocalHive

```

### Listener

```bash
$ hmcli listener --help

Usage: hmcli listener [OPTIONS] COMMAND [ARGS]...

  HiveMind listener controls

Options:
  --help  Show this message and exit.

Commands:
  add-device     add a device and keys
  announce       advertise this node's presence in the local network
  delete-device  remove a device
  list-keys      list devices and keys
  listen         start listening for HiveMind connections
  scan           scan for Hives

```

```
$ hmcli listener scan
Scanning....
                 HiveMind Devices                  
┏━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━┓
┃ Name  ┃ Protocol ┃     Host      ┃ Port ┃
┡━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━┩
│ Mark1 │   wss    │ 192.168.1.112 │ 5678 │
└───────┴──────────┴───────────────┴──────┘
```


## Credentials Management

```     
$ hmcli listener add-device Mark1
Credentials added to database!

Node ID: 6
Friendly Name: Mark1
Access Key: 645df537c65caacb9a009a5ba1535d30
Encryption Key: ab8363672d6e7e89
```

```
$ hmcli listener list-keys
                      HiveMind Credentials:                       
┏━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ ID ┃ Name  ┃            Access Key            ┃    Crypto Key    ┃
┡━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ 8  │ Mark1 │ 41c544ecd8f939c2b7125858ce903a08 │ 57f89a205d4d7685 │
└────┴───────┴──────────────────────────────────┴──────────────────┘
```

```
$ hmcli listener delete-device 8
Revoked credentials!

Node ID: 8
Friendly Name: Mark1
Access Key: 41c544ecd8f939c2b7125858ce903a08
Encryption Key: 57f89a205d4d7685
```

