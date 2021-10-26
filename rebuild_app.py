import sys
from script_helpers.git_functions import does_app_repo_exist
from script_helpers.app_functions import build_app
from script_helpers.validations import validate_app_name, validate_args

def run():
    args = sys.argv[1:]
    valid_number_of_args = validate_args(args, ["app name"])

    if valid_number_of_args:

        app_name = args[0]
        app = validate_app_name(app_name)

        if app:
            if does_app_repo_exist(app):
                build_app(app)

run()