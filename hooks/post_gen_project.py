"""This module is called after project is created."""

import time

import textwrap
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd().absolute()
GITHUB_ORG = "rendeirolab"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"


def main() -> None:
    init_git_repo()
    print_further_instuctions()


def print_further_instuctions() -> None:
    """Show user what to do next after project creation."""
    cmds0 = "\n\t".join(get_git_init_commands())
    cmds1 = "\n\t".join(get_additional_commands())
    CURRENT_DATE = time.strftime("%Y-%m-%d")
    CSV_ROW = ",".join(
        [
            "RLXXXX",
            "{{ cookiecutter.project_slug }}",
            "{{ cookiecutter.project_description }}",
            "{{ cookiecutter.full_name }}",
            CURRENT_DATE,
            "https://github.com/rendeirolab/{{ cookiecutter.project_slug }}",
            "/research/lab_rendeiro/projects/{{ cookiecutter.project_slug }}",
            "/nobackup/lab_rendeiro/projects/{{ cookiecutter.project_slug }}",
        ]
    )
    message = f"""
    Your project '{PROJECT_SLUG}' is created.

    You should have registered your project on the lab's register:
    https://cemmat.sharepoint.com/:x:/r/sites/rendeirolab/_layouts/15/Doc.aspx?sourcedoc=%7B4c72f84b-f33b-4162-a5e8-f05556fdf66b%7D

    Add a row like this:
        "{CSV_ROW}"

    You can now start working on it, but there are a few additional things to do:

    1) Start a github repository in the new directory structure:
        $ cd {PROJECT_SLUG} && git init
    2) Go to https://github.com/new and create a project with the same slug name: '{PROJECT_SLUG}'
        or create if from the command line:
        $ gh repo create --private rendeirolab/{PROJECT_SLUG}
    3) Upload initial code to GitHub (using ssh, requires setup):
        $ git add .
        $ git commit -m "Initial commit"
        $ git branch -M main
        $ git remote add origin git@github.com:{GITHUB_ORG}/{PROJECT_SLUG}.git
        $ git push -u origin main
    4. Create a directory for the project in the CeMM cluster:
        $ mkdir -p /research/lab_rendeiro/projects/{PROJECT_SLUG}/data
    5. Create a directory for the project in the CeMM cluster at:
        $ mkdir -p /nobackup/lab_rendeiro/projects/{PROJECT_SLUG}/
    6. Create a soft link between '/research/.../data' and '/nobackup/.../data':
        $ cd /nobackup/lab_rendeiro/projects/{PROJECT_SLUG}/
        $ ln -s /research/lab_rendeiro/projects/{PROJECT_SLUG}/data ./
    6. Create a 'cemm_metadata.json' file in '/research/lab_rendeiro/projects/{PROJECT_SLUG}/'
    7. Create a 'cemm_metadata.json' file in '/nobackup/lab_rendeiro/projects/{PROJECT_SLUG}/'

    Summary of next steps:
        ```
        {cmds0}
        {cmds1}
        ```

    Don't forget also to describe the project in 'cemm_metadata.json' files as well.
    """
    print(textwrap.dedent(message))


def get_git_init_commands():
    cmds = [
        f"cd {PROJECT_SLUG}",
        "git init",
        "git add .",
        'git commit -m "Initial commit"',
        "git branch -M main",
        f"git remote add origin git@github.com:{GITHUB_ORG}/{PROJECT_SLUG}.git",
        f"gh repo create --private rendeirolab/{PROJECT_SLUG}",
        "git push -u origin main",
    ]
    return cmds


def get_additional_commands():
    cmds = [
        "ssh {{ cookiecutter.username }}@login",
        f"mkdir -p /research/lab_rendeiro/projects/{PROJECT_SLUG}/data",
        f"mkdir -p /nobackup/lab_rendeiro/projects/{PROJECT_SLUG}/",
        f"cd /nobackup/lab_rendeiro/projects/{PROJECT_SLUG}/",
        f"ln -s /research/lab_rendeiro/projects/{PROJECT_SLUG}/data ./",
    ]
    return cmds


def init_git_repo() -> None:
    """
    Create git repository and add to remote.

    Unfortunately it doesn't work as it would require the template instance to already exist but that will only happen after this script finishes.
    """
    import subprocess

    cmds = get_git_init_commands()[1:]
    {% if not cookiecutter.create_github_repo -%} 
    cmds = cmds[:-2]
    {% endif %}

    for cmd in cmds:
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    main()
