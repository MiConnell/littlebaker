import calendar
import csv
import datetime
import json
import random
from beemovie import script

import numpy as np
import pandas as pd
from littletable import Table, DataObject


class make(object):
    def __repr__(self):
        return "Class for making dummy objects - lists, dictionaries, dataframes, matricies, arrays, json, csv (plus more to come!)"

    def a_list(self, length=101) -> list:
        self.length = length
        return [i for i in range(self.length)]

    def a_dict(self) -> dict:
        alpha = [
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
        return {a: n for a, n in enumerate(alpha)}

    def a_df(self, n=100) -> pd.DataFrame:

        self.n = n

        def date_generator():
            month = random.randint(1, 12)
            year = random.randint(1950, datetime.datetime.now().year)
            dates = calendar.Calendar().itermonthdates(year, month)
            return random.choice([date for date in dates if date.year == year])

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
        # TODO

    def an_array(self) -> np.array:
        pass
        # TODO

    def some_json(self):
        pass
        # TODO

    def a_csv(self, filename="./littlechef.csv"):
        self.filename = filename
        self.a_df().to_csv(self.filename)
        return f"csv {self.filename} created!"


"""
## TODO
list - default types to int but allow specifying desired type
matrix - anything
json - anything
array - anything

"""
