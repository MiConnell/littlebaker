import calendar
import datetime
import json
import random
from typing import List
import csv

import numpy as np
import pandas as pd

try:
    from littlechef import beemovie
except ImportError as e:
    import beemovie  # noqa

pd.options.display.max_columns = 8

current_year = datetime.datetime.now().year


def date_generator(
    num_dates: int = 1,
    start_year: int = 1950,
    end_year: int = current_year,
    as_list: bool = False,
):
    """
    Function to generate date(s). Specify the number of dates (num_dates, defaults to 1), start year (start_year, defaults to 1950),
    end year (end_year, defaults to the current year), and whether you'd like the resuts as a list (as_list, defaults to False)
    """
    if num_dates <= 0:
        raise ValueError("Number of dates must be greater than zero")
    if start_year > end_year:
        raise ValueError("start_year must be less than or equal to end_year")
    if start_year < 1:
        raise ValueError("start_year must be greater than 0")
    if not as_list:
        if num_dates == 1:
            year = random.randint(start_year, end_year)
            month = random.randint(1, 12)
            dates = calendar.Calendar().itermonthdates(year, month)
            date_list = [date for date in dates if start_year <= date.year <= end_year]
        else:
            while num_dates > 1:
                year = random.randint(start_year, end_year)
                month = random.randint(1, 12)
                dates = calendar.Calendar().itermonthdates(year, month)
                date_list = [
                    date for date in dates if start_year <= date.year <= end_year
                ]
                print(random.choice(date_list))
                num_dates -= 1
        return random.choice(date_list)
    date_res = (
        []
    )  # list comprehension doesn't work very well since the year is not randomly chosen inline :(
    for _ in range(num_dates):
        year = random.randint(start_year, end_year)
        month = random.randint(1, 12)
        dates = calendar.Calendar().itermonthdates(year, month)
        date_list = [date for date in dates if start_year <= date.year <= end_year]
        date_res.append(str(random.choice(date_list)))
    return date_res


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
        """

        Method to create a list. Specify the length (length, default is 101) and data type (data_type, default is 'int', options are:

        int - return list of integers

        float - return list of floats

        char - return list of characters ['a', 'b', 'c']

        date - return list of dates

        str - return list of strings (these just so happen to be from the bee movie script)

        )

        """
        self.length = length
        self.data_type = data_type
        if self.length <= 0:
            raise ValueError("Length must be greater than 0")
        if self.data_type == "int":
            return [i for i in range(self.length)]
        elif self.data_type == "float":
            return [round(random.random() * 100, 3) for _ in range(self.length)]
        elif self.data_type == "char":
            return [random.choice(self.alpha) for _ in range(self.length)]
        elif self.data_type == "date":
            return [str(date_generator()) for _ in range(self.length)]
        elif self.data_type == "str":
            if self.length > len(beemovie.honey):
                raise ValueError(
                    f"Maximum allowed length for data_type `str` is {len(beemovie.honey)}"
                )
            if self.length == len(beemovie.honey):
                return beemovie.honey
            start = random.randint(0, len(beemovie.honey) - (self.length - 1))
            return beemovie.honey[start:(start + self.length)]
        else:
            raise ValueError(
                f"data_type `{self.data_type}` not recognized. Valid options are 'int', 'float', 'char', 'date', or 'str'"
            )

    def a_dict(
        self, length: int = 101, key_type: str = "int", value_type: str = "char"
    ) -> dict:
        self.length = length
        self.key_type = key_type
        self.value_type = value_type
        return {
            a: n
            for a, n in enumerate(random.choice(self.alpha) for _ in range(self.length))
        }

    def a_df(self, n: int = 100) -> pd.DataFrame:

        self.n = n

        self.df = pd.DataFrame(
            [
                [
                    random.randint(1, 1000),
                    random.random() + random.randint(1, 1000),
                    beemovie.script(),
                    False,
                    True,
                    np.nan,
                    date_generator(),
                ]
                for _ in range(n)
            ],
            columns=[
                "col_int",
                "col_float",
                "col_string",
                "col_boolFalse",
                "col_boolTrue",
                "col_npNan",
                "col_datetime",
            ],
        )
        self.df["col_datetime"] = pd.to_datetime(self.df["col_datetime"])
        return self.df

    def a_matrix(
        self, num_lists: int = 5, list_length: int = 5, value_type: str = "all"
    ) -> List[list]:
        self.num_lists = num_lists
        self.list_length = list_length
        self.value_type = value_type
        if self.value_type not in ("all", "int", "float", "str", "char", "date"):
            raise ValueError(
                f"value_type {self.value_type} not allowed. Valid options are 'int', 'float', 'str', 'char', 'date', or 'all'"
            )
        if self.value_type == "all" and self.num_lists != 5:
            raise ValueError("num_lists must be 5 for value_type 'all'")
        if self.value_type == "all":
            sublists = [
                self.a_list(data_type="int", length=self.list_length),
                self.a_list(data_type="float", length=self.list_length),
                self.a_list(data_type="str", length=self.list_length),
                self.a_list(data_type="char", length=self.list_length),
                self.a_list(data_type="date", length=self.list_length),
            ]
        else:
            sublists = [
                self.a_list(length=self.list_length, data_type=self.value_type)
                for _ in range(self.num_lists)
            ]
        return [s for s in sublists]

    def an_array(self, matrix: List[list]) -> np.array:
        self.matrix = matrix
        return np.array(self.matrix)

    def some_json(self, value_length: int = 5) -> json:
        self.value_length = value_length
        self.int_list = self.a_list(length=4)
        self.value_list = [
            self.a_list(length=self.value_length),
            self.a_list(length=self.value_length, data_type="char"),
            self.a_list(length=self.value_length, data_type="date"),
            self.a_list(length=self.value_length, data_type="str"),
        ]
        self.data = {a: s for a, s in zip(self.int_list, self.value_list)}
        return json.dumps(self.data)

    def a_csv(self, filename="./littlechef.csv", rows: int = 100) -> csv:
        self.filename = filename
        self.rows = rows
        self.a_df(n=self.rows).to_csv(self.filename)
        return f"csv {self.filename} created!"


make = make()
