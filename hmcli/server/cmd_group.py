from hmcli.base import hmcli_cmds

@hmcli_cmds.group("server", help="HiveMind server controls")
def server_cmds():
    """
    the subcommand 'hivemind server', a Click command group
    """
