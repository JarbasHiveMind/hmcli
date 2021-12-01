from local_hive.loader import load_skills_folder
from mycroft.skills.skill_loader import get_default_skills_directory
from ovos_utils import wait_for_exit_signal


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Load and Connect a directory containing skills to LocalHive')
    parser.add_argument("--path", help="path to directory with skills to be loaded",
                        default=get_default_skills_directory())
    args = parser.parse_args()

    skills = list(load_skills_folder(args.path))
    if not skills:
        print(f"No skills found in {args.path}")
        exit(1)

    for skill in skills:
        print("Loaded: ", skill.skill_id)

    wait_for_exit_signal()

    for skill in skills:
        skill.handle_shutdown()


if __name__ == '__main__':
    main()
