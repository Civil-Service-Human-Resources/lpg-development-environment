from script_helpers.config import APP_DIR, APPS
from script_helpers.git_functions import clone_all_apps, create_required_directories

def run():
    create_required_directories()
    clone_all_apps(APPS)

run()