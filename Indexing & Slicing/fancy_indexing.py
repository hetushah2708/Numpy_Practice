# Fancy Indexing is selecting multtiple elements at once

import numpy as np
arr=np.array([10,20,30,40,50,60,70])
print(arr[[0,2,4]]) # this will give the output [10 30 50]
print(arr[[-1,-2,2]]) # this will give the output [70 60 30]