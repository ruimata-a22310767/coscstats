"""


"""
from dataclasses import dataclass, field, asdict
from typing import List

import json


# globals


@dataclass
class Settings:
    settings_folder: str = "settings"
    data_folder: str = "data"
    stats_folder: str = "status"

    def as_dict(self):
        return asdict(self)

    def as_json(self):
        return json.dumps(self.as_dict(), indent=4)


# -------------------------------------------------------


# util functions
def read_config():
    import os
    import json

    # check if the settings folder exists
    if not os.path.exists("settings"):
        # Create the settings folder
        os.mkdir("settings")

    # Check if the config.json file exists in the settings folder
    if not os.path.exists("settings/config.json"):
        # create a default settings definition
        config = Settings()

        # create an empty config.json file
        file = open("settings/config.json", "w")

        # write default settings into file
        file.write(config.as_json())

        # close the settings file
        file.close()
        return

    # read the config.json file
    with open("settings/config.json") as f:
        config = json.load(f)

    # use the config object
    return config


# if launched via command line (for testing purposes)
if __name__ == "__main__":
    config = read_config()
    print(config)
