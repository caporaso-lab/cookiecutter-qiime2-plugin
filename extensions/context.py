import urllib.request
import subprocess

import yaml
from copier_templates_extensions import ContextHook

# Download the data only once (because of sys.module cache),
# instead of on each template event.
DIST_DATA = \
    'https://raw.githubusercontent.com/qiime2/distributions/dev/data.yaml'
with urllib.request.urlopen(DIST_DATA) as response:
    yaml_file = response.read()
    distributions_data = yaml.safe_load(yaml_file)


def _check_git_installed():
    try:
        _ = subprocess.run("git --version",
                           shell=True, check=True, capture_output=True)
    except subprocess.CalledProcessError:
        return False
    return True


class ContextUpdater(ContextHook):
    def hook(self, context):
        if context["_copier_phase"] == "prompt":
            return {}

        update = {
            "has_git": _check_git_installed(),
            "first_run": not (context['_copier_conf']['dst_path']
                              / context['package_name'] / '.git/').exists()
        }
        return update
