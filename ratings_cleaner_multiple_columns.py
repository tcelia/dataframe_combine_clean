import pandas as pd

def filter_rows_by_tags(dataframe, tags, columns_to_check):
    """
    Filters rows from the DataFrame based on the values in specified columns.
    Keeps rows where at least three values in the specified columns are in the list of tags.

    Parameters:
    dataframe (pd.DataFrame): DataFrame containing the data.
    tags (list): List of tags to check against.
    columns_to_check (list): List of column names to check.

    Returns:
    pd.DataFrame: DataFrame with rows filtered based on the specified criteria.
    """
    # Count the number of tags present in each row for the specified columns
    tags_count = dataframe[columns_to_check].apply(lambda row: sum(tag in row.values for tag in tags), axis=1)

    # Keep rows where at least three tags are present
    filtered_df = dataframe[tags_count >= 3]

    return filtered_df

if __name__ == "__main__":
    # Example usage:
    df = pd.DataFrame({
        'cola': ['tag1', 'tag2', 'tag3', 'tag4'],
        'colb': ['tag5', 'tag6', 'tag7', 'tag8'],
        'colc': ['tag1', 'tag2', 'tag3', 'tag4'],
        'cold': ['tag1', 'tag2', 'tag3', 'tag4'],
        'col_other': ['other1', 'other2', 'other3', 'other4']
    })

    # List of tags
    tags_list = ['tag1', 'tag2', 'tag3']

    # Columns to check for tags
    columns_to_check = ['cola', 'colb', 'colc', 'cold']

    # Filter rows based on the specified criteria
    filtered_df = filter_rows_by_tags(df, tags_list, columns_to_check)
    print("DataFrame after filtering rows:")
    print(filtered_df)
