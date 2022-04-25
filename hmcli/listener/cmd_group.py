from hmcli.base import hmcli_cmds


@hmcli_cmds.group("listener", help="HiveMind listener controls")
def listener_cmds():
    """
    the subcommand 'hivemind listener', a Click command group
    """
