import numpy as np

def assign_weights_to_ids(ids, weights):
    """
    Randomly assigns weights to IDs.

    Parameters:
    ids (list): List of IDs.
    weights (list): List of weights to assign.

    Returns:
    dict: Dictionary mapping IDs to their assigned weights.
    """
    # Shuffle the list of IDs to randomize the order
    shuffled_ids = np.random.permutation(ids)

    # Initialize an empty dictionary to store the assignments
    assignments = {}

    # Assign weights to IDs
    for asset_id in shuffled_ids:
        weight = np.random.choice(weights)
        assignments[asset_id] = weight

    return assignments

# Example usage:
if __name__ == "__main__":
    # Example lists of IDs and weights
    ids = range(1, 501)  # Assuming IDs are sequential integers from 1 to 500
    weights = [0.1, 0.2, 0.3, 0.4]

    # Assign weights to IDs
    assignments = assign_weights_to_ids(ids, weights)

    # Print the assignments (for demonstration purposes)
    print("Assignments:")
    for asset_id, weight in assignments.items():
        print(f"ID: {asset_id}, Weight: {weight}")