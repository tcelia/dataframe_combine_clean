import pandas as pd
import re

def clean_columns(dataframe, selected_columns):
    """
    Removes non-alphanumeric characters and extra spaces from values in selected columns.

    Parameters:
    dataframe (pd.DataFrame): DataFrame containing the data.
    selected_columns (list): List of column names to clean.

    Returns:
    pd.DataFrame: DataFrame with selected columns cleaned.
    """
    cleaned_dataframe = dataframe.copy()

    # Iterate over each selected column
    for column in selected_columns:
        # Remove non-alphanumeric characters and extra spaces from values
        cleaned_dataframe[column] = cleaned_dataframe[column].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', str(x)))
        cleaned_dataframe[column] = cleaned_dataframe[column].apply(lambda x: re.sub(r'\s+', ' ', x.strip()))

    return cleaned_dataframe

if __name__ == "__main__":
    # Example DataFrame
    df = pd.DataFrame({
        'cola': ['abc 123', 'def!456', 'ghi 789', 'jkl 10'],
        'colb': ['pqr321', 'st  456', 'uvw   89', 'xyz#@!'],
        'colc': ['123456', 'abc', 'def', 'xyz'],
        'cold': ['foo bar', 'baz', 'qux  123', '123!']
    })

    # Selected column names to clean
    selected_columns = ['cola', 'colb', 'colc', 'cold']

    # Clean selected columns
    cleaned_df = clean_columns(df, selected_columns)
    print("DataFrame after cleaning selected columns:")
    print(cleaned_df)
