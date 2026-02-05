# if you want to check the number of dimensions in an array, you can use the .ndim property.

import numpy as np
arr_1d=np.array([1,2,3])
arr_2d=np.array([[1,2,3], [4,5,6]])
arr_3d=np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

#the output will be:
# 1
# 2
# 3
# Here, the outputs 1, 2, and 3 indicate that arr_1d is a 1-dimensional array,
# arr_2d is a 2-dimensional array, and arr_3d is a 3-dimensional array.