from hmcli.base import hmcli_cmds


@hmcli_cmds.group("setup", help="HiveMind service configuration  -  Valid options: 'all', 'ovos', 'master', 'local', 'voice', 'cli', 'announce'")
def setup_cmds():
    """
    the subcommand 'hivemind local', a Click command group
    """
