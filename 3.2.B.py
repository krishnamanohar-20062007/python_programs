# 3.2.b Find the indices of the max and min numbers along the given axis
import numpy as np
arr2d=np.array([[10,20,30],[40,5,25],[7,50,60]])
# index of max along axix 0 (column wise)
print("ArgMax (axis=0): ",np.argmax(arr2d,axis=0))
# index of min along axix 1 (row wise)
print("ArgMin (axis=1): ",np.argmin(arr2d,axis=1))
