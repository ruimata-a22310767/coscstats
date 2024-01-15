"""
COScStats Setting loader

Settings loader module for use with COScStats lib

Author: Rui Mata
Email: atamiur@gmail.com
Date: Jan 2024

Dependencies:
    ['os']                      # python built in 
    ['json']                    # python built in
    ['dataclasses'] (>= 0.6)    # dataclass lib -> handle class alike data structures

Example usage:
    import settings
    config = settings.read_config()

TODO: exception management

"""
from dataclasses import dataclass, field, asdict
import os, json


# globals
STD_SETTINGS_FOLDER = "settings/"
STD_SETTINGS_FILE = "config.json"
STD_DATA_FOLDER = "data/"
STD_STATS_FOLDER = "status/"


@dataclass
class Settings:
    settings_folder: str = STD_SETTINGS_FOLDER
    settings_file: str = STD_SETTINGS_FILE
    data_folder: str = STD_DATA_FOLDER
    stats_folder: str = STD_STATS_FOLDER

    def as_dict(self):
        return asdict(self)

    def as_json(self):
        return json.dumps(self.as_dict(), indent=4)


# -------------------------------------------------------


# util functions
def read_config():
    """Retrieves the settings json from predefined file. If not present, creates folder and config file (<settings_folder>/<settings_file>)

    Parameters:
        N/A

    Returns:
        Settings: dataclass object
    """

    # check if the settings folder exists
    if not os.path.exists(STD_SETTINGS_FOLDER):
        # Create the settings folder
        os.mkdir(STD_SETTINGS_FOLDER)

    # Check if the config.json file exists in the settings folder
    if not os.path.exists(STD_SETTINGS_FOLDER + STD_SETTINGS_FILE):
        # create a default settings definition
        config = Settings()

        # create an empty config.json file
        file = open(STD_SETTINGS_FOLDER + STD_SETTINGS_FILE, "w")

        # write default settings into file
        file.write(config.as_json())

        # close the settings file
        file.close()
        return config

    # read the config.json file
    with open(STD_SETTINGS_FOLDER + STD_SETTINGS_FILE) as f:
        config_json = json.load(f)

        # convert json to Settings dataclass (** to ensure key to properties exact match)
        config = Settings(**config_json)

    # use the config object
    return config


# if launched via command line (for testing purposes)
if __name__ == "__main__":
    config = read_config()
    print(config)
    print(config.settings_folder)
    print(config.settings_file)
    print(config.data_folder)
    print(config.stats_folder)
