from littlebaker import littlebaker
import pytest
import pandas as pd
import numpy as np
import datetime
import json
from typing import List


def test_list_creation():
    assert type(littlebaker.make.a_list(length=1)) is list
    assert len(littlebaker.make.a_list()) == 101
    assert len(littlebaker.make.a_list(length=5)) == 5
    assert len(littlebaker.make.a_list(length=5, data_type="int")) == 5
    assert len(littlebaker.make.a_list(length=5, data_type="float")) == 5
    assert len(littlebaker.make.a_list(length=5, data_type="char")) == 5
    assert len(littlebaker.make.a_list(length=5, data_type="str")) == 5
    assert len(littlebaker.make.a_list(length=5, data_type="date")) == 5
    assert type(littlebaker.make.a_list(length=1)[0]) is int
    assert type(littlebaker.make.a_list(length=1, data_type="int")[0]) is int
    assert type(littlebaker.make.a_list(length=1, data_type="char")[0]) is str
    assert type(littlebaker.make.a_list(length=1, data_type="float")[0]) is float
    assert type(littlebaker.make.a_list(length=1, data_type="str")[0]) is str
    assert type(littlebaker.make.a_list(length=1, data_type="date")[0]) is str
    with pytest.raises(ValueError):
        littlebaker.make.a_list(-1)
    with pytest.raises(ValueError):
        littlebaker.make.a_list(data_type="not allowed")
    with pytest.raises(ValueError):
        littlebaker.make.a_list(data_type="str", length=999999)


def test_dict_creation():
    assert len(littlebaker.make.a_dict()) == 101
    assert len(littlebaker.make.a_dict(length=5)) == 5
    assert type(littlebaker.make.a_dict(length=1)) is dict
    with pytest.raises(ValueError):
        littlebaker.make.a_dict(length=-1)
    with pytest.raises(ValueError):
        littlebaker.make.a_dict(value_type='invalid')


def test_df_creation():
    assert len(littlebaker.make.a_df()) == 100
    assert len(littlebaker.make.a_df(n=1)) == 1
    assert type(littlebaker.make.a_df()) == pd.DataFrame
    assert type(littlebaker.make.a_df()["col_int"][0]) is np.int64
    assert type(littlebaker.make.a_df()["col_float"][0]) is np.float64
    assert type(littlebaker.make.a_df()["col_string"][0]) is str
    assert type(littlebaker.make.a_df()["col_boolTrue"][0]) is np.bool_
    assert type(littlebaker.make.a_df()["col_boolFalse"][0]) is np.bool_
    assert type(littlebaker.make.a_df()["col_npNan"][0]) is np.float64
    assert type(littlebaker.make.a_df()["col_datetime"][0]) is not str


def test_json_creation():
    baker_json = json.loads(littlebaker.make.some_json())
    baker_json_len_ten = json.loads(littlebaker.make.some_json(value_length=10))
    assert len(baker_json['0']) == 5
    assert len(baker_json_len_ten['0']) == 10

def test_matrix_creation():
    assert type(littlebaker.make.a_matrix()) is list
    assert len(littlebaker.make.a_matrix()) == 5
    assert len(littlebaker.make.a_matrix()[0]) == 5
    with pytest.raises(ValueError):
        littlebaker.make.a_matrix(num_lists=10)
    with pytest.raises(ValueError):
        littlebaker.make.a_matrix(value_type='not valid')
    with pytest.raises(ValueError):
        littlebaker.make.a_matrix(num_lists=-1, value_type='int')
    with pytest.raises(ValueError):
        littlebaker.make.a_matrix(list_length=-1, value_type='int')
    with pytest.raises(ValueError):
        littlebaker.make.a_matrix(num_lists=0, value_type='int')
    with pytest.raises(ValueError):
        littlebaker.make.a_matrix(list_length=0, value_type='int')
    assert type(littlebaker.make.a_matrix(value_type='str')[0][0]) is str
    assert type(littlebaker.make.a_matrix(value_type='char')[0][0]) is str
    assert type(littlebaker.make.a_matrix(value_type='int')[0][0]) is int
    assert type(littlebaker.make.a_matrix(value_type='float')[0][0]) is float
    assert type(littlebaker.make.a_matrix(value_type='date')[0][0]) is str


def test_array_creation():
    mtr = littlebaker.make.a_matrix()
    assert type(littlebaker.make.an_array(mtr)) is np.ndarray
    with pytest.raises(TypeError):
        littlebaker.make.an_array(matrix=0)

def test_csv_creation():
    baker_csv = littlebaker.make.a_csv()
    with pytest.raises(TypeError):
        littlebaker.make.a_csv(df='a')
    with pytest.raises(ValueError):
        littlebaker.make.a_csv(path='notavalidpath')
    with pytest.raises(ValueError):
        littlebaker.make.a_csv(filename='notavalidname')
    with pytest.raises(ValueError):
        littlebaker.make.a_csv(rows=-9)
    with pytest.raises(TypeError):
        littlebaker.make.a_csv(index=10)
