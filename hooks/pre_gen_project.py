"""This module is called before the project creation is started."""

import os
from pathlib import Path

import textwrap


def main() -> None:
    print_pre_instuctions()


def print_pre_instuctions() -> None:
    """Show user how to set up a configuration."""
    message = """
    Neither a '~/.cookiecutterrc' file or a 'COOKIECUTTER_CONFIG' variable are set!

    For a more streamline use of the template with cookiecutter, please add a YAML file with the configuration.
    If should contain the following structure and fields:

    default_context:
        full_name: "Andre Rendeiro"
        username: "arendeiro"
        email: "arendeiro@cemm.at"

    For more information, see: https://cookiecutter.readthedocs.io/en/1.7.2/advanced/user_config.html
    """

    config = Path("~/.cookiecutterrc").expanduser()
    env = os.environ.get("COOKIECUTTER_CONFIG")
    if not config.exists() and env is None:
        print(textwrap.dedent(message))


if __name__ == "__main__":
    main()
