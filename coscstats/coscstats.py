"""
COScStats main 

Maind COSc files handling module

Author: Rui Mata
Email: atamiur@gmail.com
Date: Jan 2024

Dependencies:
    ['os']                      # python built in 
    ['json']                    # python built in
    ['dataclasses'] (>= 0.6)    # dataclass lib -> handle class alike data structures
    ['typing ] (>= 3.7.4.3)     # add-on python module: Support for type hints

Example usage:
    import settings
    config = settings.read_config()

TODO: exception management
TODO: argument validation

"""


import sys
from settings import Settings, read_config
from data import list_data_files
import tabulate
from pprint import pprint

config: Settings


def read_metadata(file: str):
    return


def grab_statistics(config: Settings):
    # get data file list
    data_files = list_data_files(config)
    print("list: ", end="")
    pprint(data_files)
    # for each file
    #   retrieve file metadata
    #   process file and create dict data
    return


def _main():
    # read the config file
    config = read_config()
    # check if arguments are set
    # adjust config based on arguments

    pprint(config)  # @@@ remove
    pprint(list(enumerate(sys.argv)))  # @@@ remove

    from commands.commands import _commands

    _commands()

    # grab statistics
    stats = grab_statistics(config)
    #   cycle data files

    #   create statistics


if __name__ == "__main__":
    _main()


""" def _main():
    if len(sys.argv) > 1:
        from .api import text_stats

        f = sys.argv[1]
        with open(f, "r") as text_file:
            f_stats = text_stats(text_file.read())
        print(
            tabulate(
                f_stats.items(),
                headers=["Statistic", "Value"],
                tablefmt="rounded_outline",
            )
        )

    else:
        from .stats_finder import _find_stats

        stats_found = _find_stats()

        stats_help = {n: getdoc(f).split("\n")[0] for n, f in stats_found.items()}

        print(
            tabulate(
                stats_help.items(),
                headers=["Statistic", "Description"],
                tablefmt="rounded_outline",
            )
        ) """
