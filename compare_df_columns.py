import pandas as pd
import sys


def compare_dataframe_columns(dataframes):
    """
    Takes a list of DataFrames and compares the column names in each DataFrame.
    Prints a matrix showing the comparison of column names between each pair of DataFrames.

    Parameters:
    dataframes (list of pd.DataFrame): List of DataFrames to compare.
    """
    num_dfs = len(dataframes)
    has_diff = False

    row = []
    # Nested loop for comparison
    for i in range(num_dfs):
        sub_row = []  # Start the row with the current DataFrame label
        for j in range(num_dfs):
            if i == j:
                sub_row.append("Same")
            else:
                cols_i = sorted(dataframes[i].columns)
                cols_j = sorted(dataframes[j].columns)
                if cols_i == cols_j:
                    sub_row.append("Same")
                else:
                    sub_row.append("Diff")
                    has_diff = True

        row.append(sub_row)
    print("----------------------------------")
    print("Compare Columns:")
    for i in row:
        print(i)
    print("----------------------------------")


    if has_diff == True:
        print("There are different columns in a dataframe")
        sys.exit()

if __name__ == "__main__":
    # Example usage:
    df1 = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })

    df2 = pd.DataFrame({
        'A': [10, 11, 12],
        'C': [13, 14, 15],
        'B': [16, 17, 18]
    })

    df3 = pd.DataFrame({
        'B': [19, 20, 21],
        'C': [22, 23, 24],
        'A': [25, 26, 27]
    })

    dfs = [df1, df2, df3]
    compare_dataframe_columns(dfs)
