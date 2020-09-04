from littlechef import littlechef
import pytest
import pandas as pd
import numpy as np
import datetime


def test_list_creation():
    assert type(littlechef.make.a_list(length=1)) is list
    assert len(littlechef.make.a_list()) == 101
    assert len(littlechef.make.a_list(length=5)) == 5
    assert len(littlechef.make.a_list(length=5, data_type="int")) == 5
    assert len(littlechef.make.a_list(length=5, data_type="float")) == 5
    assert len(littlechef.make.a_list(length=5, data_type="char")) == 5
    assert len(littlechef.make.a_list(length=5, data_type="str")) == 5
    assert len(littlechef.make.a_list(length=5, data_type="date")) == 5
    assert type(littlechef.make.a_list(length=1)[0]) is int
    assert type(littlechef.make.a_list(length=1, data_type="int")[0]) is int
    assert type(littlechef.make.a_list(length=1, data_type="char")[0]) is str
    assert type(littlechef.make.a_list(length=1, data_type="float")[0]) is float
    assert type(littlechef.make.a_list(length=1, data_type="str")[0]) is str
    assert type(littlechef.make.a_list(length=1, data_type="date")[0]) is str
    with pytest.raises(ValueError):
        littlechef.make.a_list(-1)
    with pytest.raises(ValueError):
        littlechef.make.a_list(data_type="not allowed")


def test_dict_creation():
    assert len(littlechef.make.a_dict()) == 101
    assert len(littlechef.make.a_dict(length=5)) == 5
    assert type(littlechef.make.a_dict(length=1)) is dict

def test_df_creation():
    assert len(littlechef.make.a_df()) == 100
    assert len(littlechef.make.a_df(n=1)) == 1
    assert type(littlechef.make.a_df()) == pd.DataFrame
    assert type(littlechef.make.a_df()['col_int'][0]) is np.int64
    assert type(littlechef.make.a_df()['col_float'][0]) is np.float64
    assert type(littlechef.make.a_df()['col_string'][0]) is str
    assert type(littlechef.make.a_df()['col_boolTrue'][0]) is np.bool_
    assert type(littlechef.make.a_df()['col_boolFalse'][0]) is np.bool_
    assert type(littlechef.make.a_df()['col_npNan'][0]) is np.float64
    assert type(littlechef.make.a_df()['col_datetime'][0]) is not str
