import pandas as pd
import re

def find_non_alphanumeric(dataframe, selected_columns):
    """
    Finds non-alphanumeric characters or spaces in the values of selected columns.

    Parameters:
    dataframe (pd.DataFrame): DataFrame containing the data.
    selected_columns (list): List of column names to check.

    Returns:
    dict: Dictionary where keys are column names and values are lists of rows with non-alphanumeric characters.
    """
    non_alphanumeric_dict = {}

    # Iterate over each selected column
    for column in selected_columns:
        non_alphanumeric_rows = []

        # Iterate over each row and check for non-alphanumeric characters
        for index, value in dataframe[column].items():
            if not pd.isna(value) and re.search(r'[^a-zA-Z0-9\s]', str(value)):
                non_alphanumeric_rows.append(index)

        # Store the rows with non-alphanumeric characters in the dictionary
        non_alphanumeric_dict[column] = non_alphanumeric_rows

    return non_alphanumeric_dict

if __name__ == "__main__":
    # Example DataFrame
    df = pd.DataFrame({
        'cola': ['abc123', 'def456', 'ghi789', 'jkl 10'],
        'colb': ['pqr321', 'st!456', 'uvw 89', 'xyz#@!'],
        'colc': ['123456', 'abc', 'def', 'xyz'],
        'cold': ['foo bar', 'baz', 'qux123', '123!']
    })

    # Selected column names to check
    selected_columns = ['cola', 'colb', 'colc', 'cold']

    # Find non-alphanumeric characters in selected columns
    non_alphanumeric_info = find_non_alphanumeric(df, selected_columns)
    print("Non-alphanumeric characters found in selected columns:")
    print(non_alphanumeric_info)
