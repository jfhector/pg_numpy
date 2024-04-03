import numpy as np

arr = np.array([[1,2,3], 
                [4,5,6]])

# Basic indexing and slicing routines create memory views of (references to positions in) the original ndarray, not copies
fst_row = arr[0]
fst_row += 10
arr
