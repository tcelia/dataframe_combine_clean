import pandas as pd

def assign_lot_weights(dataframe, weights):
    """
    Assigns lot-level weights based on the provided weights and par amounts in the DataFrame.

    Parameters:
    dataframe (pd.DataFrame): DataFrame containing the data.
    weights (dict): Dictionary mapping IDs to their assigned weights.

    Returns:
    pd.DataFrame: DataFrame with lot-level weights assigned.
    """
    # Merge DataFrame with weights
    dataframe['Weight'] = dataframe['ID'].map(weights)

    # Group by ID and calculate total par amount for each ID
    grouped = dataframe.groupby('ID')['Par'].sum().reset_index()

    # Merge total par amounts back to the original DataFrame
    dataframe = pd.merge(dataframe, grouped, on='ID', suffixes=('', '_total'))

    # Calculate lot-level weights based on proportion of total par amount
    dataframe['Lot Weight'] = dataframe['Par'] / dataframe['Par_total'] * dataframe['Weight']

    return dataframe

# Example usage:
if __name__ == "__main__":
    # Example DataFrame
    df = pd.DataFrame({
        'ID': ['ID1', 'ID1', 'ID2', 'ID2'],
        'Par': [75, 25, 50, 50]  # Example par amounts
    })

    # Example weights (you can replace this with your own weights)
    weights = {'ID1': 0.2, 'ID2': 0.3}

    # Assign lot-level weights
    df_with_weights = assign_lot_weights(df, weights)

    print("DataFrame with Lot-Level Weights:")
    print(df_with_weights)
