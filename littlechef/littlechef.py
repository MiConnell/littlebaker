import pandas as pd
import numpy as np
import json
import csv


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

    def a_df(self):
        pass

    def a_matrix(self):
        pass

    def an_array(self):
        pass

    def some_json(self):
        pass

    def a_csv(self):
        pass
