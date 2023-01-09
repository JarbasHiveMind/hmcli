from hmcli.base import hmcli_cmds


@hmcli_cmds.group("listener", help="HiveMind listener controls")
def listener_cmds():
    """
    the subcommand 'hmcli listener', a Click command group
    """
