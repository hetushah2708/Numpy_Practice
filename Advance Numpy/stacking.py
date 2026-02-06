# Stacking in Advance numpy is used to combine multiple arrays along a specified axis.
# It is a powerful tool for creating new arrays from existing ones.
# There are several functions in numpy that can be used for stacking, 
# including `numpy.stack`, `numpy.hstack`, and `numpy.vstack`.

import numpy as np  
arr_1=np.array([1,2,3])
arr_2=np.array([4,5,6])
print(np.vstack((arr_1,arr_2)))  # Stacking vertically
print(np.hstack((arr_1,arr_2)))  # Stacking horizontally
