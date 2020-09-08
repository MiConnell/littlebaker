# Numbered comments are defined in the index at the end of the file
import calendar
import csv
import datetime
import json
import random
import string
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd

try:
    import beemovie  # noqa
except ImportError:
    from . import beemovie

pd.options.display.max_columns = 8  # 2

current_year = datetime.datetime.now().year


# Generate dates
def date_generator(
    num_dates: int = 1,
    start_year: int = 1950,
    end_year: int = current_year,
    as_list: bool = False,
):
    """
    Function to generate date(s). Specify the number of dates (num_dates, defaults to 1),\n
    start year (start_year, defaults to 1950),\n
    end year (end_year, defaults to the current year),\n
    and whether you'd like the resuts as a list (as_list, defaults to False)
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
            date_list = [
                date for date in dates
                if start_year <= date.year <= end_year
            ]
        else:
            while num_dates > 1:
                year = random.randint(start_year, end_year)
                month = random.randint(1, 12)
                dates = calendar.Calendar().itermonthdates(year, month)
                date_list = [
                    date for date in dates
                    if start_year <= date.year <= end_year
                ]
                print(random.choice(date_list))
                num_dates -= 1
        return random.choice(date_list)
    date_res = []
    for _ in range(num_dates):
        year = random.randint(start_year, end_year)
        month = random.randint(1, 12)
        dates = calendar.Calendar().itermonthdates(year, month)
        date_list = [
            date for date in dates
            if start_year <= date.year <= end_year
        ]
        date_res.append(str(random.choice(date_list)))
    return date_res


class make(object):
    def __init__(self):
        self.alpha = string.ascii_lowercase  # 3

    def __repr__(self):
        return "Class for making dummy objects - lists, dictionaries, dataframes, matricies, arrays, json, and csv files"

    # Generate lists
    def a_list(
        self,
        length: int = 101,
        data_type: str = "int"
    ) -> list:
        """
        Creates a list. Specify the length (length, default is 101) and data type (data_type, default is 'int', options are:\n
        int - return list of integers\n
        float - return list of floats\n
        char - return list of characters ['a', 'b', 'c']\n
        date - return list of dates\n
        str - return list of strings (these just so happen to be from the bee movie script)\n
        )
        """
        self.length = length
        self.data_type = data_type
        if self.length <= 0:
            raise ValueError("Length must be greater than 0")
        if self.data_type == "int":
            return list(range(self.length))
        elif self.data_type == "float":
            return [
                round(random.random() * 100, 3)
                for _ in range(self.length)
            ]
        elif self.data_type == "char":
            return [
                random.choice(self.alpha)
                for _ in range(self.length)
            ]
        elif self.data_type == "date":
            return [
                str(date_generator())
                for _ in range(self.length)
            ]
        elif self.data_type == "str":
            if self.length > len(beemovie.honey):
                raise ValueError(
                    f"Maximum allowed length for data_type `str` is {len(beemovie.honey)}"
                )
            if self.length == len(beemovie.honey):
                return beemovie.honey
            start = random.randint(
                0,
                len(beemovie.honey) - (self.length - 1)
            )
            return beemovie.honey[start:(start + self.length)]
        else:
            raise ValueError(
                f"data_type `{self.data_type}` not recognized. Valid options are 'int', 'float', 'char', 'date', or 'str'"
            )

    # Generate dictionary
    def a_dict(
        self,
        length: int = 101,
        value_type: str = "char"
    ) -> dict:
        """
        Generates a dictionary. Specify the length (length, defaults to 101)\n
        and value type (value_type, defaults to 'char')
        """
        self.length = length
        self.value_type = value_type
        if self.length <= 0:
            raise ValueError("length must be greater than 0")
        if self.value_type not in ("char", "int", "float", "str", "date"):
            raise ValueError(f"Invalid value_type of `{self.value_type}`. Valid options are 'int', 'float', 'char', 'date', or 'str'")
        if self.value_type == "char":
            return dict(
                enumerate(random.choice(self.alpha) for _ in range(self.length))
            )
        elif self.value_type == "int":
            return dict(
                enumerate(range(self.length))
            )
        elif self.value_type == "float":
            return dict(
                round(random.random() * 100, 3) for _ in range(self.length)
            )
        elif self.value_type == "str":
            return dict(
                enumerate(random.choice(beemovie.honey) for _ in range(self.length))
            )
        elif self.value_type == "date":
            return dict(
                enumerate(str(date_generator()) for _ in range(self.length))
            )

    # Generate Pandas DataFrame
    def a_df(
        self,
        n: int = 100
    ) -> pd.DataFrame:
        """
        Generates a Pandas DataFrame with 7 columns and n rows (n, defaults to 100).\n
        Columns are all various types:\n
        int      - col_int
        float    - col_float
        string   - col_string
        False    - col_boolFalse
        True     - col_boolTrue
        NaN      - col_npNan
        datetime - col_datetime
        """

        self.n = n

        self.df = pd.DataFrame(
            [
                [
                    random.randint(1, 1000),
                    random.random() + random.randint(1, 1000),
                    beemovie.script(),  # 4
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

    # Generate a matrix (list of lists)
    def a_matrix(
        self,
        num_lists: int = 5,
        list_length: int = 5,
        value_type: str = "all"
    ) -> List[list]:
        """
        Generates a matrix (list of lists). Arguments are:\n
        num_lists (how many lists to generate in the list, defaults to 5),\n
        list_length (how long the inner lists should be, defaults to 5), \n
        value_type (desired type for inner lists, options are 'int', 'float', 'str', 'char', 'date', or 'all'. Defaults to 'all').\n
        value_type of 'all' will create 5 inner lists of all types above.
        """
        self.num_lists = num_lists
        self.list_length = list_length
        self.value_type = value_type
        if self.num_lists <= 0:
            raise ValueError("num_lists must be greater than 0")
        if self.list_length <= 0:
            raise ValueError("list_length must be greater than 0")
        if self.value_type not in (
            "all",
            "int",
            "float",
            "str",
            "char",
            "date"
        ):
            raise ValueError(
                f"value_type {self.value_type} not allowed. Valid options are 'int', 'float', 'str', 'char', 'date', or 'all'"
            )
        if self.value_type == "all" and self.num_lists != 5:
            raise ValueError("num_lists must be 5 for value_type 'all'")
        if self.value_type == "all":
            of_lists = [
                self.a_list(data_type="int", length=self.list_length),
                self.a_list(data_type="float", length=self.list_length),
                self.a_list(data_type="str", length=self.list_length),
                self.a_list(data_type="char", length=self.list_length),
                self.a_list(data_type="date", length=self.list_length),
            ]
        else:
            of_lists = [
                self.a_list(length=self.list_length, data_type=self.value_type)
                for _ in range(self.num_lists)
            ]
        return list(of_lists)

    # Generate numpy array
    def an_array(self, matrix: List[list] = "default") -> np.array:
        """
        Generates a numpy array. Defaults to creating an array generated from the default littlebaker.make.a_matrix(), \n
        but any valid list can be passed as an argument (including a custom littlebaker.make.a_matrix())
        """
        self.matrix = matrix
        if matrix == "default":
            self.matrix = self.a_matrix()
            return np.array(self.matrix)
        return np.array(self.matrix)

    # Generate json
    def some_json(
        self,
        value_length: int = 5
    ) -> json:
        """
        Generates in-memory json.\n
        Specify the value_length (defaults to 5) which specifies the length of the values in the key:value of the blob.
        """
        self.value_length = value_length
        self.int_list = self.a_list(length=5)
        self.value_list = [
            self.a_list(length=self.value_length),
            self.a_list(length=self.value_length, data_type="char"),
            self.a_list(length=self.value_length, data_type="date"),
            self.a_list(length=self.value_length, data_type="str"),
            self.a_list(length=self.value_length, data_type="float"),
        ]
        self.data = dict(zip(self.int_list, self.value_list))
        return json.dumps(self.data, indent=4)

    # Generate and save a csv
    def a_csv(
        self,
        path=Path.cwd(),
        filename: str = "littlebaker.csv",
        rows: int = 100,
        df: pd.DataFrame = "default",
    ) -> csv:
        """
        Generates and saves a csv file. Specify the path to save (path, defaults to the current directory),\n
        file name (filename, defaults to 'littlebaker.csv'),\n
        number of rows (rows, defaults to 100),\n
        and dataframe to use (df, defaults to littlebaker.make.a_df())
        """
        self.filename = filename
        self.path = path
        self.rows = rows
        self.df = df
        if type(self.df) is not pd.DataFrame:
            raise TypeError(
                f"df '{self.df}' of type {type(self.df)} is not of correct type 'Pandas DataFrame'"
            )
        if self.path == Path.cwd():
            self.destination = Path(fr"{self.path}/{self.filename}")
        elif path[-1] in ("/", "\\"):
            self.destination = Path(fr"{self.path}{self.filename}")
        else:
            self.destination = Path(fr"{self.path}/{self.filename}")
        if self.df == "default":
            self.a_df(n=self.rows).to_csv(self.destination)
        else:
            self.df.to_csv(self.destination)
        print(f"csv {self.destination} created!")


make = make()


"""INDEX"""
# 1 Bee Movie script - useful for generating random words/sentences
# 2 Option to print out all columns in Pandas DataFrame when returned
# 3 Lowercase American English alphabet
# 4 Random segments of the Bee Movie script
