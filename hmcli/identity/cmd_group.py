from hmcli.base import hmcli_cmds


@hmcli_cmds.group("identity", help="HiveMind Identity Manager")
def identity_cmds():
    """
    the subcommand 'hmcli identity', a Click command group
    """
