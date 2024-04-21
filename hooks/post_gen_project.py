import subprocess

def _check_git_installed():
    try:
        _ = subprocess.run("git --version",
                           shell=True, check=True, capture_output=True)
    except subprocess.CalledProcessError:
        return False
    return True

commit_message_head = "initial commit"
commit_message_content = (
    "Created from https://github.com/caporaso-lab/cookiecutter-qiime2-plugin. "
    "See https://develop.qiime2.org to learn more.")

if __name__ == "__main__":
    if not _check_git_installed():
        print("Git is not installed, so won't initialize a git repository.")
    else:
        subprocess.check_call(
            "git init", shell=True)
        subprocess.check_call(
            "git add .", shell=True)
        subprocess.check_call(
            f'git commit -m "{commit_message_head}" -m "{commit_message_content}"', shell=True)
        print("Git was found. Initialized git repository.")

