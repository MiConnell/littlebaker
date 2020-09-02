import calendar
import datetime
import json
import random

import numpy as np
import pandas as pd
from littletable import DataObject, Table

from beemovie import script


def date_generator(start_year=1950):
    month = random.randint(1, 12)
    year = random.randint(start_year, datetime.datetime.now().year)
    dates = calendar.Calendar().itermonthdates(year, month)
    return random.choice([date for date in dates if date.year == year])


class make(object):
    def __init__(self):
        self.alpha = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

    def __repr__(self):
        return "Class for making dummy objects - lists, dictionaries, dataframes, matricies, arrays, json, csv (plus more to come!)"

    def a_list(self, length: int = 101, data_type: str = "int") -> list:
        self.length = length
        self.data_type = data_type
        if self.data_type == "int":
            littlelist = [i for i in range(self.length)]
        elif self.data_type == "str":
            littlelist = [a for a in self.alpha]
        elif self.data_type == "date":
            littlelist = [str(date_generator()) for _ in range(self.length)]
        elif self.data_type == "words":
            littlelist = script().split()
        else:
            raise ValueError(
                f"data_type `{self.data_type}` not recognized. Valid options are 'int', 'str', 'date', or 'words'"
            )
        return littlelist

    def a_dict(self) -> dict:
        return {a: n for a, n in enumerate(self.alpha)}

    def a_df(self, n=100) -> pd.DataFrame:

        self.n = n

        return pd.DataFrame(
            [
                [
                    random.randint(1, 1000),
                    random.random() + random.randint(1, 1000),
                    script(),
                    False,
                    True,
                    np.nan,
                    date_generator(),
                ]
                for _ in range(n)
            ],
            columns=[
                "Col_int",
                "Col_float",
                "Col_string",
                "Col_boolFalse",
                "Col_boolTrue",
                "Col_npNan",
                "Col_datetime",
            ],
        )

    def a_matrix(self):
        pass

    def an_array(self) -> np.array:
        pass

    def some_json(self):
        pass

    def a_csv(self, filename="./littlechef.csv"):
        self.filename = filename
        self.a_df().to_csv(self.filename)
        return f"csv {self.filename} created!"


make = make()

"""
## TODO
TESTS
Readme updates
Comments/Docstrings
list - default types to int but allow specifying desired type
matrix - anything
json - anything
array - anything

"""
