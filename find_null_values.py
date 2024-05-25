import pandas as pd

def find_unique_null_ids(dataframe, id_column, column_name):
    """
    Finds unique IDs where null values are found in the specified column.

    Parameters:
    dataframe (pd.DataFrame): DataFrame containing the data.
    id_column (str): Name of the column containing unique identifiers.
    column_name (str): Name of the column to check for null values.

    Returns:
    list: List of unique IDs corresponding to rows where null values are found in the specified column.
    """
    # Filter rows where the specified column has null values
    null_rows = dataframe[dataframe[column_name].isnull()]

    # Get unique IDs from the filtered rows
    unique_null_ids = null_rows[id_column].unique().tolist()

    return unique_null_ids

if __name__ == "__main__":
    # Example DataFrame
    df = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'cola': ['abc', 'def', None, 'jkl'],
        'colb': ['mno', None, 'uvw', 'xyz'],
        'colc': ['123456', 'abc', 'def', 'xyz']
    })

    # Column name to check for null values
    column_to_check = 'colb'

    # Find unique IDs where nulls are found in the specified column
    unique_null_ids = find_unique_null_ids(df, 'id', column_to_check)
    print(f"Unique IDs with nulls in column '{column_to_check}': {unique_null_ids}")
