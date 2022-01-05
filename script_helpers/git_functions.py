import os
from script_helpers.classes import App
from script_helpers.config import GIT_REPO_BASE, APP_DIR

def clone_repo(app):
    branch = f"-b {app.branch}" if app.branch else ""
    command = f"git clone {branch} {GIT_REPO_BASE}/{app.name}.git {APP_DIR}/{app.name}"
    print(command)
    return os.system(command)


def clone_all_apps(apps):
    failed_apps = []
    for app in apps:
        if not does_app_repo_exist(app):
            success = clone_repo(app) == 0
            if not success:
                failed_apps.append(app)
        else:
            print(f"{APP_DIR}/{app.name} already exists! Skipping")

    return failed_apps


def check_and_create_dir(directory):

    if not os.path.exists(directory):
        os.mkdir(directory)


def create_required_directories():
    dirs = [APP_DIR]
    create_dirs(dirs)

def does_app_repo_exist(app: App):
    return os.path.exists(f"{APP_DIR}/{app.name}")


def create_dirs(dirs):
    for _dir in dirs:
        print(f"Checking for \"{_dir}\" directory and creating if it doesn't exist...")
        check_and_create_dir(_dir)