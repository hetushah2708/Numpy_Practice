# np.isinf() this is used for checking if the elements of an array are infinite (positive or negative infinity).

# so basically this type of calculation wich exceed the pythins number limit will be treated as infinite.

#Syntax is np.isinf(array)

import numpy as np
arr=np.array([1,2,np.inf,4,-np.inf,6]) # creating an array with some infinite values
print(np.isinf(arr)) # this will return a boolean array indicating the presence of infinite values  

# now how to replace infinite number with the finit number

cleaned_arr=np.nan_to_num(arr,posinf=1000, neginf=-1000)
#this will replace all the positive infinite values with 1000 and negative infinite values with -1000.
# You can change these values to any other values you want to use for replacement.

print(cleaned_arr)

# the output will be :
#[False False  True False  True False]
# [    1.     2.  1000.     4. -1000.     6.]