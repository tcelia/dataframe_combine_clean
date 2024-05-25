import pandas as pd


def create_dataframes_from_files(file_list):
    """
    Takes a list of Excel file names, imports each file into a DataFrame,
    and returns a list of these DataFrames.

    Parameters:
    file_list (list of str): List of Excel file names.

    Returns:
    list of pd.DataFrame: List of DataFrames created from the Excel files.
    """
    dataframes = []
    for file_name in file_list:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_name)
        # Append the DataFrame to the list
        dataframes.append(df)

    return dataframes
