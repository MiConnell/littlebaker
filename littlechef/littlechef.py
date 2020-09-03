import calendar
import datetime
import json
import random
from typing import List

import numpy as np
import pandas as pd

from beemovie import script  # noqa

pd.options.display.max_columns = 8


def date_generator(
    num_dates: int = 1,
    start_year: int = 1950,
    end_year: int = datetime.datetime.now().year,
    as_list: bool = False,
):
    """
    Function to generate date(s). Specify the number of dates (num_dates, defaults to 1), start year (start_year, defaults to 1950),
    end year (end_year, defaults to the current year), and whether you'd like the resuts as a list (as_list, defaults to False)
    """
    if num_dates <= 0:
        raise ValueError("Number of dates must be greater than zero")
    if not as_list:
        if num_dates == 1:
            year = random.randint(start_year, end_year)
            month = random.randint(1, 12)
            dates = calendar.Calendar().itermonthdates(year, month)
            date_list = [date for date in dates if start_year <= date.year <= end_year]
            return random.choice(date_list)
        while num_dates > 1:
            year = random.randint(start_year, end_year)
            month = random.randint(1, 12)
            dates = calendar.Calendar().itermonthdates(year, month)
            date_list = [date for date in dates if start_year <= date.year <= end_year]
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
        self.length = length
        self.data_type = data_type
        if self.data_type == "int":
            return [i for i in range(self.length)]
        elif self.data_type == "str":
            return [a for i, a in enumerate(self.alpha) if i < self.length]
        elif self.data_type == "date":
            return [str(date_generator()) for _ in range(self.length)]
        elif self.data_type == "words":
            return script().split()[0:self.length]
        else:
            raise ValueError(
                f"data_type `{self.data_type}` not recognized. Valid options are 'int', 'str', 'date', or 'words'"
            )

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

    def a_matrix(self) -> List[list]:
        pass

    def an_array(self) -> np.array:
        pass

    def some_json(self) -> json:
        self.int_list = self.a_list(length=5)
        self.value_list = [
            self.a_list(length=5),
            self.a_list(length=5, data_type="str"),
            self.a_list(length=5, data_type="date"),
            self.a_list(length=5, data_type="words"),
        ]
        self.data = {a: s for a, s in zip(self.int_list, self.value_list)}
        return json.dumps(self.data)

    def a_csv(self, filename="./littlechef.csv"):
        self.filename = filename
        self.a_df().to_csv(self.filename)
        return f"csv {self.filename} created!"
