import numpy as np

arr = np.array([[1,4,2], 
                [4,5,6]])

# Using a boolean mask for indexing

# mask = arr > 3
# mask = (arr > 3) & (arr % 2 == 0)
# mask = (arr > 3) | (arr % 2 == 0)
# mask

# arr[mask]
arr[(arr > 3) & (arr % 2 == 0)]
