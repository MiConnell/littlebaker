import pandas as pd
import numpy as np
import json
import csv
import datetime
import random
import calendar


class make(object):
    def a_list(self, length=101):
        self.length = length
        return [i for i in range(self.length)]

    def a_dict(self):
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

    def a_df(self, n=100):

        self.n = n

        def date_generator():
            month = random.randint(1, 12)
            year = random.randint(1950, datetime.datetime.now().year)
            dates = calendar.Calendar().itermonthdates(year, month)
            return random.choice([date for date in dates if date.year == year])

        return pd.DataFrame(
            [
                [
                    1,
                    15.5,
                    "xyz",
                    False,
                    True,
                    np.nan,
                    date_generator(),
                ]
                for _ in range(n)
            ],
            columns=["A", "B", "C", "D", "E", "F", "G"],
        )

    def a_matrix(self):
        pass

    def an_array(self):
        pass

    def some_json(self):
        pass

    def a_csv(self):
        pass
