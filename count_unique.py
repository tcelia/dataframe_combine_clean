import pandas as pd

def count_unique_cusips(dataframe, count_column):
    """
    Counts the number of unique values in the count_column of the given DataFrame.

    Parameters:
    dataframe (pd.DataFrame): DataFrame containing the count column.

    Returns:
    int: Number of unique values in the count column.
    """
    # Use nunique() to count the number of unique values in the 'cusip' column
    unique_cusips = dataframe[count_column].nunique()

    print(f"Number of unique values in {count_column}:", unique_cusips)
    
    return unique_cusips

if __name__ == "__main__":
    # Example DataFrame
    portfolio_df = pd.DataFrame({
        'cusip': ['123456', '789012', '123456', '345678', '789012', '901234']
    })

    # Count the unique cusips in the DataFrame
    unique_cusips_count = count_unique_cusips(portfolio_df, 'cusip')