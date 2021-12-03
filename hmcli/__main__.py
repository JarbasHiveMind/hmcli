from importlib import import_module
from pkgutil import iter_modules

import hmcli
from src.commands import hmcli_cmds


for plugin in iter_modules(hmcli.__path__, hmcli.__name__ + "."):
    import_module(plugin.name)

if __name__ == "__main__":
    hmcli_cmds()
