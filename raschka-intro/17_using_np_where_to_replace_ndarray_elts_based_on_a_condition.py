import numpy as np

# using boolean masks to check how many elements in an array meet a certain condition
arr = np.array([1,2,3,4,5,6])

np.where(arr > 2, 1, 0)
