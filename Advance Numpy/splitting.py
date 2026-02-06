#Splitting in Advance Numpy is used to divide an array into multiple sub-arrays.
# It is useful for data manipulation and analysis. 
# There are several functions in numpy that can be used for splitting, 
# including `np.split`, `np.hsplit`, and `np.vsplit`.


import numpy as np
arr=np.array([1,2,3,4,5,6])
print(np.split(arr,2)) # Splitting into 2 equal parts

# the output will be :
# [array([1, 2, 3]), array([4, 5, 6])]
