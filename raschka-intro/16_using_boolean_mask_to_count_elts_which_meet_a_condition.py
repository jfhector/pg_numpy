import numpy as np

# using boolean masks to check how many elements in an array meet a certain condition
arr = np.array([1,2,3,4,5,6])

mask = (arr >= 2) & (arr % 2 == 0)
# mask = (arr > 2)
# mask = (arr % 2 == 0)

# arr[mask]
# arr[mask].sum()
len(arr[mask])
