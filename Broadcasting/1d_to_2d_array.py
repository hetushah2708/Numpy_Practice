# how to do broadcasting from 1d to 2d array in numpy
import numpy as np
matrix= np.array([[1,2,3],[4,5,6]]) # 2x3 matrix
vector=np.array([10,20,30]) # 1D aaray 

reuslt = matrix + vector # Broadcasting will automatically apply the operation to each row of the matrix
print(reuslt) 

# the output will be :
# [[11 22 33]
#  [14 25 36]]
