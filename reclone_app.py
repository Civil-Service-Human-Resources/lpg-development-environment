import sys
from script_helpers.git_functions import clone_repo, does_app_repo_exist, check_and_create_dir
from script_helpers.validations import validate_app_name, validate_args

def run():
    args = sys.argv[1:]
    valid_number_of_args = validate_args(args, ["app name"])
    if valid_number_of_args:

        app_name = args[0]
        app = validate_app_name(app_name)
        if app:
            if not does_app_repo_exist(app):
                clone_repo(app)

run()