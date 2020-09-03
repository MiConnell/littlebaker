import calendar
import datetime
import json
import random

import numpy as np
import pandas as pd
from littletable import DataObject, Table

from beemovie import script  # noqa


def date_generator(num_dates=1, start_year=1950, end_year=datetime.datetime.now().year):
    if num_dates <= 0:
        raise ValueError("Number of dates must be greater than zero")
    while num_dates > 1 and num_dates is not None:
        year = random.randint(start_year, end_year)
        month = random.randint(1, 12)
        dates = calendar.Calendar().itermonthdates(year, month)
        date_list = [date for date in dates if start_year <= date.year <= end_year]
        print(random.choice(date_list))
        num_dates -= 1
    return random.choice(date_list)


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

    def a_dict(self, length: int = 101, data_type: str = "int") -> dict:
        self.length = length
        self.data_type = data_type
        return {a: n for a, n in enumerate(self.alpha)}

    def a_df(self, n: int = 100) -> pd.DataFrame:

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

    def some_json(self) -> json:
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
list - allow mixed types in list/dicts
matrix - anything
json - anything
array - anything

"""
