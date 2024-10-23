#!/usr/bin/env python

"""Analysis description."""


from src import config


def main() -> int:

    step1()
    step2()

    return 0


def step1() -> None: ...


def step2() -> None: ...


if __name__ == "__main__" and "get_ipython" not in locals():
    import sys

    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit()
