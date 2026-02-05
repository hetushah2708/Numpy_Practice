# Flattening array used when u want to convert a multi-dimensional array into a one-dimensional array.
# .ravel() -> this will return a view of the original array whenever possible.
# If the original array is not contiguous in memory, it will return a copy.
#.flatten() -> this will always return a copy of the original array, regardless of its memory layout.

import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel) # this will give the output [1 2 3 4 5 6]
print(arr_2d.flatten) # this will also give the output [1 2 3 4 5 6] 

# so the main difference between ravel and flatten is :
# so if ua re working on some project whcih have millions of rows and columns
# so we can use ravel and flatten if we want an o/p in single line array
