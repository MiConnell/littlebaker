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

### littlebaker.make.a_list(length, data_type)

    length=
        any integer greater than 0, specifies list length, defaults to 101
    data_type=
        specifies the type of values in the returned list, defaults to `int`. Valid options are
            int: returns a list of integers
            float: returns a list of floats
            char: returns a list of single str characters
            date: returns a list of dates
            str: returns a list of random strings

### littlebaker.make.a_dict(length, value_type)

    length=
        any integer greater than 0, specifies dictionary length, defaults to 101
    value_type=
        specifies the type returned in the value of the dictionary's key:value pair, defaults to char.
        valid options are:
            int: returns a dictionary with keys of integers and values of integers
            float: returns a dictionary with keys of integers and values of floats
            char: returns a dictionary with keys of integers and values of single str characters
            date: returns a dictionary with keys of integers and values of dates
            str: returns a dictionary with keys of integers and values of random strings

### littlebaker.make.a_matrix(num_lists, list_length, value_type)

    num_lists=
        positive integer, specifies the number of lists within the returned matrix, defaults to 5
    list_length=
        positive integer, specifies the lentgh of the inner lists, defaults to 5
    value_type=
        specity the type returned in the inner lists, defaults to all
        int: returns inner lists of integers
        float: returns inner lists of floats
        char: returns inner lists of single str characters
        date: returns inner lists of dates
        str: returns inner lists of random strings
        all: returns inner lists of all of the above options. With this option, `num_lists` must be 5

### littlebaker.make.an_array(matrix)

    matrix=
        matrix to use to create the array, defaults to the default values in `littlebaker.make.a_matrix()`
        must be of type `List[list]`

### littlebaker.make.some_json(value_length)

    value_length=
        positive integer, specifies the length of the values returned in the resulting json, defaults to 5

### littlebaker.make.a_df(n)

    n=
        positive integer for the number of rows desired in the DataFrame, defaults to 100

### littlebaker.make.a_csv(path, filename, rows, df, index)

    path=
        filepath to desired save location, defaults to the current `.py` file's directory
    filename=
        desired name of file, defaults to `littlebaker.csv`
    rows=
        positive integer to specity number of rows desired in the csv file, defaults to 100
    df=
        Pandas DataFrame to be written to csv, defaults to `littlebaker.make.a_df()`
    index=
        boolean to specify if an index is desired in the resulting csv

littlebaker can also generate dates for you with `littlebaker.date_generator()`

## date_generator(num_dates, start_year, end_year, as_list)

    num_dates=
        positive integer to specify the number of dates desired to be returned, defaults to 1
    start_year=
        positive integer for the beginning year of the random date(s) to be returned, defaults 1950
    end_year=
        positive integer for the end year of the random date(s) to be returned, defaults to the current year
    as_list=
        boolean to specify if the date(s) returned should be in list form or as individual newline separated dates, defaults to False
