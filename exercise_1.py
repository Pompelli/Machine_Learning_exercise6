import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 10000  # Number of tosses
bias_percentage = 51  # Bias percentage, can be adjusted between 50 and 100
prob_biased_head = bias_percentage / 100  # Convert percentage to a probability

# Simulate the biased coin tosses using NumPy (vectorized)
tosses = np.random.rand(n) < prob_biased_head  # True for heads, False for tails

# Calculate the cumulative proportion of heads
proportions = np.cumsum(tosses) / np.arange(1, n+1)

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(np.arange(1, n+1), proportions, label="Simulated Proportion of Heads", color="blue")
plt.axhline(y=prob_biased_head, color='red', linestyle='--', label=f'Expected Bias ({bias_percentage}%)')
plt.title(f"Biased Coin Toss Simulation (Bias: {bias_percentage}%)")
plt.xlabel("Number of Tosses")
plt.ylabel("Proportion of Heads")
plt.legend()
plt.grid(True)
plt.show()
