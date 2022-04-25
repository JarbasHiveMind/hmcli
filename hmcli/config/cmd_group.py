from hmcli.base import hmcli_cmds


@hmcli_cmds.group("config", help="HiveMind config helper")
def config_cmds():
    """
    the subcommand 'hivemind config', a Click command group
    """
