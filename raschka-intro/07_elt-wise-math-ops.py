import numpy as np

arr = np.array([[1,2,3], [4,5,6]])

# Using nested for loops

# for rowindex, rowvalue in enumerate(arr):
#   for colindex, colvalue in enumerate(rowvalue):
#     arr[rowindex, colindex] += 1

# Using list comprehensions

# arr = [[el + 1 for el in row] for row in arr]

arr + 1
