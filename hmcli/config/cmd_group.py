from hmcli.base import hmcli_cmds


@hmcli_cmds.group("config", help="HiveMind config helper")
def config_cmds():
    """
    the subcommand 'hmcli config', a Click command group
    """
