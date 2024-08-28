import numpy as np

monte_carlo_simulation = lambda n: np.sum(np.where(np.random.rand(n) < 1/6, 6, -1.3))

print(monte_carlo_simulation(100))
