import pandas as pd


def combine_dfs(dfs):
    '''Takes in a list of dataframes. Assumes all dataframes have the same columns.
    Returns the combined dataframe'''
    
    # Concatenate the DataFrames vertically
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

if __name__ == '__main__':
    # Example DataFrames
    df1 = pd.DataFrame({
        'a': ['a', 'a', 'a'],
        'b': ['b', 'b', 'b'],
        'c': ['c', 'c', 'c']
    })

    df2 = pd.DataFrame({
        'a': ['A', 'A', 'A'],
        'c': ['C', 'C', 'C'],
        'b': ['B', 'B', 'B']
    })
    dfs = [df1, df2]
# Concatenate the DataFrames vertically
    final_df = combine_dfs(dfs)
    print(final_df)
