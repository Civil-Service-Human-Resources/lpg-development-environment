from config import APPS
from git_functions import clone_all_apps

def run():
    clone_all_apps(APPS)

run()