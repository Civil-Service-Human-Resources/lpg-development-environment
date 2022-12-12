from script_helpers.config import APPS
from script_helpers.git_functions import clone_all_apps, create_required_directories
from script_helpers.app_functions import build_apps
import sys

BUILD_APPS_FLAG = "-build"
ACCEPTED_ARGS = [BUILD_APPS_FLAG]

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


def run(should_build_apps=False):

    create_required_directories()

    print("\nCLONING APPS\n")
    clone_all_apps(APPS)

    if should_build_apps:
        requirements_met = check_requirements()
        if requirements_met:
            print("\nBUILDING APPS\n")
            build_apps(APPS)
        else:
            print("ERROR: Build flag was passed in, however not all requirements for building projects have been met.")
            exit(1)

def validate_args(args):

    invalid_args = []

    for arg in args:
        if arg not in ACCEPTED_ARGS:
            invalid_args.append(arg)
    
    return invalid_args

args = sys.argv[1:]

invalid_args = validate_args(args)
if invalid_args:
    print(f"{invalid_args} are not valid arguments. Valid args are: {ACCEPTED_ARGS}")
    exit(1)

should_build_apps = BUILD_APPS_FLAG in args
run(should_build_apps=should_build_apps)