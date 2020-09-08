# littlebaker

![littlebaker](https://user-images.githubusercontent.com/14168559/92290502-2a13cf80-eec9-11ea-9dd7-f460c6bef14b.png)

littlebaker is your personal Python baker to create custom lists, dictionaries, matricies (lists of lists), [numpy arrays](https://numpy.org/doc/stable/reference/generated/numpy.array.html), csv files, in-memory json blobs, and [Pandas DataFrames](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

All it takes is

    from littlebaker import littlebaker

    baker_list = littlebaker.make.a_list() # returns list
    baker_dict = littlebaker.make.a_dict() # returns dictionary
    baker_matrix = littlebaker.make.a_matrix() # returns a list-of-lists
    baker_array = littlebaker.make.an_array() # returns numpy array
    baker_json = littlebaker.make.some_json() # returns json
    baker_csv = littlebaker.make.a_csv() # creates a csv file
    baker_df = littlebaker.make.a_df() # returns Pandas DataFrame

## Installation

simply install littlebaker via pip `pip install littelbaker`

## Examples and Usage

> a_list()
> a_dict()
> a_matrix()
> an_array()
> some_json()
> a_csv()
> a_df()
