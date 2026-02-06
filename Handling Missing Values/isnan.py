# isnan in numpy is used for checking if the elements of an array are NaN (Not a Number). 
# It returns a boolean array where True indicates the presence of NaN values 
# and False indicates the absence of NaN values.

# syntax: np.isnan(array)

import numpy as np
arr=np.array([1,2,np.nan,4,np.nan,6]) # creating an array with some NaN values

print(np.isnan(arr)) # this will return a boolean array indicating the presence of NaN values


# the output will be :
# [False False  True False  True False]
# here Flase means the value is not NaN and True means the value is NaN.


# FOR INTERVIEW PURPOSES:
# 1. CAN U COMPARE np.nan==np.nan
#soltion is we cannot compare this since np.nan is not equal to itself, so the result will be False.
