# axis 1= row wise
# axis 0= column wise
import numpy as np
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m.sum(axis=0))   # [5 7 9]  -> column-wise
print(m.sum(axis=1))   # [6 15]   -> row-wise