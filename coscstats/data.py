"""
COScStats data files management

Settings loader module for use with COScStats lib

Author: Rui Mata
Email: atamiur@gmail.com
Date: Jan 2024

Dependencies:
    [os]                        # python built in 
    [settings]                  # local definition of Settings dataclass

Example usage:
    import data
    print(list_data_files(STD_DATA_FOLDER))

TODO: exception management

"""

import os
from settings import Settings, STD_DATA_FOLDER
import settings


# globals
data_files = []


def list_data_files(settings: Settings):
    """Retrieves the list of data files in the defined data folder. Files are expected to be in the format <name>.tif
    Sets global data_files as a list of tif files. Also returns a list of data files (as a list of strings)

    Parameters:
        N/A

    Returns:
        Settings: dataclass object
    """
    data_files = [
        file
        for file in os.listdir(STD_DATA_FOLDER)
        if file[-1 * (len(file) - t.find(".")) :] in STD_DATA_EXTENSIONS
        # if file.upper().endswith(".tif".upper())
    ]
    # t[-1*(len(t)-t.find('.')):]

    return data_files


# if launched via command line (for testing purposes)
if __name__ == "__main__":
    # Example usage
    tif_files = list_data_files(STD_DATA_FOLDER)
    print(tif_files)
