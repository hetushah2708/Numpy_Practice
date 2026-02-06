import numpy as np
prices= np.array([100,200,300])
discount= 10 # 10% discount which is a single value
final_prices = prices - (prices * discount/100) # Broadcasting will automatically apply the operation to each element in the prices array
print(final_prices)
# the output will be :  
# [ 90. 180. 270.]

# There are certain rukes for broadcasting to work:
# 1. If the arrays have different number of dimensions, the shape of the smaller array is padded with ones on its leading (left) side.
# 2. If the shape of the arrays does not match in any dimension, 
# the array with shape equal to 1 in that dimension is stretched to match the other shape.
# 3. If in any dimension the sizes disagree and neither is equal to 1, an error is raised.