# astype - converts an array to a different data type 

import numpy as np
arr=np.array([1.2,2.5,3.7,4.6])
print(arr.dtype)
int_arr=arr.astype(int)
print(int_arr)
print(int_arr.dtype)


# the output will be:
# float64
# [1 2 3 4]
# int64
# Here, we first create an array of floating-point numbers and check its data type using .dtype property.
# Then, we use the astype(int) method to convert the array to integers.