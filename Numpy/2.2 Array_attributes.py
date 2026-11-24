import numpy as np
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)   # (2, 3)  -> rows, columns
print(b.ndim)    # 2       -> number of dimensions
print(b.size)    # 6       -> total elements
print(b.dtype)   # int64   -> data type