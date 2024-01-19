import sys
import rasterio
import dataclasses
import numpy as np


def show_progress(string: str, max_value: float, actual_value: float):
    print(
        f"{string} {(actual_value * 100 / max_value):.3f}%                         ",
        end="\r",
        flush=True,
    )
    sys.stdout.flush()


@dataclasses.dataclass
class PixelData:
    latitude: float
    longitude: float
    pixel_value: float


def process_data_file(file: str):
    # Open GeoTIFF file
    with rasterio.open(file) as src:
        # Extract metadata
        projection = src.crs
        transform = src.transform
        width = src.width
        height = src.height
        bands = src.count

        # f = src.read()
        # print(np.array(f).shape)
        r = src.read(1)
        # print(np.array(r).shape)
        # l = src.read(1, window=(0, 0, 1, 1)[0])
        # print(l)
        # print(np.array(l).shape)

        # Iterate through pixels
        for y in range(height):
            show_progress(
                "        extracting pixel values: ", width * height, (y * width)
            )  # + x)
            for x in range(width):
                # Convert pixel coordinates to latitude and longitude
                lon, lat = rasterio.transform.rowcol(transform, y, x)

                # Extract pixel value
                # pixel_value = src.sample([(y, x)])
                pixel_value = r[y, x]
                # pixel_value = src.read(1, window=(y, x, 1, 1))[0][
                #    0
                # ]  # Extract pixel value from numpy array

                # Create dataclass instance
                pixel_data = PixelData(
                    latitude=lat, longitude=lon, pixel_value=r[y, x]
                )

                # present progress in console
