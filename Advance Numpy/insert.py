# Insert in Advance Numpy is used to insert values into an array at specified indices.

'''
Syntax is : np.insert(array, index, value, axis=None)
here array is the OG array
index is the position where you want to insert the value
value is the value you want to insert
axis is the axis along which to insert the values. If None, the input array is flattened
'''

import numpy as np
arr=np.array([10,20,30,40,50,60,70])
new_arr=np.insert(arr,2,100) # inserting 100 at index 2
print(new_arr) 

# the output will be:
# [ 10  20 100  30  40  50  60  70]
# Here, 100 is inserted at index 2, and the rest of the elements are shifted to the right.

arr_2d= np.array([[1,2],[3,4]])
print(arr_2d)
new_arr_2d=np.insert(arr_2d,1,[5,6],axis=0) # inserting [5,6] at index 1 along axis 0 (rows)
print(new_arr_2d)