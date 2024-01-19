"""
    dataclasses resumed info: https://www.youtube.com/watch?v=vBH6GRJ1REM
"""

import sys, inspect
from pprint import pprint
from dataclasses import dataclass, field

__default_argument = "--just-checking"


@dataclass
class Metadata:
    code: int


@dataclass
class Point:
    lat: float
    long: float


@dataclass
class Datapoint:
    ID: int
    point: Point


#############
def __just_checking():
    p = Point(1.1, 2.2)
    print(p)

    d = Datapoint(123, p)
    print(d)


if __name__ == "__main__":
    if __default_argument in sys.argv:
        __just_checking()

        pprint(inspect.getmembers(Point, inspect.isfunction))
        pprint(inspect.getmembers(Metadata, inspect.isfunction))
        pprint(inspect.getmembers(Datapoint, inspect.isfunction))
