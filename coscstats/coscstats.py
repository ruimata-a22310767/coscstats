"""
COScStats main 

Main COSc file handling module

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
from data_files import list_data_files
import data_header
from pixeldata_rasterio import process_data_file
import tabulate
from pprint import pprint

config: Settings


def read_metadata(file: str):
    return


def grab_statistics(config: Settings):
    # get data file list
    print("Determining files to process...", end="")
    sys.stdout.flush()
    cosc_files = list_data_files(config)
    print("OK")
    print("Files to be processed: ", cosc_files, "\n")

    # for each file
    #   retrieve file metadata
    #   process file and create dict data
    for file in cosc_files:
        # get header metadata
        print(
            "----------------------------\nProcessing file  -->  ",
            config.data_folder + file,
        )  # TODO: get into a method
        print("    Retrieving metadata header...", end="")
        data_header.GeotiffMetadatHeader.target_file(config.data_folder + file)
        print("OK")

        # getting detailed info
        print("    Processing pixel data...")  # , end="")
        sys.stdout.flush()
        process_data_file(config.data_folder + file)
        print("    file processed !")

    return


def _main():
    # read the config file
    print("Configuration settings... ", end="")
    sys.stdout.flush()
    config = read_config()
    print("OK")

    # check if arguments are set
    # adjust config based on arguments

    # pprint(config)  # @@@ remove
    # pprint(list(enumerate(sys.argv)))  # @@@ remove

    from commands.commands import _commands

    _commands()

    # grab statistics
    stats = grab_statistics(config)
    #   cycle data files

    #   create statistics


if __name__ == "__main__":
    _main()
