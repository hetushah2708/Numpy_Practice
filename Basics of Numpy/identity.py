# Creating Identity Matrices in numpy
# Identity matrix is a square matrix with ones on the main diagonal and zeros elsewhere
#eye(size)

import numpy as np
identity_matrix=np.eye(3)
print(identity_matrix)

# The out put will be:
# [[1. 0. 0.]    so 1's are at diagonal posotions and 0's are at elewhere
#  [0. 1. 0.]
#  [0. 0. 1.]]
