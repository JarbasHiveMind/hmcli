import click

from .cmd_group import localhive_cmds


@click.command(help="connect a skill to LocalHive")
@click.argument("path", required=True)
def connect_skill(path):
    from local_hive.loader import HiveMindExternalSkillWrapper
    from ovos_utils import wait_for_exit_signal
    skill = HiveMindExternalSkillWrapper(path)

    wait_for_exit_signal()

    skill.handle_shutdown()


localhive_cmds.add_command(connect_skill)
