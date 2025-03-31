import numpy as np
np.random.seed(42)  # for reproducibility

# Generate 1000 random numbers between 0 and 1
X = np.random.uniform(0, 1, 1000000)
# Calculate h(X) = X²
hX = X**2
# Calculate the mean
estimate = np.mean(hX)

print(f"Monte Carlo estimate with 1000 points: {estimate:.4f}")
print(f"True value (∫₀¹ x² dx = 1/3): {1/3:.4f}")