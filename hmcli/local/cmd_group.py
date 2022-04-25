from hmcli.base import hmcli_cmds


@hmcli_cmds.group("local", help="LocalHive controls")
def localhive_cmds():
    """
    the subcommand 'hmcli local', a Click command group
    """
