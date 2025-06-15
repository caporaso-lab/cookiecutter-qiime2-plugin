import subprocess

from copier_templates_extensions import ContextHook


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
