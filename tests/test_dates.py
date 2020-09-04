from littlechef import littlechef
import datetime
import pytest


def test_date_generator():
    assert type(littlechef.date_generator()) is datetime.date
    assert type(littlechef.date_generator(as_list=True)) is list
    assert type(littlechef.date_generator(as_list=False)) is not list
    assert len(littlechef.date_generator(as_list=True, num_dates=20)) == 20
    with pytest.raises(ValueError):
        littlechef.date_generator(num_dates=-1)
    with pytest.raises(ValueError):
        littlechef.date_generator(start_year=-9)
    with pytest.raises(ValueError):
        littlechef.date_generator(end_year=-9)
    with pytest.raises(ValueError):
        littlechef.date_generator(start_year=2010, end_year=1999)
