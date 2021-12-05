from hmcli.base import hmcli_cmds

@hmcli_cmds.group("localhive", help="LocalHive controls")
def localhive_cmds():
    """
    the subcommand 'hivemind server', a Click command group
    """
