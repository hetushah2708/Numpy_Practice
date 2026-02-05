# If you want to check the shape of an array, you can use the .shape property. 
# This will return a tuple representing the dimensions of the array.

import numpy as np
arr_2d=np.array([[1,2,3],
                 [4,5,6]])
print(arr_2d.shape)

# the output will be:
# (2, 3)
# Here, the output (2, 3) indicates that the array has 2 rows and 3 columns.