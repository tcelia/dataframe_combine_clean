import pandas as pd

def get_unique_ids_for_values(dataframe, id_column, selected_column, value_list):
    """
    Finds all instances where the selected column has a value present in the given list.
    Returns a list of unique ids for those rows.

    Parameters:
    dataframe (pd.DataFrame): DataFrame containing the data.
    id_column (str): Name of the column containing unique identifiers.
    selected_column (str): Name of the column to search for values.
    value_list (list of str): List of strings to search for in the selected column.

    Returns:
    list: List of unique identifiers corresponding to rows where selected column values match the list.
    """
    # Boolean indexing to filter rows where the selected column has values in the value_list
    filtered_rows = dataframe[dataframe[selected_column].isin(value_list)]

    # Get unique ids from the filtered rows
    unique_ids = filtered_rows[id_column].unique().tolist()

    return unique_ids


def get_unique_ids_for_values_not_in(dataframe, id_column, selected_column, value_list):
    """
    Finds all instances where the selected column's value is not present in the given list.
    Returns a list of unique ids for those rows.

    Parameters:
    dataframe (pd.DataFrame): DataFrame containing the data.
    id_column (str): Name of the column containing unique identifiers.
    selected_column (str): Name of the column to search for values.
    value_list (list of str): List of strings to check for absence in the selected column.

    Returns:
    list: List of unique identifiers corresponding to rows where selected column values are not in the list.
    """
    # Boolean indexing to filter rows where the selected column's value is not in the value_list
    filtered_rows = dataframe[~dataframe[selected_column].isin(value_list)]

    # Get unique ids from the filtered rows
    unique_ids = filtered_rows[id_column].unique().tolist()

    return unique_ids


if __name__ == "__main__":
    # Example usage:
    df = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'cusip': ['123456', '789012', '123456', '345678', '789012'],
        'selected_column': ['value1', 'value2', 'value1', 'value3', 'value4']
    })

    # List of strings to search for in the 'selected_column'
    search_values = ['value1', 'value2']

    # Get unique ids for rows where 'selected_column' has values in the search_values list
    unique_ids = get_unique_ids_for_values(df, 'id', 'selected_column', search_values)
    print("Unique IDs:", unique_ids)
