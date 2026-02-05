# Slicing in Numpy is a powerful technique that allows you to extract specific portions of an array.
# It is similar to slicing in Python lists but can be applied to multi-dimensional arrays as well. 

# array[start:stop:step] for 1D arrays
# array[start:end]
 
import numpy as np
arr=np.array([10,20,30,40,50,60,70])
print(arr[1:5]) # This will give us the elements from index 1 to index 4 (stop index is exclusive)
print(arr[:4]) # This will give us the elements from index 0 to index 3 (stop index is exclusive)
print(arr[::2]) # This will give us every second element in the array starting from index 0
print(arr[::-1]) # This will give us the elements in reverse order

# The output will be:
# [20 30 40 50]
# [10 20 30 40]
# [10 30 50]
# [70 60 50 40 30 20 10]

