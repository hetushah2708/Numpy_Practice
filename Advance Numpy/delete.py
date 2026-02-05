# delete in Advance Numpy is used to remove elements from an array.

# Syntax: np.delete(array, index, axis=None)
 
# delete of 1d array
import numpy as np
arr=np.array([10,20,30,40,50,60,70])
print(arr)
new_arr=np.delete(arr,0) # deleting the element at index 0 (which is 10)
print(new_arr)

# delte of 2d array
import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d)
new_arr_2d=np.delete(arr_2d,0,axis=0) # deleting the row at index 0 (which is [1,2,3])
# here 0 means i wanna delete the 0th row i.e [1,2,3] and axis=0 means i wanna delete row vise
print(new_arr_2d)