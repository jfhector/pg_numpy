import numpy as np

arr = np.array([[1,2,3], 
                [4,5,6]])

# Fancy indexing
# Creates copies, not views

# First and last columns
arr[:, [0, 2]]
