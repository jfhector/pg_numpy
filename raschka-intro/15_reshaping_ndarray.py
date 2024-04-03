import numpy as np

# ndarray sizes are fixed, but their shapes are not
# so if we need the array in a different shape, we can reshape it without needing to create a new one
arr = np.array([1,2,3,4,5,6])

# reshaped_arr = arr.reshape([3, 2])
# same as:
# reshaped_arr = arr.reshape([3, -1])

# flattens
reshaped_arr = arr.reshape([-1])

reshaped_arr
# np.may_share_memory(arr, reshaped_arr)
