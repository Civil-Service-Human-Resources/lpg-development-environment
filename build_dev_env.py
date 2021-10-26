from script_helpers.config import APPS, APP_DIR
from script_helpers.git_functions import create_dirs, clone_all_apps
from script_helpers.app_functions import build_apps


def check_requirements():
    print("Checking requirements...")
    requirements = []
    for app in APPS:
        requirements.extend(app.requirements)
    requirements = set(requirements)
    match = True
    for requirement in requirements:
        match = requirement.does_version_match()
        if not match:
            print(f"{requirement.lang} must be set to version {requirement.required_version}")
        else:
            print(f"{requirement.lang} is set to the correct version! ({requirement.required_version})")
    return match


def run():

    requirements_met = check_requirements()

    if requirements_met:
        dirs = [APP_DIR]
        create_dirs(dirs)

        print("\nCLONING APPS\n")
        clone_all_apps(APPS)

        print("\nBUILDING APPS\n")
        build_apps(APPS)

run()