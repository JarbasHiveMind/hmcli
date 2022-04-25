import click

from .cmd_group import localhive_cmds


@click.command(help='connect a directory containing skills to LocalHive')
@click.argument("path")
def load_skills_dir(path=None):
    from mycroft.skills.skill_loader import get_default_skills_directory
    from local_hive.loader import load_skills_folder
    from ovos_utils import wait_for_exit_signal

    path = path or get_default_skills_directory()
    skills = list(load_skills_folder(path))
    if not skills:
        print(f"No skills found in {path}")
        exit(1)

    for skill in skills:
        print("Loaded: ", skill.skill_id)

    wait_for_exit_signal()

    for skill in skills:
        skill.handle_shutdown()


localhive_cmds.add_command(load_skills_dir)
