#!/usr/bin/env python

"""Analysis description."""


from src._config import Config as config


def main() -> None:

    step1()
    step2()


def step1() -> None:
    ...


def step2() -> None:
    ...


if __name__ == "__main__" and "get_ipython" not in locals():
    import sys

    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit()
