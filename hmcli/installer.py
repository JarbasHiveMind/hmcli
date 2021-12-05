import os
import subprocess
import sys
from os.path import expanduser, isfile
from subprocess import PIPE, Popen
import os
from ovos_utils.log import LOG


class HiveMindInstaller:
    def __init__(self, interactive=True, dev=True, update=True):
        self.interactive = interactive
        self.dev = dev
        self.update = update

    def pip_install(self, packages, print_logs=True):
        if not len(packages):
            return False

        pip_args = [sys.executable, '-m', 'pip', 'install']
        if self.update:
            pip_args += ["-U"]

        for dependent_python_package in packages:
            LOG.info("(pip) Installing " + dependent_python_package)
            pip_command = pip_args + [dependent_python_package]
            if print_logs:
                proc = Popen(pip_command)
            else:
                proc = Popen(pip_command, stdout=PIPE, stderr=PIPE)
            pip_code = proc.wait()
            if pip_code != 0:
                stderr = proc.stderr.read().decode()
                raise RuntimeError(
                    pip_code, proc.stdout.read().decode(), stderr
                )

        return True

    @staticmethod
    def create_unit(python_cmd, name="", description=""):
        unit_template = """[Unit]
        Description={description}
    
        [Service]
        ExecStart={python} {script_path}
    
        [Install]
        WantedBy=default.target
        """
        name = name or python_cmd.split("/")[-1].split(".")[0]
        p = expanduser("~/.config/systemd/user")
        os.makedirs(p, exist_ok=True)
        units_path = f'{p}/{name}.service'
        if not isfile(units_path):
            with open(units_path, "w") as f:
                f.write(unit_template.format(
                    python=sys.executable,
                    description=description or name,
                    script_path=python_cmd
                ))
        return units_path

    @staticmethod
    def is_localhive_installed():
        try:
            import local_hive
            return True
        except ImportError:
            return False

    @staticmethod
    def is_hivemind_installed():
        try:
            import jarbas_hive_mind
            return True
        except ImportError:
            return False

    @staticmethod
    def is_voicesat_installed():
        try:
            import hivemind_voice_satellite
            return True
        except ImportError:
            return False

    @staticmethod
    def is_cli_installed():
        try:
            import hivemind_cli_terminal
            return True
        except ImportError:
            return False

    def install_hivemind_core(self, branch="dev"):
        installed = self.is_hivemind_installed()
        if not installed or self.update:
            install = not self.interactive or \
                      input("Install/Update HiveMind-core? y/n :").lower().startswith("y")
            if install:
                if self.dev:
                    pkg = f"https://github.com/JarbasHiveMind/HiveMind-core/archive/{branch}.zip"
                else:
                    pkg = "jarbas_hive_mind"
                installed = self.pip_install([pkg])

        if not installed:
            print("Could not install HiveMind-core")
            return

        print("HiveMind-core installed")

    def install_hivemind_voice(self, branch="v2"):
        installed = self.is_voicesat_installed()
        if not installed or self.update:
            install = not self.interactive or \
                      input("Install/Update HiveMind-voice-sat? y/n :").lower().startswith("y")
            if install:
                if self.dev:
                    pkg = f"https://github.com/JarbasHiveMind/HiveMind-voice-sat/archive/{branch}.zip"
                else:
                    pkg = "HiveMind-voice-sat"
                installed = self.pip_install([pkg])

        if not installed:
            print("Could not install HiveMind-voice-sat")
            return

        print("HiveMind-voice-sat installed")

    def install_hivemind_cli(self, branch="v2"):
        installed = self.is_cli_installed()
        if not installed or self.update:
            install = not self.interactive or \
                      input("Install/Update HiveMind-cli? y/n :").lower().startswith("y")
            if install:
                if self.dev:
                    pkg = f"https://github.com/JarbasHiveMind/HiveMind-cli/archive/{branch}.zip"
                else:
                    pkg = "HiveMind-cli"
                installed = self.pip_install([pkg])

        if not installed:
            print("Could not install HiveMind-cli")
            return

        print("HiveMind-cli installed")

    def install_localhive(self, branch="master"):
        installed = self.is_localhive_installed()
        if not installed or self.update:
            install = not self.interactive or \
                      input("Install/Update local hive? y/n :").lower().startswith("y")
            if install:
                if self.dev:
                    pkg = f"https://github.com/JarbasHiveMind/LocalHive/archive/{branch}.zip"
                else:
                    pkg = "HiveMind-LocalHive"
                installed = self.pip_install([pkg])

        if not installed:
            print("Could not install LocalHive")
            return

        print("LocalHive installed")

    def enable_hivemind_core(self):
        installed = self.is_hivemind_installed()
        unit = "HiveMind"
        if not installed:
            print("Could not enable HiveMind-core, it is not installed")
            return

        import jarbas_hive_mind
        create = not self.interactive or \
                    input("Create systemd user unit file? y/n :").lower().startswith("y")
        if create:
            self.create_unit(jarbas_hive_mind.__file__.replace("__init__.py", "__main__.py"),
                             unit, "Listen for HiveMind connections")
        os.system(f"systemctl --user enable {unit}")

    def enable_hivemind_voice(self):
        unit = "HiveMind_voice_satellite"
        installed = self.is_voicesat_installed()
        if not installed:
            print(f"Could not enable {unit}, it is not installed")
            return

        # create unit file
        import hivemind_voice_satellite
        create = not self.interactive or \
                    input("Enable start on boot? y/n :").lower().startswith("y")
        if create:
            self.create_unit(hivemind_voice_satellite.__file__.replace("__init__.py", "__main__.py"),
                             unit, "LocalHive Voice Service")

        # enable
        os.system(f"systemctl --user enable {unit}")

    def enable_localhive(self):
        unit = "LocalHive"
        installed = self.is_localhive_installed()
        if not installed:
            print(f"Could not enable {unit}, it is not installed")
            return

        import local_hive
        create = not self.interactive or \
                    input("Create systemd user unit file? y/n :").lower().startswith("y")
        if create:
            self.create_unit(local_hive.__file__.replace("__init__.py", "__main__.py"),
                             unit, "Load mycroft skills in isolation")
        os.system(f"systemctl --user enable {unit}")

    def disable_hivemind_core(self):
        installed = self.is_hivemind_installed()
        if not installed:
            print("Could not disable HiveMind-core, it is not installed")
            return
        unit = "HiveMind"
        os.system(f"systemctl --user disable {unit}")

    def disable_hivemind_voice(self):
        installed = self.is_voicesat_installed()
        if not installed:
            print("Could not disable HiveMind-voice-sat, it is not installed")
            return
        unit = "HiveMind_voice_satellite"
        os.system(f"systemctl --user disable {unit}")

    def disable_localhive(self):
        installed = self.is_localhive_installed()
        if not installed:
            print("Could not disable LocalHive, it is not installed")
            return
        unit = "LocalHive"
        os.system(f"systemctl --user disable {unit}")

    def start_hivemind_core(self):
        installed = self.is_hivemind_installed()

        if not installed:
            print("Could not start HiveMind-core, it is not installed")
            return

        unit = "HiveMind"
        os.system(f"systemctl --user start {unit}")

    def start_hivemind_voice(self):
        installed = self.is_voicesat_installed()
        if not installed:
            print("Could not enable HiveMind-voice-sat, it is not installed")
            return
        unit = "HiveMind_voice_satellite"
        os.system(f"systemctl --user start {unit}")

    def start_localhive(self):
        installed = self.is_localhive_installed()

        if not installed:
            print("Could not start LocalHive, it is not installed")
            return

        unit = "LocalHive"
        os.system(f"systemctl --user start {unit}")

    def stop_hivemind_core(self):
        installed = self.is_hivemind_installed()
        if not installed:
            print("Could not stop HiveMind-core, it is not installed")
            return
        unit = "HiveMind"
        os.system(f"systemctl --user stop {unit}")

    def stop_hivemind_voice(self):
        installed = self.is_voicesat_installed()
        if not installed:
            print("Could not stop HiveMind-voice-sat, it is not installed")
            return
        unit = "HiveMind_voice_satellite"
        os.system(f"systemctl --user stop {unit}")

    def stop_localhive(self):
        installed = self.is_localhive_installed()
        if not installed:
            print("Could not stop LocalHive, it is not installed")
            return
        unit = "LocalHive"
        os.system(f"systemctl --user stop {unit}")

    def install(self):
        self.install_hivemind_core()
        self.install_localhive()
        self.install_hivemind_cli()
        self.install_hivemind_voice()

    def enable(self):
        self.enable_hivemind_core()
        self.enable_localhive()
        self.enable_hivemind_voice()

    def disable(self):
        self.disable_hivemind_core()
        self.disable_localhive()
        self.disable_hivemind_voice()

    def start(self):
        self.start_hivemind_core()
        self.start_localhive()
        self.start_hivemind_voice()

    def stop(self):
        self.stop_localhive()
        self.start_hivemind_core()
        self.start_hivemind_voice()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Install HiveMind')
    parser.add_argument("--no-prompt", help="Do not prompt user before actions", action='store_true')
    parser.add_argument("--dev", help="install from github", action='store_true')
    parser.add_argument("--update", help="update existing install", action='store_true')
    parser.add_argument("--enable", help="enable HiveMind system services (launch on boot)", action='store_true')
    parser.add_argument("--disable", help="disable HiveMind system services (launch on boot)", action='store_true')
    parser.add_argument("--start", help="start HiveMind system services", action='store_true')
    parser.add_argument("--stop", help="stop HiveMind system services", action='store_true')

    args = parser.parse_args()

    installer = HiveMindInstaller(interactive=not args.no_prompt,
                                  dev=args.dev,
                                  update=args.update)
    installer.install()
    installer.enable()
    # installer.disable()
