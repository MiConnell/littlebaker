from littlechef import littlechef
import pytest
import pandas as pd
import numpy as np
import datetime
import json
from typing import List


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
    with pytest.raises(ValueError):
        littlechef.make.a_list(data_type="str", length=999999)


def test_dict_creation():
    assert len(littlechef.make.a_dict()) == 101
    assert len(littlechef.make.a_dict(length=5)) == 5
    assert type(littlechef.make.a_dict(length=1)) is dict


def test_df_creation():
    assert len(littlechef.make.a_df()) == 100
    assert len(littlechef.make.a_df(n=1)) == 1
    assert type(littlechef.make.a_df()) == pd.DataFrame
    assert type(littlechef.make.a_df()["col_int"][0]) is np.int64
    assert type(littlechef.make.a_df()["col_float"][0]) is np.float64
    assert type(littlechef.make.a_df()["col_string"][0]) is str
    assert type(littlechef.make.a_df()["col_boolTrue"][0]) is np.bool_
    assert type(littlechef.make.a_df()["col_boolFalse"][0]) is np.bool_
    assert type(littlechef.make.a_df()["col_npNan"][0]) is np.float64
    assert type(littlechef.make.a_df()["col_datetime"][0]) is not str


def test_json_creation():
    chef_json = json.loads(littlechef.make.some_json())
    chef_json_len_ten = json.loads(littlechef.make.some_json(value_length=10))
    assert len(chef_json['0']) == 5
    assert len(chef_json_len_ten['0']) == 10

def test_matrix_creation():
    assert type(littlechef.make.a_matrix()) is list
    assert len(littlechef.make.a_matrix()) == 5
    assert len(littlechef.make.a_matrix()[0]) == 5
    with pytest.raises(ValueError):
        littlechef.make.a_matrix(num_lists=10)
    with pytest.raises(ValueError):
        littlechef.make.a_matrix(value_type='not valid')
    with pytest.raises(ValueError):
        littlechef.make.a_matrix(num_lists=-1, value_type='int')
    with pytest.raises(ValueError):
        littlechef.make.a_matrix(list_length=-1, value_type='int')
    with pytest.raises(ValueError):
        littlechef.make.a_matrix(num_lists=0, value_type='int')
    with pytest.raises(ValueError):
        littlechef.make.a_matrix(list_length=0, value_type='int')
    assert type(littlechef.make.a_matrix(value_type='str')[0][0]) is str
    assert type(littlechef.make.a_matrix(value_type='char')[0][0]) is str
    assert type(littlechef.make.a_matrix(value_type='int')[0][0]) is int
    assert type(littlechef.make.a_matrix(value_type='float')[0][0]) is float
    assert type(littlechef.make.a_matrix(value_type='date')[0][0]) is str


def test_array_creation():
    mtr = littlechef.make.a_matrix()
    assert type(littlechef.make.an_array(mtr)) is np.ndarray

def test_csv_creation():
    with pytest.raises(TypeError):
        littlechef.make.a_csv(df='a')
