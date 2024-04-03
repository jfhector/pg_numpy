import numpy as np

# Creating random state objects to ensure the random generates the same values each time (reproductible).
# This could be done just as `np.random.seed(387)`, but doing it separately like below is helpful is not all code is executed, or not in the same sequence
# e.g. when running tests or doing interactive programming
rs = np.random.RandomState(seed=387)

rs.rand(3)
