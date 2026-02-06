# Vectorization in Numpy is used to perform operations on arrays without using explicit loops.

import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

result = arr1 + arr2 # Vectorized operation, adds corresponding elements of the two arrays
print(result)

#the output will be :
# [5 7 9]