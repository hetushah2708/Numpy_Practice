# Reshaping means changing the shape of an array without changing its data.
# like changing a 1D array to 2D or 3D array.
# reshape(rows, columns) specify new shape, if dimesnions match 

import numpy as np
arr=np.array([1,2,3,4,5,6])
reshaped_Arr=arr.reshape(2,3)
print(reshaped_Arr)

# the output will be:
# [[1 2 3]
#  [4 5 6]]

# so basically it converted 1D array to 2D array with 2 rows and 3 columns