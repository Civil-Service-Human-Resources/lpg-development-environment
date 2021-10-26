import subprocess
import re

class Requirement:

    def __init__(self, lang, required_version: str, version_command, version_regex):
        self.lang = lang
        self.required_version = required_version
        self.version_command = version_command
        self.version_regex = version_regex

    def does_version_match(self):
        version_out = subprocess.check_output(self.version_command, stderr=subprocess.STDOUT)
        version = re.search(self.version_regex, str(version_out)).groups()[0]
        return self.required_version.startswith(version)


class AppLanguage:

    def __init__(self, lang, build_tool=None, build_command=None, compile_dir=None):
        self.lang = lang
        self.build_tool = build_tool
        self.build_command = build_command
        self.compile_dir = compile_dir

class App:

    def __init__(self, name, _source_language: AppLanguage, requirements=[], branch=None):
        self.name = name
        self._source_language = _source_language
        if self._source_language.build_tool:
            self.buildable = True
        else:
            self.buildable = False
        self.requirements = requirements
        self.branch = branch