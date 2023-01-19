

def remove_extra_rows(full_df):
    """Function to remove all rows with the value 'United States' in each column."""

    # These rows just have the value 'United States' in every column.
    extra_row_indexes = [
        28, 203, 229, 258, 316, 357, 487, 536, 537,
        558, 640, 661, 803, 865, 884, 943, 948,
        1062, 1166, 1210, 1211
    ]
    altered_df = full_df.drop(labels=extra_row_indexes, axis=0)
    return altered_df
