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


"""
def date_generator(
    num_dates: int = 1,
    start_year: int = 1950,
    end_year: int = current_year,
    as_list: bool = False,
):
    """ """
    Function to generate date(s). Specify the number of dates(num_dates, defaults to 1), start year(start_year, defaults to 1950),
    end year(end_year, defaults to the current year), and whether you'd like the resuts as a list(as_list, defaults to False)
    """ """
    if num_dates <= 0:
        raise ValueError("Number of dates must be greater than zero")
    if not as_list:
        if num_dates == 1:
            year = random.randint(start_year, end_year)
            month = random.randint(1, 12)
            dates = calendar.Calendar().itermonthdates(year, month)
            date_list = [date for date in dates if start_year <= date.year <= end_year]
        else:
            while num_dates > 1:
                year = random.randint(start_year, end_year)
                month = random.randint(1, 12)
                dates = calendar.Calendar().itermonthdates(year, month)
                date_list = [
                    date for date in dates if start_year <= date.year <= end_year
                ]
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
"""
