# Concate in Advance Numpy is used to join two or more arrays along an existing axis.

# Syntax: numpy.concatenate((array1, array2, ...), axis=0)
'''
if axis is 0 then it will stack row vise meaning vertically
if axis is 1 then it will stack column vise meaning horizontally
'''
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
new_arr=np.concatenate((arr1,arr2)) # concatenating arr1 and arr2
print(new_arr)