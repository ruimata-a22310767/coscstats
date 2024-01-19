"""
header metadata handling 

Main COSc file handling module

Author: Rui Mata
Email: atamiur@gmail.com
Date: Jan 2024

Dependencies:
    ['raterio'] (>= 1.3.9)      # raster files handling
    ['dataclasses'] (>= 0.6)    # dataclass lib -> handle class alike data structures

Example usage:
    import settings
    config = settings.read_config()

TODO: exception management
TODO: magic constants

"""

import rasterio
from dataclasses import dataclass, fields
from settings import STD_STATS_FOLDER, check_folder


# Create a dataclass schema
@dataclass
class GeotiffMetadatHeader:
    projection: str
    transform: tuple
    width: int
    height: int
    bands: int

    @classmethod
    def extract_metadata(cls, file: str):
        metadata = None
        # read metadata from GeoTiff file
        with rasterio.open(
            file,
            read_info=True,
        ) as src:
            # Create a GeoTif metadata dataclass with header metadata
            metadata = GeotiffMetadatHeader(
                projection=src.crs,
                transform=src.transform,
                width=src.width,
                height=src.height,
                bands=src.count,
            )
        return metadata

    @classmethod
    def target_file(cls, file: str):
        metadata = cls.extract_metadata(file)
        return cls(
            projection=metadata.projection,
            transform=metadata.transform,
            width=metadata.width,
            height=metadata.height,
            bands=metadata.bands,
        )


if __name__ == "__main__":
    # Example usage
    data = GeotiffMetadatHeader.target_file(
        "/home/rmata/Desktop/coscstats/data/prof/tratameto_mapas/data/COSc2022/COSc2022_N3_v0_TM06.tif"
    )
    print("\n", data, "\n")
    # Save the dataclass
    import pickle

    # testing the dataclass dump into a  file (pickle\binary) TODO: shift to json
    check_folder(STD_STATS_FOLDER)
    with open(
        STD_STATS_FOLDER + "geotiff_metadata_header_bin.pickle", "wb"
    ) as f:  # TODO: improve magic constant
        pickle.dump(data, f)
