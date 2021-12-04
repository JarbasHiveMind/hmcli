import click

from hmcli.src.commands import hmcli_cmds

@click.command()
@click.argument("path", required=True)
def connect_skill():
    from local_hive.loader import HiveMindExternalSkillWrapper
    from ovos_utils import wait_for_exit_signal
    skill = HiveMindExternalSkillWrapper(args.path)

    wait_for_exit_signal()

    skill.handle_shutdown()

hmcli_cmds.add_command(connect_skill)
