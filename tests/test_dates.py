from littlechef import littlechef
import datetime


def test_date_generator():
    assert type(littlechef.date_generator()) is datetime.date
