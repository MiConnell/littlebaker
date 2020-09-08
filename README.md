# littlebaker

![littlebaker](https://user-images.githubusercontent.com/14168559/92421136-ebca1a80-f12b-11ea-8f90-c69ade7a659c.png)

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

    littlebaker.make.
> a_list()
### length
> a_dict()
> a_matrix()
> an_array()
> some_json()
> a_csv()
> a_df()
