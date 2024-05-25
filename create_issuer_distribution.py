import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_portfolio_weights(num_assets, average_issuer_size):
    """
    Generates a distribution of portfolio weights based on average issuer size.

    Parameters:
    num_assets (int): Number of assets to select.
    average_issuer_size (float): Average issuer size.

    Returns:
    np.array: Array representing the portfolio weights.
    """
    # Generate weights following a log-normal distribution with a shorter right tail
    weights = np.random.lognormal(mean=np.log(average_issuer_size), sigma=0.2, size=num_assets)

    # Ensure all weights are above zero
    weights = np.maximum(weights, 0.01)  # Set minimum weight to 0.01 for stability

    # Normalize weights to sum up to 100%
    weights /= np.sum(weights)
    weights *= 100

    # Adjust weights to match the specified average issuer size
    weights *= average_issuer_size / np.mean(weights)

    return weights

if __name__ == "__main__":
    # Parameters
    num_assets = 300
    average_issuer_size = 0.45
    num_buckets = 10

    # Generate portfolio weights
    portfolio_weights = generate_portfolio_weights(num_assets, average_issuer_size, num_buckets)

    # Create histogram
    plt.figure(figsize=(10, 6))
    plt.hist(portfolio_weights, bins=15, color='skyblue', edgecolor='black')
    plt.title('Portfolio Weights Histogram')
    plt.xlabel('Weights')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
