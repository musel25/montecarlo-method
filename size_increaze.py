import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
true_value = 1/3

# Try different sample sizes
sample_sizes = [10, 100, 1000, 10000, 100000]

estimates = []
for n in sample_sizes:
    X = np.random.uniform(0, 1, n)
    estimate = np.mean(X**2)
    estimates.append(estimate)

# Plot results
plt.figure(figsize=(10, 6))
plt.axhline(y=true_value, color='r', linestyle='--', label='True value (1/3)')
plt.plot(sample_sizes, estimates, 'bo-', label='Monte Carlo estimates')
plt.xscale('log')
plt.grid(True)
plt.xlabel('Number of samples')
plt.ylabel('Estimated value')
plt.title('Monte Carlo Estimates vs. Number of Samples')
plt.legend()
plt.show()

# Print numerical results
for n, est in zip(sample_sizes, estimates):
    print(f"Samples: {n:5d}, Estimate: {est:.4f}, Error: {abs(est-true_value):.4f}")