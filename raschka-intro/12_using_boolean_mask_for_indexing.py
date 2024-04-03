import numpy as np

arr = np.array([[1,4,3], 
                [4,5,6]])

# Using a boolean mask for indexing

# First and last columns
mask = arr > 3
# mask

arr[mask]
