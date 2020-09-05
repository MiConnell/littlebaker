# littlechef

![littlechef](https://user-images.githubusercontent.com/14168559/92290502-2a13cf80-eec9-11ea-9dd7-f460c6bef14b.png)

littlechef is your personal Python chef to create custom lists, dictionaries, matricies (lists of lists), [numpy arrays](https://numpy.org/doc/stable/reference/generated/numpy.array.html), csv files, in-memory json blobs, and [Pandas DataFrames](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

All it takes is

    from littlechef import littlechef

    chef_list = littlechef.make.a_list() # returns list
    chef_dict = littlechef.make.a_dict() # returns dictionary
    chef_matrix = littlechef.make.a_matrix() # returns a list-of-lists
    chef_array = littlechef.make.an_array() # returns numpy array
    chef_json = littlechef.make.some_json() # returns json
    chef_csv = littlechef.make.a_csv() # creates a csv file
    chef_df = littlechef.make.a_df() # returns Pandas DataFrame

## Installation

simply install littlechef via pip `pip install littelchef`
