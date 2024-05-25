import pandas as pd

def delete_rows_by_ids(dataframe, id_column, id_list):
    """
    Deletes rows from the DataFrame where the ID column value is in the given list of IDs.

    Parameters:
    dataframe (pd.DataFrame): DataFrame containing the data.
    id_column (str): Name of the column containing unique identifiers.
    id_list (list): List of IDs to delete.

    Returns:
    pd.DataFrame: DataFrame with rows deleted based on the provided IDs.
    """
    # Boolean indexing to filter out rows with IDs in the id_list
    filtered_df = dataframe[~dataframe[id_column].isin(id_list)]

    return filtered_df

if __name__ == "__main__":
    # Example usage:
    df = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'cusip': ['123456', '789012', '123456', '345678', '789012'],
        'selected_column': ['value1', 'value2', 'value1', 'value3', 'value4']
    })

    # List of IDs to delete
    ids_to_delete = [2, 4]

    # Delete rows from DataFrame based on the list of IDs
    updated_df = delete_rows_by_ids(df, 'id', ids_to_delete)
    print("DataFrame after deleting rows:")
    print(updated_df)
