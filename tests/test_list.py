from littlechef import littlechef
import pytest


def test_list_creation():
    assert len(littlechef.make.a_list()) == 101
    assert len(littlechef.make.a_list(length=5)) == 5
    assert type(littlechef.make.a_list(length=1, data_type='int')[0]) is int
    assert type(littlechef.make.a_list(length=1, data_type='char')[0]) is str
    assert type(littlechef.make.a_list(length=1, data_type='float')[0]) is float
    assert type(littlechef.make.a_list(length=1, data_type='str')[0]) is str
    assert type(littlechef.make.a_list(length=1, data_type='date')[0]) is str
    with pytest.raises(ValueError):
        littlechef.make.a_list(-1)
