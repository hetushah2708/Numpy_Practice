#nan_to_num this will replace all the NaN values in an array with a specified value (default is 0).

# Syntax is np.nan_to_num(array, nan=0.0, posinf=None, neginf=None)
'''
here array is the input array containing NaN values,
nan=0.0 is the value to replace NaN values with (default is 0.0),
posinf is the value to replace positive infinity values with (default is None, which means it will not replace positive infinity values),
neginf is the value to replace negative infinity values with (default is None, which means it will not replace negative infinity values).

'''

import numpy as np
arr=np.array= ([1,2,np.nan,4,np.nan,6]) # creating an array with some NaN values
cleaned_arr= np.nan_to_num(arr,nan=120) # this will replace all the NaN values in the array with 120. You can change this value to any other value you want to use for replacement.
print(cleaned_arr)