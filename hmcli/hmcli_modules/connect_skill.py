from local_hive.loader import HiveMindExternalSkillWrapper
from ovos_utils import wait_for_exit_signal


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Connect a skill to LocalHive')
    parser.add_argument("--path", help="path to skill to be loaded")
    args = parser.parse_args()

    skill = HiveMindExternalSkillWrapper(args.path)

    wait_for_exit_signal()

    skill.handle_shutdown()


if __name__ == '__main__':
    main()
