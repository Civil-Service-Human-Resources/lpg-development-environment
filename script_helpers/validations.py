from script_helpers.config import APPS

def validate_app_name(app_name):
    app_names = [app.name for app in APPS]
    app_names_ln = "\n".join(app_names)
    if app_name not in app_names:
        print(f"{app_name} is not a valid application. Valid apps are: \n{app_names_ln}")
        return None
    else:
        return [app for app in APPS if app.name == app_name][0]

def validate_args(args, required_args):
    if len(args) != len(required_args):
        required_args_ln = "\n".join(required_args)
        print(f"Script requires {len(required_args)} arguments: \n{required_args_ln}")
        return False
    else:
        return True