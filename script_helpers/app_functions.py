import os
from script_helpers.config import APP_DIR
from script_helpers.classes import App

def build_apps(apps):
    for app in apps:
        if app.buildable:
            print(f"App {app.name} is marked as buildable, attempting to build...")
            if not os.path.exists(f"{APP_DIR}/{app.name}/{app._source_language.compile_dir}"):
                print(f"{app._source_language.compile_dir} doesn't exist for {app.name}")
                build_app(app)
            else:
                print(f"{app._source_language.compile_dir} already exists for {app.name}")


def build_app(app: App):
    print(f"Building app {app.name}, running command {app._source_language.build_command}")
    command = f"cd {APP_DIR}/{app.name} && {app._source_language.build_command}"
    return os.system(command)